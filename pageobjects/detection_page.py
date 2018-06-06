# -*- coding:utf-8 -*-

from framework.base_page import BasePage


class DetectionPage(BasePage):

    email = "id=>email"
    password = "id=>password"
    sign_button = "class_name=>btn-primary"
    menu_detection_report = "id=>menu-detection-report"
    add_android_app = "class_name=>btn-fileupload"

    def input_email(self, text):
        self.type(self.email, text)

    def input_pwd(self, text):
        self.type(self.password, text)

    def sign_in(self):
        self.click(self.sign_button)

    def select_detection_report(self):
        self.click(self.menu_detection_report)

    def click_to_upload(self):
        self.click(self.add_android_app)

