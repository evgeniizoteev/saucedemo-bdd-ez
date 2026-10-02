Feature: Login
  Users can access the inventory with valid credentials.

  Scenario: Standard user reaches inventory
    Given the login page is open
    When the standard user logs in
    Then the inventory page is displayed

  Scenario: Locked out user cannot log in
    Given the login page is open
    When the locked out user logs in
    Then a locked out error is displayed
    And the user remains on the login page