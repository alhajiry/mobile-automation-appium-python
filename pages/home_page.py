from elements.home_page_elements import HomePageElements
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def click_login_button(self):
        self.wait_element_to_be_visible(HomePageElements.LOGIN_BUTTON, 60)
        self.get_element(HomePageElements.LOGIN_BUTTON)
        