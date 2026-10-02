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