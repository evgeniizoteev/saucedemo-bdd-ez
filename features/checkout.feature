Feature: Checkout
  Users can complete an order with a product in the cart.

  Background:
    Given the standard user is on the inventory page

  @smoke
  Scenario: Complete an order with a backpack
    When the user adds "Sauce Labs Backpack" to the cart
    And the user opens the cart
    Then the checkout cart contains "Sauce Labs Backpack"
    When the user starts checkout
    Then the checkout information page is displayed
    When the user enters generated customer information
    Then the checkout overview contains "Sauce Labs Backpack"
    And the order total is "Total: $32.39"
    When the user finishes checkout
    Then the order confirmation is displayed