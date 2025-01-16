from pytest_bdd import when, scenario
from pages.home_page import HomePage
from appium.webdriver.common.appiumby import AppiumBy

@scenario("../features/login.features", "Login to the application")
def test_login():
    pass

@when("I click the login button")
def click_login(driver):
    home_page = HomePage(driver)
    home_page.click_login_button()
    # driver.find_element(AppiumBy.ID, "blibli.mobile.commerce:id/bt_login").click()