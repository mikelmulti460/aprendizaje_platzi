import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=Service('./chromedriver/chromedriver.exe'))
        driver = cls.driver
        driver.implicitly_wait(10)
    
    def test_access(self):
        driver = self.driver
        driver.get("http://pandapanel.com")
    
    def test_pandapanel_login(self):
        driver = self.driver
        driver.get("http://pandapanel.com")
        input_user = driver.find_element_by_id('id_username')
        input_user.send_keys('admin@centrofowardimport')
        input_password = driver.find_element_by_id('id_password')
        input_password.send_keys('olakase210804\n')
        #button = driver.find_element_by_css_selector("button.login100-form-btn")
        #button.click()
        driver.implicitly_wait(5)
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'fa-sign-out'))

    def test_invoices(self):
        driver = self.driver
        driver.get("http://centrofowardimport.pandapanel.com/billing/")
        

    def is_element_present(self, how, where):
        try:
            self.driver.find_element(by=how, value=where)
        except NoSuchElementException:
            return False
        return True

    def is_correct_current_url(self, link):
        current_url = self.driver.current_url
        if link==current_url:
            return True

        return False

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    
if __name__ == "__main__":
    unittest.main(verbosity=1, testRunner=HTMLTestRunner(output="reports", report_name="Login_Test"))