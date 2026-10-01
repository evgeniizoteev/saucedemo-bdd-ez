from playwright.sync_api import Locator, Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.page_title = page.locator("[data-test='title']")

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def open(self, path: str = "/") -> None:
        self.page.goto(path)

    def cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def open_cart(self) -> None:
        self.click(self.cart_link)
