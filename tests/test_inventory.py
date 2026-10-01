import allure
from playwright.sync_api import expect

from data.users import BACKPACK


@allure.feature("Inventory")
def test_verify_inventory_page(logged_in):
    expect(logged_in.page_title).to_contain_text("Products")
    assert BACKPACK in logged_in.product_names()


@allure.feature("Inventory")
def test_add_backpack_to_cart(logged_in):
    logged_in.add_to_cart(BACKPACK)
    assert logged_in.cart_count() == 1
