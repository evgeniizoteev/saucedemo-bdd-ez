Feature: Data-driven inventory
  Users can add different products to the cart.

  Scenario Outline: Add a selected product to the cart
    Given a standard user is on the inventory page
    When the user adds the selected product "<product_name>"
    Then the shopping cart badge shows "1"
    When the user navigates to the shopping cart
    Then the selected product "<product_name>" is in the cart

    Examples:
      | product_name             |
      | Sauce Labs Backpack      |
      | Sauce Labs Bike Light    |
      | Sauce Labs Bolt T-Shirt  |

  Scenario: Add two different products to the cart
    Given a standard user is on the inventory page
    When the user adds the selected product "Sauce Labs Backpack"
    And the user adds the selected product "Sauce Labs Bike Light"
    Then the shopping cart badge shows "2"
    When the user navigates to the shopping cart
    Then the cart contains 2 products
    And the selected product "Sauce Labs Backpack" is in the cart
    And the selected product "Sauce Labs Bike Light" is in the cart

  Scenario: Add and remove a product from the cart
    Given a standard user is on the inventory page
    When the user adds the selected product "Sauce Labs Backpack"
    Then the shopping cart badge shows "1"
    When the user navigates to the shopping cart
    Then the cart contains 1 products
    When the user removes the selected product "Sauce Labs Backpack"
    Then the cart contains 0 products
