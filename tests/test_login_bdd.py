from playwright.sync_api import expect
from pytest_bdd import given, scenario, then, when

from data.users import get_user


@scenario("../features/login.feature", "Standard user reaches inventory")
def test_standard_user_reaches_inventory_bdd():
    pass


@given("the login page is open")
def open_login_page(login_page):
    login_page.open()


@when("the standard user logs in")
def log_in_as_standard_user(login_page):
    login_page.login(*get_user("standard"))


@then("the inventory page is displayed")
def verify_inventory_page(login_page):
    expect(login_page.page).to_have_url("/inventory.html")


@scenario("../features/login.feature", "Locked out user cannot log in")
def test_locked_out_user_cannot_log_in_bdd():
    pass


@when("the locked out user logs in")
def log_in_as_locked_out_user(login_page):
    login_page.login(*get_user("locked_out"))


@then("a locked out error is displayed")
def verify_locked_out_error(login_page):
    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text("locked out")


@then("the user remains on the login page")
def verify_login_page_url(login_page):
    expect(login_page.page).to_have_url("/")
    