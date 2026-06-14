![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-E6E6E6?style=for-the-badge&logo=allure&logoColor=black)
![Pytest HTML](https://img.shields.io/badge/Pytest_HTML-009688?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)

# Pytest Selenium Automation Framework

A scalable and maintainable UI automation framework built using **Python, Selenium WebDriver, and Pytest** for the **Demo Web Shop** application. This project demonstrates modern test automation practices using industry-standard design patterns, reusable components, and reporting tools.

---

## Features

- Cross-browser support (Chrome & Firefox)
- Headless and Normal execution modes
- Page Object Model (POM) design pattern
- Centralized configuration management using `config.ini`
- Automatic driver management with `webdriver-manager`
- Explicit and configurable wait strategies
- Structured logging and debugging support
- Pytest markers for selective test execution
- Allure Reporting integration
- Pytest HTML Reporting
- Parallel execution support using `pytest-xdist`
- CI/CD ready for GitHub Actions and Jenkins

---

## Application Under Test

**Demo Web Shop**

https://demowebshop.tricentis.com/

Demo Web Shop is a sample e-commerce platform used for practicing automation testing scenarios such as:

- User Registration
- User Login
- Product Search
- Add to Cart
- Wishlist Management
- Product Comparison
- Checkout Flow
- Order Placement

---

## Tech Stack

| Technology | Purpose |
|------------|----------|
| Python 3.x | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| WebDriver Manager | Driver Management |
| Allure Reports | Advanced Reporting |
| Pytest HTML | HTML Reporting |
| Logging | Test Execution Logs |

---

## Project Structure

```text
Pytest_Automation_Project
│
├── configuration/          # Configuration files
├── pages/                  # Page Object Classes
├── actions/                # Business Layer Actions
├── tests/                  # Test Cases
├── utils/                  # Utility Classes
├── data_provider/          # Test Data Files
├── logs/                   # Execution Logs
├── reports/                # Generated Reports
├── conftest.py             # Fixtures & Driver Setup
├── pytest.ini              # Pytest Configuration
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Pytest_Automation_Project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Update the `configuration/config.ini` file:

```ini
[browser]
browser = chrome
mode = normal

[application]
url = https://demowebshop.tricentis.com/
title = Demo Web Shop

[timeouts]
explicit_wait = 15
page_load_timeout = 30
```

---

## Running Tests

### Run All Tests

```bash
pytest
```

### Verbose Execution

```bash
pytest -v
```

### Run Specific Test File

```bash
pytest tests/test_register.py -v
```

### Run Using Markers

```bash
pytest -m smoke
pytest -m regression
pytest -m sanity
pytest -m "smoke and regression"
```

---

## Parallel Execution

Run tests using multiple workers:

```bash
pytest -n 4
```

---

## Reports

### Pytest HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

### Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```

### Generate Static Allure Report

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

---

## Sample Test Structure

```python
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_user_login(driver):
    drv, wait = driver

    # Test Steps

    assert "Demo Web Shop" in drv.title
```

---

## Covered Test Scenarios

- User Registration
- User Login
- Product Search
- Product Filtering
- Add Product to Cart
- Add Product to Wishlist
- Remove Product from Cart
- Product Comparison
- Checkout Process
- Logout Functionality

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Follow the existing POM structure
4. Add proper logging and assertions
5. Test changes in Chrome and Firefox
6. Submit a Pull Request

---

## Future Enhancements

- API Testing Integration
- Docker Execution Support
- BrowserStack Integration
- Data-Driven Testing with Excel and JSON
- Advanced Reporting Dashboard
- Test Analytics Integration

---

## Contributors

- Vithya
- Haritha
- sowndariya
- Vetrivel
- JeevaPranesh

---

## License

This project is intended for learning and educational purposes.

---

Built with Python, Selenium WebDriver, and Pytest for modern web UI automation.
