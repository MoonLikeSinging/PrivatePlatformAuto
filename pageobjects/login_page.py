from framework.base_page import BasePage


class LoginPage(BasePage):

    email = "id=>email"
    password = "id=>password"
    sign_button = "class_name=>btn-primary"

    def input_email(self, text):
        self.type(self.email, text)

    def input_pwd(self, text):
        self.type(self.password, text)

    def sign_in(self):
        self.click(self.sign_button)
