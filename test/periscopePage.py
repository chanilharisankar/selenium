from .seleniumUtils import SeleniumUtils

class PeriscopePage:
    def __init__(self,driver):
        self.__HOME__=".pageHeaderCopy>h1"
        self.driver=driver
        self.seleniumUtils=SeleniumUtils(self.driver)
    def getText(self):
        return self.seleniumUtils.driver.find_element_by_css_selector(self.__HOME__).text



