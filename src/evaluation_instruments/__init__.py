from .model import TokenUsage
from ._evaluation import Evaluation
import logging

logging.basicConfig()
logger = logging.getLogger('evaluation')

# Configure logger for evaluation
def set_logging(level):
    logger.setLevel(level)
