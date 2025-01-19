from pytest_bdd import given, when, then, parsers, scenario
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

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

@then(parsers.parse("I will be redirected to product detail page for '{product_name}'"))
def verify_product_detail(driver, product_name):
    product_page = ProductPage(driver)
    product_detail_visibility, product_name_visibility = product_page.verify_is_on_product_detail_page(product_name)
    assert product_detail_visibility is not None, f"Product detail page is not displayed'"
    assert product_name_visibility is not None, f"Product detail page does not contain product with name'{product_name}'"

@when("I click buy now button")
def user_click_buy_now_button(driver):
    product_page = ProductPage(driver)
    product_page.click_buy_now_button()

@then("Product content details with variant and quantity selection will be be displayed")
def verify_product_content_bottomsheet_displayed(driver):
    product_page = ProductPage(driver)
    product_content_bottomsheet_visibility = product_page.verify_buy_now_detail_displayed()
    assert product_content_bottomsheet_visibility is not None

@when(parsers.parse("I select product '{variant_attribute}' variant with '{variant_option}'"))
def user_select_variant(driver, variant_attribute, variant_option):
    product_page = ProductPage(driver)
    product_page.select_variant(variant_attribute, variant_option)

@then("The product checkout page will be displayed")
def verify_checkout_page_displayed(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page_visibility = checkout_page.verify_is_on_checkout_page()
    assert checkout_page_visibility is not None

@then(parsers.parse("Product with name '{product_name}' displayed on the checkout page"))
def verify_product_in_checkout_page(driver, product_name):
    checkout_page = CheckoutPage(driver)
    product_name_displayed = checkout_page.verify_checkout_product_name_is_correct(product_name)
    assert product_name_displayed

@then(parsers.parse("Product with quantity '{product_quantity}' displayed on the checkout page"))
def verify_product_in_checkout_page(driver, product_quantity):
    checkout_page = CheckoutPage(driver)
    product_quantity_displayed = checkout_page.verify_checkout_product_quantity_is_correct(product_quantity)
    assert product_quantity_displayed

@then(parsers.parse("Product with variant '{product_variant}' displayed on the checkout page"))
def verify_product_in_checkout_page(driver, product_variant):
    checkout_page = CheckoutPage(driver)
    product_variant_displayed = checkout_page.verify_checkout_product_variant_is_correct(product_variant)
    assert product_variant_displayed

@when("I click pay button on the checkout page")
def user_click_pay_button_in_checkout_page(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.click_pay_button()

@then("I will redirected to order status page")
def verify_redirection_to_order_status_page(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.verify_redirection_to_order_status_page()





