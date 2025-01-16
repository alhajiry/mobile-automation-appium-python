from appium import webdriver
from appium.options.common import AppiumOptions

class BaseDriver:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        options = AppiumOptions()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.device_name = 'emulator-5554'
        options.noReset = True
        options.platform_version = '15'
        options.appPackage = 'blibli.mobile.commerce'
        options.appActivity = 'blibli.mobile.ng.commerce.core.home_page.view.HomePageActivity'

        self.driver = webdriver.Remote('http://localhost:4723', options=options)
        return self.driver

    def stop_driver(self):
        if self.driver:
            self.driver.quit()