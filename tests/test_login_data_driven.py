from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when
from data.users import get_user

scenarios("../features/login_data_driven.feature")


@given("the login form is open for data-driven testing")
def open_login_form(login_page):
    login_page.open()


@when(
    parsers.re(
        r'the user submits username "(?P<username>[^"]*)" '
        r'and password "(?P<password>[^"]*)"'
    )
)
def submit_credentials(login_page, username, password):
    login_page.login(username, password)


@then(parsers.parse('the login error contains "{error}"'))
def verify_login_error(login_page, error):
    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text(error)


@then("the login form remains displayed")
def verify_login_form(login_page):
    expect(login_page.page).to_have_url("/")
    expect(login_page.login_button).to_be_visible()


@when(parsers.parse('the "{role}" user logs in with valid credentials'))
def log_in_with_valid_credentials(login_page, role):
    login_page.login(*get_user(role))


@then("the data-driven inventory page is displayed")
def verify_data_driven_inventory(inventory_page):
    expect(inventory_page.page).to_have_url(
        "/inventory.html",
        timeout=15_000,
    )
    expect(inventory_page.page_title).to_have_text(
        "Products",
        timeout=15_000,
    )
