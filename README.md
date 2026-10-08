# SauceDemo BDD — Lessons 12–13 and Practice

Python test automation framework using Playwright, pytest, pytest-bdd,
Page Object Model, Faker, and Allure.

## Implemented coverage

- Successful login and locked-out user rejection.
- Product catalog: six products and the expected backpack.
- Adding a backpack to the cart and verifying its presence.
- Data-driven cart checks for Backpack, Bike Light, and Bolt T-Shirt.
- Adding two products and verifying their names and the cart count.
- Removing the only product and verifying an empty cart.
- Removing one of two products and verifying the remaining product.
- Data-driven login for five allowed users.
- Five invalid or missing credential combinations.
- Complete backpack checkout with generated customer information.
- Shared BDD steps and reusable page-object fixtures.
- Hooks logging scenario start/end, step start/success, and step errors.
- Step text included in STEP START log entries.
- A smoke tag for the complete checkout scenario.

The project also retains four plain pytest UI tests from Lesson 11.
A separate unit test covers a fixed-amount discount helper created
during Red → Green → Refactor practice.

## Setup

Install uv, then run:

```bash
uv sync
uv run playwright install chromium
```

Create a local `.env` file in the project root:

```text
STANDARD_USER=standard_user/secret_sauce
LOCKED_OUT_USER=locked_out_user/secret_sauce
PROBLEM_USER=problem_user/secret_sauce
PERFORMANCE_GLITCH_USER=performance_glitch_user/secret_sauce
ERROR_USER=error_user/secret_sauce
VISUAL_USER=visual_user/secret_sauce
```

These are public SauceDemo practice credentials.
The `.env` file is excluded from Git.

## Run all tests

```bash
uv run pytest -v
```

## Run data-driven cart tests

```bash
uv run pytest tests/test_inventory_data_driven.py -v
```

## Run data-driven login tests

```bash
uv run pytest tests/test_login_data_driven.py -v
```

## Run the smoke test

```bash
uv run pytest -m smoke -v
```

## Reports and logs

- Allure results: `allure-results/`
- BDD hook log: `logs/bdd_run.log`
- General test log: `logs/test_run.log`
- Screenshots on failure: `artifacts/`

Generated reports, logs, and artifacts are excluded from Git.

## Verified locally

- Latest recorded full suite: 26 passed.
- Coverage: 21 BDD cases, 4 plain pytest UI tests, and 1 unit test.
- The checkout smoke test previously passed.
- Browser for UI tests: Chromium.

These results describe recorded local runs; tests were not rerun
for this documentation update.

## Related homework repositories

Lesson 11 — SauceDemo pytest framework:
https://github.com/evgeniizoteev/saucedemo-framework-ez

Additional Lesson 12 practice — The Internet BDD framework:
https://github.com/evgeniizoteev/the-internet-bdd-ez

Lesson 14 — DemoQA API tests:
https://github.com/evgeniizoteev/demoqa-api-ez
