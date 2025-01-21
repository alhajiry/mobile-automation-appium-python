from elements.product_page_elements import ProductPageElements
from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def verify_is_on_product_detail_page(self, product_name):
        product_detail_visibility = self.wait_element_to_be_visible(ProductPageElements.PRODUCT_DETAIL_PAGE)
        product_name_visibility = self.wait_element_contains_text_to_be_visible(ProductPageElements.PRODUCT_DETAIL_NAME, product_name)

        return product_detail_visibility, product_name_visibility
    
    def click_buy_now_button(self):
        self.wait_element_to_be_visible(ProductPageElements.PRODUCT_BUY_NOW_BUTTON)
        buy_now_button = self.get_element(ProductPageElements.PRODUCT_BUY_NOW_BUTTON)
        buy_now_button.click()

    def verify_buy_now_detail_displayed(self):
        return self.wait_element_to_be_visible(ProductPageElements.PRODUCT_CONTENT_BOTTOMSHEET)

    def select_variant(self, variant_attribute, variant_option):
        element = ""
        if variant_attribute == "color":
            element = ProductPageElements.PRODUCT_CONTENT_COLOR_VARIANT_SELECTION
        elif variant_attribute == "capacity":
            element = ProductPageElements.PRODUCT_CONTENT_CAPACITY_VARIANT_SELECTION

        self.wait_element_contains_text_to_be_visible(element, variant_option)
        variant_selection = self.get_element_contains_text(element, variant_option)
        variant_selection.click()



