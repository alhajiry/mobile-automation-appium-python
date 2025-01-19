from elements.login_page_elements import LoginPageElements
from .base_page import BasePage
import os

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    def input_email(self):
        self.wait_element_to_be_visible(LoginPageElements.EMAIL_INPUT)
        email_input = self.get_element(LoginPageElements.EMAIL_INPUT)
        email_input.click()
        email_input.send_keys(os.getenv("BLIBLI_USERNAME"))
    
    def input_password(self):
        self.wait_element_to_be_visible(LoginPageElements.PASSWORD_INPUT)
        password_input = self.get_element(LoginPageElements.PASSWORD_INPUT)
        password_input.click()
        password_input.send_keys(os.getenv("BLIBLI_PASSWORD"))
    
    def click_login_button(self):
        self.wait_element_to_be_visible(LoginPageElements.LOGIN_BUTTON)
        login_button = self.get_element(LoginPageElements.LOGIN_BUTTON)
        login_button.click()

        
        