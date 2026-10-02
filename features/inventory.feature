Feature: Inventory
  Users can view products and add them to the shopping cart.

  Background:
    Given the standard user is on the inventory page

  Scenario: Catalog lists products
    Then the catalog has 6 products
    And the catalog contains "Sauce Labs Backpack"

  Scenario: Add backpack to cart
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge shows "1"
    When the user opens the cart
    Then the cart contains "Sauce Labs Backpack"