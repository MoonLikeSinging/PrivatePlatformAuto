# -*- coding:utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.detection_page import DetectionPage
from testsuites.test_login_page import TestLoginPage

logger = Logger(logger='test_detection_page').get_log()


class TestDetectionPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        test_login_page = TestLoginPage()
        TestLoginPage.test_login_5_correct_account(test_login_page)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_upload_app(self):
        logger.info("Upload app")
        detection_page = DetectionPage(self.driver)
        detection_page.select_detection_report()
        detection_page.sleep(2)
        detection_page.click_to_upload()


if __name__ == '__main__':
    unittest.main()
