# 🧪 SauceDemo UI Automation Project

Overview
This project is a UI automation framework for testing the SauceDemo web application using Selenium WebDriver and Pytest with Page Object Model (POM) design pattern.

The goal of this project is to demonstrate practical skills in UI test automation, test design, and framework structure.


Tech Stack
- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager

Project Structure

pages/          # Page Object Models (UI layers)
tests/          # Test cases
conftest.py     # Pytest fixtures (driver setup)
pytest.ini      # Pytest configuration
requirements.txt


Test Coverage

Functional tests:
- Successful login
- Invalid login (negative case)
- Inventory page validation
- Add item to cart
- Cart verification


How to Run Tests

1. Install dependencies:
```bash
pip install -r requirements.txt
2.Run tests:
pytest

Key Features

Page Object Model (POM)
Reusable BasePage
Explicit waits for stability
Clean test structure
Separation of test logic and UI logic

What this project demonstrates

UI automation skills
Selenium WebDriver usage
Test framework design
Basic QA automation architecture
Writing stable and maintainable tests
