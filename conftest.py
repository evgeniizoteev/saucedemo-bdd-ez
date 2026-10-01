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
