from logger import logger

class stdout_logger(logger):


    """
    Constructor
    """
    def __init__(self, log_level):
        logger.__init__(self, log_level)


    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold.
    """
    def log(self, log_level, message):
        if self.should_log(log_level):
            print("%d: %s" % (log_level, message))
