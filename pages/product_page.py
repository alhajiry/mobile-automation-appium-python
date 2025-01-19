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
