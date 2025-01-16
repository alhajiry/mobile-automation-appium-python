from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, element: str, timeout: int = 10):
        element_split = element.split(":", 1)
        locator = element_split[0]
        selector = element_split[1]

        match locator:
            case "id":
                return self.driver.find_element(AppiumBy.ID, selector)
            case "xpath":
                return self.driver.find_element(AppiumBy.XPATH, selector)
            case "class":
                return self.driver.find_element(AppiumBy.CLASS_NAME, selector)
            case "AccessibilityId":
                return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, selector)
            case "AndroidUIAutomator":
                return self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, selector)
            case default:
                raise ValueError(f"Invalid locator type: {locator}")

    def wait_element_to_be_visible(self, element: str, timeout: int = 10):
        element_split = element.split(":", 1)
        locator = element_split[0]
        selector = element_split[1]

        match locator:
            case "id":
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((AppiumBy.ID, selector)))
            case "xpath":
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((AppiumBy.XPATH, selector)))
            case "class":
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, selector)))
            case "AccessibilityId":
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, selector)))
            case "AndroidUIAutomator":
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, selector)))
            case default:
                raise ValueError(f"Invalid locator type: {locator}")
