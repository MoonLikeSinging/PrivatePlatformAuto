# -*- coding:utf-8 -*-

import unittest
from framework.browser_engine import BrowserEngine
from framework.logger import Logger
from pageobjects.detection_page import DetectionPage


logger = Logger(logger='test_detection_page').get_log()


class TestDetectionPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        cls.driver.implicitly_wait(10)
        detection_page = DetectionPage(cls.driver)
        detection_page.sleep(2)
        detection_page.input_email('luyue@kiwisec.com')
        detection_page.sleep(2)
        detection_page.input_pwd('kiwi888zx')
        detection_page.sleep(2)
        detection_page.sign_in()
        detection_page.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        logger.info('over')

    def test_upload_app(self):
        logger.info("Upload app")
        detection_page = DetectionPage(self.driver)
        detection_page.select_detection_report()
        detection_page.sleep(5)
        detection_page_new = DetectionPage(self.driver)
        detection_page_new.click_to_upload()
        detection_page_new.sleep(5)


if __name__ == '__main__':
    unittest.main()
