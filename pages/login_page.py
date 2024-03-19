from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('anastguv@mail.com')

    def go_to_password(self):
        input_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        input_password.send_keys('anastguv1234')

    def go_to_button(self):
        submit_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.submit()
