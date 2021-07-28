import LOG_APP

logger = LOG_APP.get_logger(__name__)


def process(msg):
    logger.info("Перед процессом")
    print(msg)
    logger.info("После процесса")
