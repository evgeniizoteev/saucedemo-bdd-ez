from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.checkout_button = page.locator("[data-test='checkout']")

    def checkout(self) -> None:
        self.click(self.checkout_button)

    def remove_product(self, product_name: str) -> None:
        slug = product_name.lower().replace(" ", "-")
        self.click(self.page.locator(f"[data-test='remove-{slug}']"))
