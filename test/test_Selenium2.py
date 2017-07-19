import time,os,sys,pytest

from .fixture import Fixture
from selenium import webdriver

class Test_Selenium2(Fixture):

    @classmethod
    def setup_class(cls):
        super(Test_Selenium2,cls).setup_class()
        cls.periscopePage=cls.basePage.nevigateToURL()
        print("inside setup testcase file")

    # @classmethod
    # def teardown_class(cls):
    #     print("closing..")


    # @pytest.mark.skip
    def test_Test_Selenium2_T1(self):
        print('T1')
        periscope=self.periscopePage.getText()
        print(periscope)
        assert 1==1