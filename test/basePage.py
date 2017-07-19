from .periscopePage import PeriscopePage
class BasePage:
    def __init__(self,driver,url):
        self.URL=url
        self.drive=driver
    def nevigateToURL(self):
        self.drive.get(self.URL)
        return PeriscopePage(driver=self.drive)