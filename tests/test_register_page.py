import time

import pytest

from pages.register_page import RegisterPage


@pytest.mark.parametrize('link', ['http://34.141.58.52:8080/#/register', 'http://34.141.58.52:8080/#/eno'])
def test_go_to_email(browser, link):
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_password()
    page.confirm_password()
    page.go_to_submit_button()
    time.sleep(3)
    browser.save_screenshot(r'C:\Users\Anast\PycharmProjects\Selenium_UI_Pet\result5.png')
