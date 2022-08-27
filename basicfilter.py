import logging
import getpass


class NoBadWordsFilter(logging.Filter):
    """Custom Filter to NOT log a message"""

    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().__contains__("f")


# class UserFilter(logging.Filter):
#     def filter(self, record: logging.LogRecord) -> bool:
#         setattr(record, "user", getpass.getuser())
#         return True


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.addFilter(NoBadWordsFilter())

logger.info("this log works")
logger.info("f me")
