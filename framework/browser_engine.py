# -*- coding:utf-8 -*-

import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger


logger = Logger(logger='BrowserEngine').get_log()


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'

    def __init__(self, driver):
        self.driver = driver

    # 读取浏览器的配置文件，选择driver
    def open_browser(self, driver):
        # 读取配置文件
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        #获取配置文件属性
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser" % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
            logger.info("Starting Chrome browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the currect windows.")
        driver.implicitly_wait(5)
        logger.info("Set implicitly wait 5 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, close and quit the browser.")
        self.driver.quit()