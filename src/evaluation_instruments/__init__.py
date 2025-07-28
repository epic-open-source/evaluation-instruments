import logging

from ._evaluation import Evaluation
from .model import TokenUsage
from .post import frame_from_evals
from .prep import OutputMode

logging.basicConfig()
logger = logging.getLogger("evaluation")


# Configure logger for evaluation
def set_logging(level):
    logger.setLevel(level)
