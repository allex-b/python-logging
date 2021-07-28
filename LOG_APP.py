import logging


def get_logger(name=None, level=None, handler=None, formatter=None):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)
    if level:
        logger.setLevel(logging.DEBUG)

    log_handler = logging.FileHandler("LOG_%s.log" % name)
    if handler:
        log_handler = logging.StreamHandler()

    log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    if formatter:
        log_format = formatter
    log_handler.setFormatter(logging.Formatter(log_format))

    logger.addHandler(log_handler)

    return logger


def main():
    logger = get_logger(__name__, None, None, None)

    # Сообщение информационное
    logger.info("This is an info message")
    # Сообщение отладочное
    logger.debug("This is a debug message")


if __name__ == "__main__":
    main()
