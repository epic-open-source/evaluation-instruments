import json
import logging
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

from evaluation_instruments.model import TokenUsage

logger = logging.getLogger("evaluation")


class Evaluation:
    """
    Object managing the evaluation of a dataset using a specified instrument for evaluation.

    The pipeline during evaluation will call the prep_fn with a line of the dataset, passing the output to
    the completion_fn, which will call the model provider. The output of the model provider is then passed
    to the post_process_fn.

    DataFrame --> prep_fn --> completion_fn --> post_process_fn --> parsed results

    Evaluators will always require a completion function that delegates to a model provider, assuming the protocol
    supported by LiteLLM. This is a singular function that can accept a model descriptor, a message array,
    and any necessary model provider kwargs, then return a json response.

    The default post_process_fn assumes the OpenAI format, and will extract a response from
    response['choices'][0]['message']['content'] and attempt to parse it as its own json object.
    It will also parse response['usage'] into a TokenUsage object which will be used to abort a run after the
    first request exceeding the capacity specified (default 10_000 tokens).


    Parameters
    ----------
    prep_fn : callable, optional
        This function resolves a prompt for a single row of data (ex. a single summary)
        The instrument generally defines this as well as expectations around the input values.
    completion_fn : callable, optional
        This function handles the model completion process.
        Passing in a partial of litellm.completion is expected to be the most common use.
    post_process_fn : callable, optional
        This function processes the model's response, by default will assume OpenAI format and parse
        the message from the first choices node into json as the response, as well as tracking 'usage' for
        token usage.
    log_enabled : bool, optional
        a flag when true will log raw responses from completion to tmp/, by default True
    model_args : dict, optional
        a dictionary of additional kwargs to pass to the completion function, by default {}
    max_tokens : _type_, optional
        a capacity limit for an individual dataset evaluation, by default 10_000
        will stop the evaluation loop after the first request exceeding this limit
    log_prefix : Optional[str], optional
        An optional prefix for the log directory within the temporary logging path, by default None.
        Useful for organizing logs from different evaluation runs.
    """

    def __init__(
        self,
        prep_fn: callable = None,
        completion_fn: callable = None,
        post_process_fn: callable = None,
        log_enabled: bool = True,
        model_args: dict = {},
        max_tokens: int = 10_000,
        log_prefix: Optional[str] = None,
    ):
        self.prep_fn = prep_fn
        self.completion_fn = completion_fn
        self.post_fn = post_process_fn or self.post_process_default

        self.log_enabled = log_enabled
        self._model_args = model_args or {}
        self._log_prefix = log_prefix
        

        self.tmp_dir: Optional[Path] = None
        self.capacity: TokenUsage = TokenUsage(None, None, max_tokens)

        logger.debug(f"Set up with {log_enabled=} and capacity {max_tokens}")

    @property
    def prep_fn(self):
        return self._prep_fn

    @prep_fn.setter
    def prep_fn(self, fn):
        self._prep_fn = fn

    @property
    def completion_fn(self):
        return self._completion_fn

    @completion_fn.setter
    def completion_fn(self, fn):
        self._completion_fn = fn

    @property
    def post_fn(self):
        return self._post_fn

    @post_fn.setter
    def post_fn(self, fn):
        self._post_fn = fn

    @property
    def log_enabled(self):
        return self._log_enabled

    @log_enabled.setter
    def log_enabled(self, enabled: bool):
        self._log_enabled = enabled

    def toggle_logging(self):
        self._log_enabled = not self._log_enabled

    def run_dataset(self, df: "pd.DataFrame", model: str = None, capacity: int = None) -> tuple[dict, TokenUsage]:
        """
        Run the evaluation on a dataset, returning a dictionary of responses and a TokenUsage object.

        Parameters
        ----------
        df : pd.DataFrame
            The dataset to evaluate, expected to be a DataFrame.
            Individual rows will be passed to the prep_fn in the evaluation loop.
        model : str, optional
            The model to use for evaluation, by default None
            Passed as the first argument to the completion function.
        capacity : int, optional
            The maximum token capacity for the evaluation, by default None
            If not provided, will use the default capacity set in the class.
        """
        if df is None or len(df) == 0:
            logger.warning("Empty DataFrame provided for evaluation.")
            return {}, TokenUsage(0, 0, 0)

        tmp_dir = None
        outputs = {}
        accumulated_usage = TokenUsage(0, 0, 0)
        max_usage = self.capacity if not capacity else TokenUsage(None, None, capacity)

        for sample in df.itertuples():
            sample_ix = sample.Index

            # Resolve prompt
            prompt = self.prep_fn(sample)

            # Delegate
            raw_output = self.completion_fn(model=model, messages=prompt, **self._model_args)

            response, usage = self._post_fn(sample_ix, raw_output)
            accumulated_usage += TokenUsage(**usage)

            outputs[sample_ix] = response
            logger.debug(f"{sample_ix}-Completed evaluation")

            # abort if beyond capacity
            if accumulated_usage > max_usage:
                logger.warning(f"Aborting run after {sample_ix}. Capacity exceeded: {accumulated_usage} > {max_usage}")
                break

        if self.tmp_dir is not None:
            logger.info(f"Dumped raw content to {tmp_dir}")

        return outputs, accumulated_usage

    def _dump_to_temp(self, sample_ix, raw_content) -> Optional[Path]:
        """
        Dumps the raw content to a file in a temporary directory, if logging is enabled.

        Parameters
        ----------
        sample_ix :
            the index from the dataset frame
        raw_content :
            the content to be dumped; attempts to serialize as json if dict, otherwise writes as text

        Returns
        -------
        Path
            the temporary directory where the file was dumped
        """

        if not self.log_enabled:
            return None

        datestamp = datetime.now().strftime("%Y%m%d-%Hh")  # Generate a timestamp in the format YYYYMMDD-hhmm

        if self.tmp_dir is None:
            log_base_dir = Path(tempfile.gettempdir()) / "evaluation_logs"
            if self._log_prefix:
                tmp_dir = log_base_dir / f"{self._log_prefix}_{datestamp}"
            else:
                tmp_dir = log_base_dir / f"{datestamp}"
            tmp_dir.mkdir(parents=True, exist_ok=True)
            self.tmp_dir = tmp_dir

        timestamp = datetime.now().strftime("%H%M%S")  # Generate a timestamp in the format hhmmss
        filepath = self.tmp_dir / f"{sample_ix}_raw_{timestamp}.json"

        with open(filepath, "w") as f:
            # Write the raw content to the file
            if isinstance(raw_content, dict):
                json.dump(raw_content, f)
            else:
                f.write(str(raw_content))

    def post_process_default(self, sample_ix, openai_json: dict) -> tuple[dict, TokenUsage]:
        """
        The default post-processing function, assuming OpenAI responses of choices plus a usage node.

        This function will extract the first choice's message content and parse it as JSON.
        It will also extract the usage information from the response.

        Parameters
        ----------
        sample_ix :
            The index of the sample being processed.
        openai_json : dict
            The JSON response from OpenAI containing choices and usage information.

        Returns
        -------
        tuple[dict, dict]
            deserializes the response['choices'][0]['message']['content'] and returns it as a dict,
            as well as the usage information from response['usage'].
        """
        ix = 0  # assume N=1
        try: #  Many providers have their own response objects, try to convert
            openai_json = openai_json.json()
        except AttributeError:
            pass

        if isinstance(openai_json, str):
            openai_json = json.loads(openai_json)

        try:
            raw_content = openai_json["choices"][ix]["message"]["content"]
            response = json.loads(raw_content[raw_content.find("{") : raw_content.rfind("}") + 1])  # noqa: E203
        except Exception:
            logger.info(f"Failed to parse {sample_ix} response content as JSON.")
            response = {}

        usage = openai_json.get("usage", {"completion_tokens": 0, "prompt_tokens": 0, "total_tokens": 0})

        self._dump_to_temp(sample_ix=sample_ix, raw_content=openai_json)
        return response, usage


__all__ = ["Evaluation"]
