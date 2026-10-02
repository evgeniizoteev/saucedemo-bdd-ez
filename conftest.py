import logging
from pathlib import Path

import pytest
from playwright.sync_api import Page

from data.users import get_user
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def logged_in(login_page: LoginPage, inventory_page: InventoryPage) -> InventoryPage:
    login_page.open()
    login_page.login(*get_user("standard"))
    return inventory_page


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
    request, feature, scenario, step, step_func, step_func_args, exception
):
    bdd_logger.error(
        "STEP FAILED | function=%s | error=%s",
        step_func.__name__,
        type(exception).__name__,
    )
