
from .base_page import BasePage
from .locators import RegisterPageLocators


class RegisterPage(BasePage):

    def go_to_email(self):
        register_email = self.browser.find_element(*RegisterPageLocators.REGISTER_EMAIL)
        register_email.send_keys('lala@mail.com')

    def go_to_password(self):
        input_password = self.browser.find_element(*RegisterPageLocators.REGISTER_PASSWORD)
        input_password.send_keys('1111')

    def confirm_password(self):
        input_password = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        input_password.send_keys('1111')

    def go_to_submit_button(self):
        submit_button = self.browser.find_element(*RegisterPageLocators.REGISTER_SUBMIT_BUTTON)
        submit_button.submit()
