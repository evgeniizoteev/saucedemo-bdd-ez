# SauceDemo BDD — Lesson 12

Lesson 12 homework using Python, Playwright, pytest-bdd,
and the Page Object Model.

## Implemented BDD scenario

- Standard user logs in and reaches the inventory page.
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

The BDD login test passed locally in Chromium: 1 passed.

## Homework progress

Initial BDD scenario implemented.
Additional BDD scenarios and a framework for another practice
website are still pending.