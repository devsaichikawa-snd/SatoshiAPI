from functools import wraps
import logging
import logging.config
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

logging.config.fileConfig(os.path.join(BASE_DIR, "logging.conf"))
logger = logging.getLogger("root")


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            logger.info(f"View {func.__name__} executed successfully.")
            return response

        except Exception as e:
            logger.error(f"ERROR {func.__name__}: {e}", exc_info=True)
            raise

    return wrapper
