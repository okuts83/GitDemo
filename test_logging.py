import logging


# create an object for logging

def test_loggingDemo():

    logger = logging.getLogger(__name__) # (__name__) - to capture test case name in logs

    fileHandler = logging.FileHandler("logfile.log") # file location and name
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") # how our logs will be displayed

# we need to connect formatter and fileHandler to pass format to fileHandler
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) # fileHandler object >>> where file for logging is located and format of logging

# we need to set error level, if we set error >>> will display error and next critical
    logger.setLevel(logging.INFO)


# Level of errors
    logger.debug("A debug statement is execute")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")
    logger.critical("Critical issue")




