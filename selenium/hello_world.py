import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service('./chromedriver/chromedriver.exe'))
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_hello_world(self):
        driver = self.driver
        driver.get("http://pandapanel.org")
    
    def test_pandapanel_admin(self):
        driver = self.driver
        driver.get("http://pandapanel.org/admin")


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    
if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="", report_name="Hello_world_test"))