import LOG_APP_pack
import LOG_APP

logger = LOG_APP.get_logger(__name__)


def main():
    logger.info("Программа стартует")
    LOG_APP_pack.process(msg="сообщение")
    logger.warning("Cообщение должно появиться в консоли")
    logger.info("Программа завершила работу")


if __name__ == "__main__":
    main()
