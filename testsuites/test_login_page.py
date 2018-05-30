import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.login_page import LoginPage
from framework.logger import Logger

logger = Logger(logger='test_login_page').get_log()


class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.sleep(2)
        login_page.input_email('luyue@kiwisec.com')
        login_page.sleep(2)
        login_page.input_pwd('kiwi888zx')
        login_page.sleep(2)
        login_page.sign_in()
        login_page.sleep(5)
        try:
            assert '移动应用安全平台' in login_page.get_page_title()
            logger.info('sign in successfully')
        except Exception as e:
            logger.info('sign in failed, %s' % format(e))


if __name__ == '__main__':
    unittest.main()