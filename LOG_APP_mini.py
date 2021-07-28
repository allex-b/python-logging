import logging


def main():
    """
    The main entry point of the application
    """

    logging.basicConfig(
        format=u"%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s",
        filename=u"LOG_APP.log",
        level=logging.INFO,
    )  # level = logging.DEBUG)

    # Сообщение отладочное
    logging.debug(u"This is a debug message")
    # Сообщение информационное
    logging.info(u"This is an info message")
    # Сообщение предупреждение
    logging.warning(u"This is a warning")
    # Сообщение ошибки
    logging.error(u"This is an error message")
    # Сообщение критическое
    logging.critical(u"FATAL!!!")

    # Перехват исключений - метод getLogger
    log = logging.getLogger("ex")

    try:
        raise RuntimeError
    except RuntimeError:
        log.exception("Error!")


if __name__ == "__main__":
    main()
