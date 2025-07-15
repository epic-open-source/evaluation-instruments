# Evaluation-Instruments

This repository contains a collection of evaluation instruments with a focus on AI use cases for healthcare. The instruments were developed to support both manual evaluation by trained evaluators and automated evaluation approaches such as deterministic statistical methods or probabilistic LLM-as-a-Judge. The instruments were initially calibrated to support specific use cases and should be reviewed prior to use if the planned use case differs. 

The instruments provide a consistent interface for inputs and outputs to aid in reuse between use cases, composition into pipelines, and integration with [seismometer](https://epic-open-source.github.io/seismometer/) for analysis. If an instrument requires an LLM, the [litellm SDK](https://docs.litellm.ai/) API protocol is encouraged to streamline usage across language models. 

## How to use

This package is not currently published to PyPI, so it must be installed from source. It also does not provide direct support for interfacing with generative models, as this is an implicit requirement for generating the outputs needing evaluation.

### Installation

This package is not currently published to PyPI, but it can be installed directly from GitHub using `pip`. This is the recommended approach for programmatic use (e.g., from scripts or services):

```bash
pip install git+https://github.com/epic-open-source/evaluation-instruments.git
```

This installs the package along with evaluation instruments — rubrics, prompts, and supporting logic — used to assess AI-generated outputs in specific clinical contexts. Instruments are included for completeness but are not required for all workflows or runtime use.

Alternatively, you can clone the repository into a directory accessible to your Python environment,

```bash
git clone https://github.com/epic-open-source/evaluation-instruments.git
```

and then run:

```bash
pip install .
```

This is useful if you want to inspect or modify the instrument definitions before installation.

### Getting Started

Navigate to the instrument of your choice, such as the [PDSQI-9](https://github.com/epic-open-source/evaluation-instruments/blob/main/instruments/pdsqi_9/README.md).

Using an instrument typically involves two steps:

1. **Configure your backing model** - The package follows the [LiteLLM](https://docs.litellm.ai/) protocol for model integration. You'll need a function that accepts a messages array and returns an OpenAI-style JSON response. Using LiteLLM directly can simplify this to setting a few environment variables.

2. **Align your data** - The examples use a pattern where content for evaluation is stored in separate files to minimize memory usage. A DataFrame is built to store paths to these files. File contents are instrument and use-case dependent:
    - For PDSQI-9, each file contains:
      - `summary`: The text string being evaluated
      - `notes`: A list of text representing the raw information being summarized
      - `target_specialty`: The specialty of the target user

### Running Evaluations

When running evaluations, you can set a `max_tokens` threshold to stop after the first request exceeding that limit. For finer-grained control, consider using your model provider's token consumption monitoring and limiting features.
This is not currently published to pypi so must be installed from source, and does not provide direct support for reaching out to generative models.  If you have a model output to evaluate chances are good you already have a method to generate that output, so the goal here is to make something light that can fit into that ecosystem.

#### Evaluation Flow
 
The evaluation process follows a three-step pipeline for each row of input data, initiated by Evaluator.run_dataset:
 
1. `prompt = prep_fn(row)` – generates a message array from the input
2. `raw_output = completion_fn(model, prompt)` – gets model response
3. `parsed, usage = post_process_fn(raw_output)` – parses the model output
 
```text
DataFrame --> prep_fn --> completion_fn --> post_process_fn --> parsed results
```
 
> Tip: If `log_enabled` is set, all raw outputs are saved to disk with timestamps under `evaluation_logs/`.
