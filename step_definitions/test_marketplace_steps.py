from pytest_bdd import given, when, then, parsers, scenario
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage

@scenario("marketplace.feature", "User checkout an item")
def test_user_login():
    pass

@given("I logged in to the Blibli application")
def user_login(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    home_page.click_login_button()
    login_page.input_email()
    login_page.click_login_button()
    login_page.input_password()
    login_page.click_login_button()

@when(parsers.parse("I search for a product '{product_name}'"))
def user_search_product(driver, product_name):
    home_page = HomePage(driver)
    home_page.search_product(product_name)

@then(parsers.parse("The product '{product_name}' will be displayed in the search results"))
def verify_search_product(driver, product_name):
    search_page = SearchPage(driver)
    product_visibility = search_page.verify_product_with_name_displayed(product_name)
    assert product_visibility is not None, f"Product '{product_name}' was not displayed in the search results"

@when(parsers.parse("I click on product '{product_name}'"))
def user_click_product(driver, product_name):
    search_page = SearchPage(driver)
    search_page.click_on_product_with_name(product_name)