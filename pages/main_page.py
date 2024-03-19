
from .locators import MainPageLocators

from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_by_type(self):
        filter_by = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_by.click()

    def choose_a_dog(self):
        dog = self.browser.find_element(*MainPageLocators.DOG)
        dog.click()

    def choose_a_cat(self):
        cat = self.browser.find_element(*MainPageLocators.CAT)
        cat.click()

    def choose_a_reptile(self):
        reptile = self.browser.find_element(*MainPageLocators.REPTILE)
        reptile.click()

    def choose_a_hamster(self):
        hamster = self.browser.find_element(*MainPageLocators.HAMSTER)
        hamster.click()

    def choose_a_parrot(self):
        parrot = self.browser.find_element(*MainPageLocators.PARROT)
        parrot.click()

    def filter_by_name(self):
        dog = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        dog.send_keys('tasya')

    def details_of_pet(self):
        details_button = self.browser.find_element(*MainPageLocators.DETAILS_OF_PET_BUTTON)
        details_button.click()

    def pet_like_button(self):
        like_button = self.browser.find_element(*MainPageLocators.PET_LIKE_BUTTON)
        like_button.click()

    def button_paginator(self):
        button_paginator = self.browser.find_element(*MainPageLocators.BUTTON_PAGINATOR)
        button_paginator.click()
