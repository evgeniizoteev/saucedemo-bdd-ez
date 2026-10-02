Feature: Login
  Users can access the inventory with valid credentials.

  Scenario: Standard user reaches inventory
    Given the login page is open
    When the standard user logs in
    Then the inventory page is displayed