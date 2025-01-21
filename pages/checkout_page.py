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
        self.wait_element_to_be_visible(CheckoutPageElements.CHECKOUT_PAGE_PAY_BUTTON)
        pay_button = self.get_element(CheckoutPageElements.CHECKOUT_PAGE_PAY_BUTTON)
        pay_button.click()

    def verify_checkout_product_quantity_is_correct(self, text):
        return self.wait_element_contains_text_to_be_visible(CheckoutPageElements.CHECKOUT_PAGE_PRODUCT_QUANTITY, text)
    
    def verify_checkout_product_variant_is_correct(self, text):
        return self.wait_element_contains_text_to_be_visible(CheckoutPageElements.CHECKOUT_PRODUCT_VARIANT, text)
    
    def verify_redirection_to_order_status_page(self):
        return self.wait_element_to_be_visible(CheckoutPageElements.ORDER_STATUS_PAGE)
    
    def scroll_to_bottom_of_checkout_page(self):
        self.scroll_to_end("bottom")

    def remove_payment_promo_restriction_if_exist(self):
        no_payment_method_btn = self.find_element_if_exists(CheckoutPageElements.CHECKOUT_PAGE_NO_PAYMENT_SELECTED)
        if no_payment_method_btn:
            self.get_element(CheckoutPageElements.CHECKOUT_PAGE_CHOOSE_PAYMENT_BUTTON).click()
            self.wait_element_to_be_visible(CheckoutPageElements.CHECKOUT_PAYMENT_PROMO_RADIO_BUTTON)
            self.get_element(CheckoutPageElements.CHECKOUT_PAYMENT_PROMO_RADIO_BUTTON).click()
            self.wait_element_to_be_visible(CheckoutPageElements.CHECKOUT_PAYMENT_METHOD_VIRTUAL_ACCOUNT)
            self.get_element(CheckoutPageElements.CHECKOUT_PAYMENT_METHOD_VIRTUAL_ACCOUNT).click()
            self.wait_element_to_be_visible(CheckoutPageElements.CHECKOUT_PAYMENT_METHOD_VIRTUAL_ACCOUNT_BCA)
            self.get_element(CheckoutPageElements.CHECKOUT_PAYMENT_METHOD_VIRTUAL_ACCOUNT_BCA).click()
            self.wait_element_to_be_visible(CheckoutPageElements.CHECKOUT_CONTINUE_WITHOUT_PROMO_BTN)
            self.get_element(CheckoutPageElements.CHECKOUT_CONTINUE_WITHOUT_PROMO_BTN).click()