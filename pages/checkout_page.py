from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutInfoPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.postal_code, postal_code)
        self.click(self.continue_button)


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.item_names = page.locator("[data-test='inventory-item-name']")
        self.total = page.locator("[data-test='total-label']")
        self.finish_button = page.locator("[data-test='finish']")

    def finish(self) -> None:
        self.click(self.finish_button)


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header = page.locator("[data-test='complete-header']")
