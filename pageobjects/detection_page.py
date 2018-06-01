# -*- coding:utf-8 -*-

from framework.base_page import BasePage


class DetectionPage(BasePage):
    menu_detection_report = "id=>menu-detection-report"
    add_android_app = "class_names=>btn-fileupload"

    def select_detection_report(self):
        self.click(self.menu_detection_report)

    def click_to_upload(self):
        self.click(self.add_android_app[0])
