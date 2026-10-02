# SauceDemo BDD — Lessons 12–13

Practice framework using Python, Playwright, pytest-bdd
and the Page Object Model.

## Implemented scenarios

- Successful login reaches the inventory page.
- Locked out login shows an error and stays on the login page.
- Backpack is added to the cart and verified.
- Scenario Outline checks two products: Backpack and Bike Light.

The project also retains the pytest tests from Lesson 11.

## Structure

- features/ — Gherkin scenarios and Examples tables
- tests/ — pytest tests and BDD step definitions
- pages/ — Page Objects
- conftest.py — fixtures and logging hooks

## Setup

Install uv, then run:

```bash
uv sync
uv run playwright install chromium
```

Create a local .env file in the project root:

```text
STANDARD_USER=<username>/<password>
LOCKED_OUT_USER=<username>/<password>
```

Use the demo credentials displayed on https://www.saucedemo.com.
The .env file is excluded from Git.

## Run all BDD tests

```bash
uv run pytest tests/test_login_bdd.py tests/test_inventory_bdd.py tests/test_inventory_data_driven.py -v
```

## Logging

Hooks log scenario start/end, step start/success and step errors.
Output: logs/bdd_run.log.

Step argument values and passwords are not logged.
Generated logs are excluded from Git.

## Verified result

5 BDD test cases passed together locally in Chromium.
Scenario and step logging was verified.

## Additional practice project

https://github.com/evgeniizoteev/the-internet-bdd-ez

Two login scenarios passed together in that project.