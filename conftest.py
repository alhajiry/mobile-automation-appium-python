import pytest
from base_driver import BaseDriver
from dotenv import load_dotenv
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

def pytest_configure(config):
    load_dotenv()

@pytest.fixture(scope='function', autouse=True)
def driver():
    base_driver = BaseDriver()
    driver = base_driver.get_driver()
    yield driver
    base_driver.stop_driver()

@pytest.fixture(scope='function')
def home_page(driver):
    return HomePage(driver)

@pytest.fixture(scope='function')
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture(scope='function')
def search_page(driver):
    return SearchPage(driver)

@pytest.fixture(scope='function')
def product_page(driver):
    return ProductPage(driver)

@pytest.fixture(scope='function')
def checkout_page(driver):
    return CheckoutPage(driver)
