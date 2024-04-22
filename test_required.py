import yaml
import logging
from testpage import OperationsHelpers

with open('datatest.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username = data["username"]
    password = data["password"]


def test_login_success(browser):
    logging.info("Test auth login Starting")
    auth_page = OperationsHelpers(browser)
    auth_page.go_to_site()
    auth_page.enter_login(username)
    auth_page.enter_pass(password)
    auth_page.click_login_button()
    assert auth_page.get_user_text() == f"Hello, {username}", "Failed test login success"
    auth_page.get_screenshot()


def test_about_page(browser):
    logging.info("Test About page Starting")
    about_page = OperationsHelpers(browser)
    about_page.click_about_button()
    assert about_page.get_about_text() == "About Page", "Failed test About page"
    about_page.get_screenshot()


def test_check_font_size_title(browser):
    logging.info("Test Check font in title window Starting")
    about_page = OperationsHelpers(browser)
    assert about_page.get_font() == "32px", f"Failed test: Expected - 32px, Actual - {about_page.get_font()}"
    about_page.get_screenshot()
