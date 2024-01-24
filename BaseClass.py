import inspect
import logging

class BaseClass: # parent class

    def getlogger(self):
        loggerName = inspect.stack()[1][3] # to add Test case name to logs description
        logger = logging.getLogger(loggerName)  # (logger) = (__name__) - to capture test case name in logs

        fileHandler = logging.FileHandler("logfile.log")  # file location and name
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # how our logs will be displayed

        # we need to connect formatter and fileHandler to pass format to fileHandler
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # fileHandler object >>> where file for logging is located and format of logging

        # we need to set error level, if we set error >>> will display error and next critical
        logger.setLevel(logging.DEBUG) # input level og logs DEBUG, INFO, CRITICAL...
        return logger

        # Level of errors
        logger.debug("A debug statement is execute")
        logger.info("Information statement")
        logger.warning("Something is in warning mode")
        logger.error("A Major error has happend")
        logger.critical("Critical issue")

