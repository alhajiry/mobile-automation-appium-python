from elements.search_page_elements import SearchPageElements
from appium.webdriver.webelement import WebElement
from .base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def verify_product_with_name_displayed(self, product_name):
        # element = self.wait_element_contains_text_to_be_visible(SearchPageElements.PRODUCT_LIST, product_name)
        # return isinstance(element, WebElement)
        return self.wait_element_contains_text_to_be_visible(SearchPageElements.PRODUCT_LIST, product_name)
    
    def click_on_product_with_name(self, product_name):
        product = self.get_element_contains_text(SearchPageElements.PRODUCT_LIST, product_name)
        product.click()

        
        