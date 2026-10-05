from playwright.sync_api import expect
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("../features/inventory_data_driven.feature")


@given("a standard user is on the inventory page")
def verify_inventory_page(logged_in):
    expect(logged_in.page_title).to_have_text("Products")


@when(parsers.parse('the user adds the selected product "{product_name}"'))
def add_selected_product(inventory_page, product_name):
    inventory_page.add_to_cart(product_name)


@then(parsers.parse('the shopping cart badge shows "{count}"'))
def verify_cart_count(inventory_page, count):
    expect(inventory_page.cart_badge).to_have_text(count)


@when("the user navigates to the shopping cart")
def navigate_to_cart(cart_page):
    cart_page.open_cart()


@then(parsers.parse('the selected product "{product_name}" is in the cart'))
def verify_selected_product(inventory_page, product_name):
    expect(inventory_page.page).to_have_url("/cart.html")
    expect(inventory_page.item_names.filter(has_text=product_name)).to_have_text(
        product_name
    )


@then(parsers.parse("the cart contains {count:d} products"))
def verify_cart_product_count(cart_page, count):
    expect(cart_page.item_names).to_have_count(count)
