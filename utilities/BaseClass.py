import os

import pytest
import inspect
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class CommonClass:



    def verifyLink(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogs(self):
        # To get the exact file path
        loggerName = inspect.stack()[1][3] # To get the name of the current calling function this is used
        logger = logging.getLogger(loggerName)  # like __dirName we use this to print test name
        # fileHandler = logging.FileHandler('logfile.log')
        fileHandler = logging.FileHandler(os.path.abspath(__file__)+"../../logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        # we can set levels to provide logs only for errors
        logger.setLevel(logging.DEBUG)

        return logger





