# -*- coding:utf-8 -*-

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

    def test_login_1_empty_email_pwd(self):
        logger.info("Test login without email and pwd.")
        login_page = LoginPage(self.driver)
        login_page.sleep(2)
        login_page.clear_email()
        login_page.clear_pwd()
        login_page.sleep(2)
        login_page.sign_in()
        try:
            self.assertEqual(u'请输入邮箱或手机号码', login_page.get_email_error())
            logger.info(u'未输入账号')
            self.assertEqual(u'请输入登录密码', login_page.get_pwd_error())
            logger.info(u'未输入密码')
        except Exception as e:
            logger.error(u'错误提示不正确，请检查页面是否更新: %s。' % format(e))

    def test_login_2_incorrect_account(self):
        logger.info(u'Test login with incorrect account.')
        login_page = LoginPage(self.driver)
        login_page.sleep(2)
        login_page.input_email('testfortest@test.com')
        login_page.sleep(2)
        login_page.input_pwd('kiwi888zx')
        login_page.sleep(2)
        login_page.sign_in()
        login_page.sleep(2)
        try:
            self.assertEqual(u'该账号不存在，请注册', login_page.get_tips_info())
            logger.info('账号未曾注册')
        except Exception as e:
            logger.error(u'错误提示不正确, 请检查页面是否更新：%s' % format(e))

    def test_login_3_incorrect_pwd(self):
        logger.info(u'Test login with incorrect password')
        login_page = LoginPage(self.driver)
        login_page.sleep(2)
        login_page.input_email('luyue@kiwisec.com')
        login_page.sleep(2)
        login_page.input_pwd('kiwitest')
        login_page.sleep(2)
        login_page.sign_in()
        login_page.sleep(2)
        try:
            self.assertEqual(u'用户名或者密码错误', login_page.get_tips_info())
            logger.info('用户名或者密码不正确')
        except Exception as e:
            logger.error(u'错误提示不正确，请检查页面是否更新：%s' % format(e))

    def test_login_4_pwd_length(self):
        logger.info(u'Test login with Insufficient password length')
        login_page = LoginPage(self.driver)
        login_page.sleep(2)
        login_page.input_email('luyue@kiwisec.com')
        login_page.sleep(2)
        login_page.input_pwd('ki')
        login_page.sleep(2)
        login_page.sign_in()
        login_page.sleep(2)
        try:
            self.assertEqual(u'密码长度至少为6位', login_page.get_pwd_error())
            logger.info(u"密码长度不够6位")
        except Exception as e:
            logger.error(u'错误提示不正确，请检查页面是否更新：%s' % format(e))

    def test_login_5_correct_account(self):
        login_page = LoginPage(self.driver)
        login_page.sleep(2)
        login_page.input_email('luyue@kiwisec.com')
        login_page.sleep(2)
        login_page.input_pwd('kiwi888zx')
        login_page.sleep(2)
        login_page.sign_in()
        login_page.sleep(5)
        try:
            self.assertIn(u"移动应用安全平台", login_page.get_page_title())
            logger.info('sign in successfully')
        except Exception as e:
            logger.error('sign in failed, %s' % format(e))


if __name__ == '__main__':
    unittest.main()
