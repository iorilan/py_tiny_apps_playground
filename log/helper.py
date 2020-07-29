import logging, logging.handlers as handlers

"""
    S : seconds
    M : minutes
    H: hours
    D: day
    W0-W6: Weekday
    midnight
"""

def logger_daily():
    return __get_logger(logging.INFO, 'D')
def logger_midnight():
    return __get_logger(logging.INFO, 'midnight')
def logger_minute():
    return __get_logger(logging.INFO, 'M')
def logger_hour():
    return __get_logger(logging.INFO, 'M')
def __get_time_logger(default_level = logging.INFO, when='D'):
    logger = logging.getLogger("log_app")
    logger.setLevel(default_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = handlers.TimedRotatingFileHandler("log_folder/ts_app.log", when=when, interval=1, backupCount=1)
    handler.setLevel(default_level)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


"""
    debug : time based rotating ,every minute one file,0 backup
    info : time based ,every hour one file, 1 backup
    error : size based, 1k one file, 2 backup
"""
def logger_default(level=logging.DEBUG):
    logger = logging.getLogger('my_log_default')
    logger.setLevel(level=level)

    formatter1 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter2 = logging.Formatter('%(asctime)s - %(message)s')

    handler_debug = handlers.TimedRotatingFileHandler('log_folder/debug.log', when='M', interval=1, backupCount=0)
    handler_debug.setLevel(logging.DEBUG)
    handler_debug.setFormatter(formatter1)

    handler_info = handlers.TimedRotatingFileHandler('log_folder/info.log', when='H', interval=1, backupCount=1)
    handler_info.setLevel(logging.INFO)
    handler_info.setFormatter(formatter1)

    handler_error = handlers.RotatingFileHandler('log_folder/error.log', maxBytes=1000, backupCount=2)
    handler_error.setLevel(logging.ERROR)
    handler_error.setFormatter(formatter2)

    logger.addHandler(handler_debug)
    logger.addHandler(handler_info)
    logger.addHandler(handler_error)

    return logger


def logger_of_size(max_byte=1000):
    logger = logging.getLogger("log_app")
    logger.setLevel(default_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = handlers.TimedRotatingFileHandler("log_folder/size_app.log", maxBytes=max_byte, backupCount=1)
    handler.setLevel(default_level)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger