import json
from datetime import datetime
import os
import tempfile
import logging
from pathlib import Path

from evaluation_instruments.model import TokenUsage
logger = logging.getLogger('evaluation')

class Evaluation:

    def __init__(self,
                 prep_fn=None,
                 completion_fn=None,
                 post_process_fn=None,
                log_enabled=True,
                model_args: dict ={},
                max_tokens=10_000,
                ):
        self._prep_fn = prep_fn
        self._completion_fn = completion_fn
        self._post_fn = post_process_fn or self.post_process_default

        self._log_enabled = log_enabled
        self._model_args = model_args
        self.capacity = TokenUsage(None, None, max_tokens)

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

    def toggle_logging(self):
        return not self._log_enabled

    def run_dataset(self, df, model=None, capacity=None):
        tmp_file = None
        outputs={}
        accumulated_usage = TokenUsage(0,0,0)
        max_usage = capacity or self.capacity

        for sample in df.itertuples():
            sample_ix = sample.Index

            # Resolve prompt
            prompt = self._prep_fn(sample)

            # Delegate
            raw_output = self._completion_fn(model, prompt)

            response, usage = self._post_fn(raw_output)
            accumulated_usage += TokenUsage(**usage)

            tmp_file = self._dump_to_temp(sample_ix=sample_ix, raw_content=raw_output, tmp_file_path=tmp_file)
            outputs[sample_ix] = response

            logger.debug(f"{sample_ix}-Completed evaluation")

            #abort if beyond capacity
            if accumulated_usage > max_usage:
                logger.warning(f"Aborting run after {sample_ix}. Capacity exceeded: {accumulated_usage} > {max_usage}")
                break

        if tmp_file is not None:
            logger.info(f"Dumped raw content to {tmp_file}")

        return outputs, accumulated_usage

    def _dump_to_temp(self, sample_ix=None, raw_content=None, tmp_file_path=None):
        if not self._log_enabled:
            return None

        # Create a temporary directory
        if tmp_file_path is None:
            tmp_dir = Path(tempfile.gettempdir()) / "evaluation_logs"
            tmp_dir.mkdir(parents=True, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d-%H%M")  # Generate a timestamp in the format YYYYMMDD-hhmm
            tmp_file_path = os.path.join(tmp_dir, f"raw_content_{timestamp}.jsonl")

        # Append sample_ix and raw_content to the file
        with open(tmp_file_path, "a") as tmp_file:
            tmp_file.write(json.dumps({"sample_ix": sample_ix, "raw_content": raw_content}) + "\n")

        return tmp_file_path

    def post_process_default(self, openai_json):
        ix = 0 # assume N=1
        raw_content = openai_json['choices'][ix]['message']['content']
        try:
            # Assume no nesting {}
            response = json.loads(raw_content[raw_content.find('{'):raw_content.find('}')+1])
        except:
            response = {}

        usage = openai_json['usage']
        return response, usage

__all__ = ['Evaluation']
