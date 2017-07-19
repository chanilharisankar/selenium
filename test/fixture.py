import time,os,sys,pytest

from selenium import webdriver
from .basePage import BasePage
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Fixture:
    @classmethod
    def setup_class(cls):
        type="LOCALlq"
        cls.URL="https://www.periscope-solutions.com/"
        chromedriver="/MyFiles/work/workspace/python/selenium/resources/chromedriver"
        os.environ["PATH"] += os.pathsep + "resources"
        # os.environ["PATH"] ="/MyFiles/work/workspace/python/selenium/resources/chromedriver"
        if(type=="LOCAL"):
            cls.driver=webdriver.Chrome(chromedriver)
        else:

            # capability = webdriver.DesiredCapabilities.CHROME
            cls.browser = webdriver.Remote(command_executor="http://localhost:4545/wd/hub/",
                                           desired_capabilities={'browserName': 'chrome'})

        # cls.driver.maximize_window()
        cls.basePage=BasePage(cls.driver,cls.URL)

    @classmethod
    def teardown_class(cls):
        print("closcling tab")
        cls.driver.close()
