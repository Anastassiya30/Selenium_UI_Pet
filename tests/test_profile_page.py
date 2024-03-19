import time

import pytest

from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login


def test_go_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(3)
    page.pet_edit_button()
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")


@pytest.mark.delete
@pytest.mark.win10
def test_go_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(3)
    page.pet_delete_button()
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")


def test_go_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(3)
    page.pet_delete_button()
    page.pet_delete_no_button()
    time.sleep(5)
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")


@pytest.mark.delete
def test_go_profile_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    time.sleep(3)
    page.pet_delete_button()
    page.pet_delete_yes_button()
    time.sleep(5)
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")
