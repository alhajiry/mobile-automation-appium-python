from elements.checkout_page_elements import CheckoutPageElements
from .base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def verify_is_on_checkout_page(self):
        return self.wait_element_to_be_visible(CheckoutPageElements.CHECKOUT_PAGE_VIEW)

    def verify_checkout_product_name_is_correct(self, text):
        return self.wait_element_contains_text_to_be_visible(CheckoutPageElements.CHECKOUT_PRODUCT_NAME, text)

    def click_pay_button(self):
        pay_button = self.get_element(CheckoutPageElements.CHECKOUT_PAGE_PAY_BUTTON)
        pay_button.click()

    def verify_checkout_product_quantity_is_correct(self, text):
        return self.wait_element_contains_text_to_be_visible(CheckoutPageElements.CHECKOUT_PAGE_PRODUCT_QUANTITY, text)
    
    def verify_checkout_product_variant_is_correct(self, text):
        return self.wait_element_contains_text_to_be_visible(CheckoutPageElements.CHECKOUT_PRODUCT_VARIANT, text)
    
    def verify_redirection_to_order_status_page(self):
        return self.wait_element_to_be_visible(CheckoutPageElements.ORDER_STATUS_PAGE)