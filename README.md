# Evaluation-Instruments

This repository contains a collection of evaluation instruments with a focus on AI use cases for healthcare. The instruments were developed to support both manual evaluation by trained evaluators and automated evaluation approaches such as deterministic statistical methods or probabilistic LLM-as-a-Judge. The instruments were initially calibrated to support specific use cases and should be reviewed prior to use if the planned use case differs. 

The instruments provide a consistent interface for inputs and outputs to aid in reuse between use cases, composition into pipelines, and integration with [seismometer](https://epic-open-source.github.io/seismometer/) for analysis. If an instrument requires an LLM, the [litellm SDK](https://docs.litellm.ai/) API protocol is encouraged to streamline usage across language models. 

## PDSQI-9
The [PDSQI-9 notebook](https://github.com/epic-open-source/evaluation-instruments/blob/main/instruments/pdsqi_9/PDSQI_annotated.ipynb) demonstrates how to use the evaluation instument on a set of notes and their pre-generated summaries.  Note that use of the instrument is under a [separate license](https://github.com/epic-open-source/evaluation-instruments/blob/main/instruments/pdsqi_9/LICENSE.txt) and of course give credit to the authors using the provided [citation details](https://github.com/epic-open-source/evaluation-instruments/blob/main/instruments/pdsqi_9/CITATION.cff).
