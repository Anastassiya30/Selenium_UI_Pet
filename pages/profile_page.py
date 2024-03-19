from .base_page import BasePage
from .locators import ProfilePageLocators
import time


class ProfilePage(BasePage):

    def pet_edit_button(self):
        edit_button = self.browser.find_element(*ProfilePageLocators.EDIT_BUTTON)
        edit_button.click()

    def pet_delete_button(self):
        delete_button = self.browser.find_element(*ProfilePageLocators.DELETE_BUTTON)
        delete_button.click()

    def pet_delete_yes_button(self):
        delete_yes = self.browser.find_element(*ProfilePageLocators.DELETE_YES)
        delete_yes.click()

    def pet_delete_no_button(self):
        delete_no = self.browser.find_element(*ProfilePageLocators.DELETE_NO)
        delete_no.click()
