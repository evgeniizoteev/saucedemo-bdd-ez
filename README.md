# SauceDemo BDD — Lesson 12

Lesson 12 homework using Python, Playwright, pytest-bdd,
and the Page Object Model.

## Implemented BDD scenario

- Standard user logs in and reaches the inventory page.
- Locked out user sees an error and remains on the login page.
- Gherkin: features/login.feature
- Python step definitions: tests/test_login_bdd.py

The project also retains the pytest tests from Lesson 11.

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

## Run the BDD test

```bash
uv run pytest tests/test_login_bdd.py -v
```

## Verified result

Both BDD login tests passed locally in Chromium: 2 passed.

## Homework progress

Two BDD login scenarios implemented: successful and locked out login.
Additional BDD coverage and a framework for another practice
website are still pending.