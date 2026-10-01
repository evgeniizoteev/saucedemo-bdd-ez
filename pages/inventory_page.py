from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.item_names = page.locator("[data-test='inventory-item-name']")

    def product_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def add_to_cart(self, product_name: str) -> None:
        slug = product_name.lower().replace(" ", "-")
        self.click(self.page.locator(f"[data-test='add-to-cart-{slug}']"))
