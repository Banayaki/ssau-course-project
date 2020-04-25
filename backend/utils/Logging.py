import logging
import sys


class Logging:
    loggers = {}

    @staticmethod
    def get_logger(class_name) -> logging.Logger:
        if Logging.loggers.get(class_name):
            return Logging.loggers.get(class_name)
        else:
            logging.basicConfig()
            logger = logging.getLogger(class_name)
            logger.setLevel(logging.DEBUG)

            fh = logging.StreamHandler(sys.stdout)
            fh.setFormatter(logging.Formatter('%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(fh)

            Logging.loggers[class_name] = logger

            return logger
