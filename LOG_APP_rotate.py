import time
import logging
import logging.handlers


def log_setup():
    log_handler = logging.handlers.WatchedFileHandler("LOG_APP.log")
    formatter = logging.Formatter(
        "%(asctime)s program_name [%(process)d]: %(message)s", "%b %d %H:%M:%S"
    )
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)


log_setup()
logging.info("Hello, World!")
import os

os.rename("LOG_APP.log", "LOG_APP.log-old")
logging.info("Hello, New World!")
