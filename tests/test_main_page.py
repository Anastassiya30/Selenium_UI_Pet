import time

import pytest

from pages.main_page import MainPage
from tests.test_login_page import test_go_to_login


def test_go_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    screenshot = browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")
    current_url = browser.current_url
    assert screenshot
    assert current_url == 'http://34.141.58.52:8080/#/login'


@pytest.mark.like
def test_go_main_page(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.pet_like_button()
    time.sleep(3)
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")


@pytest.mark.smoke
def test_go_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    time.sleep(5)
    page.button_paginator()
    time.sleep(7)

    browser.save_screenshot(r'C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png')


@pytest.mark.smoke
def test_filter_by_dog(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    time.sleep(6)
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")
    page.choose_a_dog()
    time.sleep(6)
    browser.save_screenshot(r'C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png')


@pytest.mark.regression
def test_go_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()

    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")


@pytest.mark.smoke
def test_go_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    time.sleep(5)
    page.details_of_pet()
    time.sleep(5)

    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")


# Здесь тест проходит, но информация о другом питомце приходит


def test_go_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.filter_by_name()
    browser.save_screenshot(r"C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png")
