import pytest
from base_driver import BaseDriver

@pytest.fixture(scope='function', autouse=True)
def driver():
    base_driver = BaseDriver()
    driver = base_driver.get_driver()
    yield driver
    base_driver.stop_driver()

