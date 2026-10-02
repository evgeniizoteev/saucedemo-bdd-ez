from playwright.sync_api import expect
from pytest_bdd import parsers, scenario, then


@scenario("../features/inventory.feature", "Add backpack to cart")
def test_add_backpack_to_cart_bdd():
    pass


@scenario("../features/inventory.feature", "Catalog lists products")
def test_catalog_lists_products_bdd():
    pass


@then(parsers.parse('the cart badge shows "{count}"'))
def verify_cart_badge(inventory_page, count):
    expect(inventory_page.cart_badge).to_have_text(count)


@then(parsers.parse('the cart contains "{product_name}"'))
def verify_product_in_cart(inventory_page, product_name):
    expect(inventory_page.page).to_have_url("/cart.html")
    expect(inventory_page.item_names.filter(has_text=product_name)).to_have_text(
        product_name
    )


@then(parsers.parse("the catalog has {count:d} products"))
def verify_catalog_count(inventory_page, count):
    expect(inventory_page.item_names).to_have_count(count)


@then(parsers.parse('the catalog contains "{product_name}"'))
def verify_catalog_product(inventory_page, product_name):
    expect(inventory_page.item_names.filter(has_text=product_name)).to_have_text(
        product_name
    )
