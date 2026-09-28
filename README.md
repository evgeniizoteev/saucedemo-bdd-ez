# Sauce Demo Test Automation Framework

UI test automation framework for https://www.saucedemo.com/.

The project uses Python, Playwright, pytest, Page Object Model, Faker, logging, and Allure reports.

## Project structure

- `pages/` — locators and page actions
- `tests/` — test scenarios and assertions
- `data/` — test users and product data
- `helpers/` — reusable test-data helpers
- `conftest.py` — pytest fixtures and reporting hooks
- `.env.example` — safe credentials template

## Setup

```bash
uv sync
cp .env.example .env
uv run playwright install chromium
```

Add valid local test credentials to `.env`. Never commit `.env`.

## Run tests

```bash
uv run pytest
uv run pytest --headed
uv run pytest --headed --slowmo 800
```

## Code quality

```bash
uvx black --check .
uvx flake8 .
```

## Reports and logs

Test runs create local Allure results, an HTML report, screenshots on failure, and logs. Generated artifacts are excluded from Git.
