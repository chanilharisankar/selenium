class SeleniumUtils:
    def __init__(self,driver):
        self.driver=driver
    def find_element(cls,css_path):
        if cls.is_visible(css_path):
            element = cls.driver.find_element_by_css_selector(css_path)
        else:
            raise Exception("Element with css path :::: {0}  :: is not visible")

        return element
