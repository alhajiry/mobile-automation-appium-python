from elements.home_page_elements import HomePageElements
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def click_login_button(self):
        self.wait_element_to_be_visible(HomePageElements.LOGIN_BUTTON)
        login_button = self.get_element(HomePageElements.LOGIN_BUTTON)
        login_button.click()

    def search_product(self, product_name):
        self.wait_element_to_be_visible(HomePageElements.SEARCH_BOX)
        self.get_element(HomePageElements.SEARCH_BOX).click()
        self.wait_element_to_be_visible(HomePageElements.SEARCH_INPUT)
        search_input = self.get_element(HomePageElements.SEARCH_INPUT)
        search_input.send_keys(product_name)
        self.press_key("ENTER")
        
        