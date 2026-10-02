from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenario, then, when


@scenario("../features/inventory.feature", "Add backpack to cart")
def test_add_backpack_to_cart_bdd():
    pass


@given("the standard user is on the inventory page")
def verify_inventory_page(logged_in):
    expect(logged_in.page_title).to_have_text("Products")


@when(parsers.parse('the user adds "{product_name}" to the cart'))
def add_product_to_cart(inventory_page, product_name):
    inventory_page.add_to_cart(product_name)


@then(parsers.parse('the cart badge shows "{count}"'))
def verify_cart_badge(inventory_page, count):
    expect(inventory_page.cart_badge).to_have_text(count)


@when("the user opens the cart")
def open_cart(inventory_page):
    inventory_page.open_cart()


@then(parsers.parse('the cart contains "{product_name}"'))
def verify_product_in_cart(inventory_page, product_name):
    expect(inventory_page.page).to_have_url("/cart.html")
    expect(
        inventory_page.item_names.filter(has_text=product_name)
    ).to_have_text(product_name)