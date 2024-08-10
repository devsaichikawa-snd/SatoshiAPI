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
        logger.info(f"START: {func.__name__}")
        try:
            response = func(*args, **kwargs)
            logger.info(f"View {func.__name__} executed successfully.")
            logger.warning(
                f"View {func.__name__} did not return HttpResponse."
            )
            logger.info(f"FINISH: {func.__name__}")
            return response

        except Exception as e:
            logger.error(f"エラー発生：{func.__name__}: {e}", exc_info=True)
            raise

    return wrapper
