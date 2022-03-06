from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from login_test import LoginTest

login_test = TestLoader().loadTestsFromTestCase(LoginTest)

suit_test = TestSuite([login_test])

kwargs = {
    "output": 'suit_report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(suit_test)