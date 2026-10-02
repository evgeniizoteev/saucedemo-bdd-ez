Feature: Data-driven login
    Login behavior depends on the user and supplied credentials.

  Scenario Outline: Reject invalid credentials
    Given the login form is open for data-driven testing
    When the user submits username "<username>" and password "<password>"
    Then the login error contains "<error>"
    And the login form remains displayed

    Examples:
      | username      | password     | error                                                                     |
      | invalid_user  | secret_sauce | Username and password do not match any user in this service                |
      | standard_user | wrong_pass   | Username and password do not match any user in this service                |
      |               | secret_sauce | Username is required                                                      |
      | standard_user |              | Password is required                                                      |
      |               |              | Username is required                                                      |

        Scenario Outline: Allowed users reach inventory
    Given the login form is open for data-driven testing
    When the "<role>" user logs in with valid credentials
    Then the data-driven inventory page is displayed

    Examples:
      | role               |
      | standard           |
      | problem            |
      | performance_glitch |
      | error              |
      | visual             |