# -*- coding:utf-8 -*-
from framework.base_page import BasePage


class LoginPage(BasePage):

    email = "id=>email"
    password = "id=>password"
    sign_button = "class_name=>btn-primary"
    email_error = "id=>email-error"
    password_error = "id=>password-error"
    tips_info = 'xpath=>//*[@id="tips-info"]/span'

    def input_email(self, text):
        self.type(self.email, text)

    def input_pwd(self, text):
        self.type(self.password, text)

    def sign_in(self):
        self.click(self.sign_button)

    def clear_email(self):
        self.clear(self.email)

    def clear_pwd(self):
        self.clear(self.password)

    def get_email_error(self):
        return self.find_element(self.email_error).text

    def get_pwd_error(self):
        return self.find_element(self.password_error).text

    def get_tips_info(self):
        return self.find_element(self.tips_info).text
