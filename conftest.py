import logging
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, when

from data.users import get_user
from pages.cart_page import CartPage
from pages.checkout_page import (
    CheckoutCompletePage,
    CheckoutInfoPage,
    CheckoutOverviewPage,
)
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def logged_in(
    login_page: LoginPage,
    inventory_page: InventoryPage,
) -> InventoryPage:
    login_page.open()
    login_page.login(*get_user("standard"))
    return inventory_page


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_info_page(page: Page) -> CheckoutInfoPage:
    return CheckoutInfoPage(page)


@pytest.fixture
def checkout_overview_page(page: Page) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(page)


@pytest.fixture
def checkout_complete_page(page: Page) -> CheckoutCompletePage:
    return CheckoutCompletePage(page)


@given("the standard user is on the inventory page")
def verify_inventory_page(logged_in):
    expect(logged_in.page_title).to_have_text("Products")


@when(parsers.parse('the user adds "{product_name}" to the cart'))
def add_product_to_cart(inventory_page, product_name):
    inventory_page.add_to_cart(product_name)


@when("the user opens the cart")
def open_cart(inventory_page):
    inventory_page.open_cart()


bdd_logger = logging.getLogger("saucedemo.bdd")


def pytest_configure(config):
    log_dir = Path(__file__).resolve().parent / "logs"
    log_dir.mkdir(exist_ok=True)

    handler = logging.FileHandler(
        log_dir / "bdd_run.log",
        mode="w",
        encoding="utf-8",
    )
    handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
    bdd_logger.setLevel(logging.INFO)
    bdd_logger.propagate = False
    bdd_logger.addHandler(handler)


def pytest_unconfigure(config):
    for handler in list(bdd_logger.handlers):
        handler.close()
        bdd_logger.removeHandler(handler)


def pytest_bdd_before_scenario(request, feature, scenario):
    bdd_logger.info(
        "SCENARIO START | feature=%s | test=%s",
        feature.name,
        request.node.name,
    )


def pytest_bdd_after_scenario(request, feature, scenario):
    bdd_logger.info("SCENARIO END | test=%s", request.node.name)


def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    bdd_logger.info(
        "STEP START | type=%s | function=%s",
        step.type,
        step_func.__name__,
    )


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    bdd_logger.info("STEP PASSED | function=%s", step_func.__name__)


def pytest_bdd_step_error(
    request,
    feature,
    scenario,
    step,
    step_func,
    step_func_args,
    exception,
):
    bdd_logger.error(
        "STEP FAILED | function=%s | error=%s",
        step_func.__name__,
        type(exception).__name__,
    )
