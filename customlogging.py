import json
import logging
import getpass


class UserFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        setattr(record, "user", getpass.getuser())
        return True

class NoBadWordsFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return not record.getMessage().__contains__("f")


class CustomFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def formatMessage(self, record: logging.LogRecord) -> str:
        super().formatMessage(record)
        log_record = {
            "message": record.message,
            "level": record.levelname,
            "name": record.name,
            "pathName": record.pathname,
            "funcName": record.funcName,
            "lineNumber": record.lineno,
            "threadId": record.thread,
            "user": record.user
        }
        return json.dumps(log_record)

logging_config: dict = {
    "version": 1,
    "filters": {"user": {"()": lambda: UserFilter()}, "badwords": {"()": lambda: UserFilter()}},
    "formatters": {
        "myformatter": {
            "()": lambda: CustomFormatter(),
        },
    },
    "handlers": {
        "console": {
            "filters": ["user", "badwords"],
            "formatter": "myformatter",
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
        "propagate": False,

    },
    "loggers": {
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

if __name__ == "__main__":
    import logging.config

    logging.config.dictConfig(logging_config)

    logger = logging.getLogger(__name__)

    logger.info("this is a test")
    logger.error("this is a warning")
    logger.critical("this is a critical error")
