import json
import logging
import os
from functools import wraps
from typing import Callable, Optional

logger = logging.getLogger("evaluation")


def json_from_column(prompt_fn: Callable = None, namedtuple_key: str = None, data_path: Optional[str] = None):
    """
    Handles reading a JSON file from a specified path then passing the contents to
    the relevant function. Allows the original function to act as if the JSON file
    contents were passed directly to it.

    Can be used as a decorator or as a function.

    Parameters
    ----------
    prompt_fn : Callable
        Function to be called with the JSON data, by default None
        When used as a decorator, this is implicitly the target function.
    namedtuple_key : str
        The key to access the filename in the namedtuple, by default None
    data_path : str, optional
        The path to the directory containing the JSON file, by default None
    """
    if namedtuple_key is None:
        raise ValueError("namedtuple_key must be provided")

    def decorator(fn):
        @wraps(fn)
        def wrapped(sample: "namedtuple"):
            """
            The sample is expected to be a namedtuple with the key specified by namedtuple_key.

            This is passed in by the evaluation loop when using file descriptors to the data.
            """

            # Get the file path from the namedtuple using the key
            filename = getattr(sample, namedtuple_key) + ".json"
            if data_path:
                filename = os.path.join(data_path, filename)

            if not filename or not os.path.isfile(filename):
                raw_json = {}
            else:  # Open the file and read its contents
                with open(filename, "r") as file:
                    raw_json = json.load(file)

            # Call the original function with the file contents
            return fn(raw_json)

        return wrapped

    # When using as a function pass, wrap the first argument
    if callable(prompt_fn):
        return decorator(prompt_fn)

    # When using as a decorator, the caller will apply it to the target function
    return decorator


def to_user_messages(prompt_fn: Callable = None, system_message: Optional[str] = None):
    """
    Handles transforming a resolved prompt to a LiteLLM message array.

    Can be used as a decorator or as a function.

    Parameters
    ----------
    prompt_fn : Callable
        Function to be called with the resolved prompt, by default None
        When used as a decorator, this is implicitly the target function.
    system_message : Optional[str], optional
        When provided will insert this as the first message with role system, by default None
    """

    def decorator(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            resolved_prompt = fn(*args, **kwargs)

            messages = [] if system_message is None else [{"role": "system", "content": system_message}]
            messages.append({"role": "user", "content": resolved_prompt})
            return messages

        return wrapped

    # When using as a function pass, wrap the first argument
    if callable(prompt_fn):
        return decorator(prompt_fn)
    # When using as a decorator, the caller will apply it to the target function
    return decorator


def prompt_compilation(
    prompt_pattern: str, pattern_kwargs: dict, rubric_library: dict, rubric_keys: Optional[list] = None
) -> str:
    """
    Compiles a prompt pattern with the provided pattern kwargs and rubrics.

    This supports the first level of "doubly-resolved" prompts. This step is done to take a rubric pattern and have
    a use-case specific prompt but will NOT have anything specific to case being evaluated. That should be done in a
    subsequent application of pattern.format. Allows processing a subset of the defined criteria by passing a list of
    keys to the rubric_library.
    If no keys are provided, all rubrics will be included.

    Parameters
    ----------
    prompt_pattern : str
        an f-string template for the prompt
    pattern_kwargs : dict
        a dictionary of keyword arguments to format the prompt
    rubric_library : dict
        a dictionary mapping rubric keys to their descriptions
    rubric_keys : Optional[list], optional
        a list of keys to specify which rubrics to include, by default None

    Returns
    -------
    str
        The formatted prompt template with the specified rubrics included.
        Ready to resolve into a specific prompt via string.format
    """
    if rubric_keys is None:
        rubrics = "\n".join(list(rubric_library.values()))
    else:
        good_keys = [k for k in rubric_keys if rubric_library.get(k) is not None]
        if len(good_keys) < len(rubric_keys):
            logger.warning(
                f"Requested rubric keys not found, omitting: {', '.join(set(rubric_keys) - set(good_keys))}"
            )
        rubrics = "\n".join([rubric_library[k] for k in good_keys])
    if rubrics:
        pattern_kwargs["RUBRIC_SET"] = rubrics
    general_prompt = prompt_pattern.format(**pattern_kwargs)

    return general_prompt
