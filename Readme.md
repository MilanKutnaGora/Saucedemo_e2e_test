# SauceDemo E2E Test

## This project contains an end-to-end test for the purchase flow on saucedemo.com using Python and Selenium.

### Prerequisites

#### - Python 3.7+

#### - Chrome browser

### Setup

#### 1. Clone the repository:

`git clone https://github.com/MilanKutnaGora/Saucedemo_e2e_test`

`cd saucedemo-e2e-test`

#### 2. Create and activate a virtual environment:

`python -m venv venv`

`source venv/bin/activate` 

#### On Windows, use 

`venv\Scripts\activate` 

#### 3. Install the required packages:

`pip install -r requirements.txt`

### Running the Tests

#### To run the tests, execute the following command:

`pytest tests/test_purchase_flow.py`

#### This will run the test in headless mode. If you want to see the browser in action, remove the `--headless` option from the `chrome_options` in `conftest.py`.