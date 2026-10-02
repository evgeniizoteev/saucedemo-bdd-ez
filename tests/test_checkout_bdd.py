from playwright.sync_api import expect
from pytest_bdd import parsers, scenario, then, when

from helpers.customer import get_customer


@scenario(
    "../features/checkout.feature",
    "Complete an order with a backpack",
)
def test_complete_order_with_backpack_bdd():
    pass


@then(parsers.parse('the checkout cart contains "{product_name}"'))
def verify_checkout_cart(cart_page, product_name):
    expect(cart_page.page).to_have_url("/cart.html")
    expect(cart_page.page_title).to_have_text("Your Cart")
    expect(cart_page.item_names).to_have_text([product_name])


@when("the user starts checkout")
def start_checkout(cart_page):
    cart_page.checkout()


@then("the checkout information page is displayed")
def verify_checkout_information_page(checkout_info_page):
    expect(checkout_info_page.page).to_have_url("/checkout-step-one.html")
    expect(checkout_info_page.first_name).to_be_visible()


@when("the user enters generated customer information")
def enter_customer_information(checkout_info_page):
    customer = get_customer()
    checkout_info_page.fill_info(
        customer["first_name"],
        customer["last_name"],
        customer["postal_code"],
    )


@then(parsers.parse('the checkout overview contains "{product_name}"'))
def verify_checkout_overview(checkout_overview_page, product_name):
    expect(checkout_overview_page.page).to_have_url("/checkout-step-two.html")
    expect(checkout_overview_page.page_title).to_have_text("Checkout: Overview")
    expect(checkout_overview_page.item_names).to_have_text([product_name])


@then(parsers.parse('the order total is "{expected_total}"'))
def verify_order_total(checkout_overview_page, expected_total):
    expect(checkout_overview_page.total).to_have_text(expected_total)


@when("the user finishes checkout")
def finish_checkout(checkout_overview_page):
    checkout_overview_page.finish()


@then("the order confirmation is displayed")
def verify_order_confirmation(checkout_complete_page):
    expect(checkout_complete_page.page).to_have_url("/checkout-complete.html")
    expect(checkout_complete_page.header).to_have_text("Thank you for your order!")
