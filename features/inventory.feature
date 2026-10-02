Feature: Inventory
  Users can add products to the shopping cart.

  Scenario: Add backpack to cart
    Given the standard user is on the inventory page
    When the user adds "Sauce Labs Backpack" to the cart
    Then the cart badge shows "1"
    When the user opens the cart
    Then the cart contains "Sauce Labs Backpack"