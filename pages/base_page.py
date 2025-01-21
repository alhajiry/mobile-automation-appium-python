from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import appium.webdriver.extensions.android.nativekey as nativekey

class BasePage:
    def __init__(self, driver, timeout = 30):
        self.driver = driver
        self.timeout = timeout

    def get_element(self, element: str):
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

    def wait_element_to_be_visible(self, element: str, timeout=None):
        if timeout is None:
            timeout = self.timeout

        element_split = element.split(":", 1)
        locator = element_split[0]
        selector = element_split[1]

        wait = WebDriverWait(self.driver, self.timeout)

        match locator:
            case "id":
                return wait.until(EC.visibility_of_element_located((AppiumBy.ID, selector)))
            case "xpath":
                return wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, selector)))
            case "class":
                return wait.until(EC.visibility_of_element_located((AppiumBy.CLASS_NAME, selector)))
            case "AccessibilityId":
                return wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, selector)))
            case "AndroidUIAutomator":
                return wait.until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, selector)))
            case default:
                raise ValueError(f"Invalid locator type: {locator}")
            
    def wait_element_contains_text_to_be_visible(self, element: str, element_text: str, timeout=None):
        element_split = element.split(":", 1)
        selector = element_split[1]
        selector_with_text = f"{selector[:-1]} and contains(@text, '{element_text}')]"

        wait = WebDriverWait(self.driver, self.timeout)
        return wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, selector_with_text)))
    
    def get_element_contains_text(self, element:str, element_text:str, timeout=None):
        element_split = element.split(":", 1)
        selector = element_split[1]
        selector_with_text = f"{selector[:-1]} and contains(@text, '{element_text}')]"
        return self.driver.find_element(AppiumBy.XPATH, selector_with_text)
    
    def find_element_if_exists(self, element):
        try:
            self.wait_element_to_be_visible(element)
            return self.get_element(element)
        except NoSuchElementException:
            return None

    def press_key(self, keycode):
        androidkey = nativekey.AndroidKey
        
        key = androidkey.__dict__.get(keycode, None)
        if key is not None:
            self.driver.press_keycode(key)
        else:
            raise ValueError(f"Invalid keycode: {keycode}")
        
    def scroll_to_end(self, direction):
        screen_size = self.driver.get_window_size()
        start_y = screen_size['height'] * 0.8
        end_y = screen_size['height'] * 0.2
        start_x = screen_size['width'] * 0.5

        previous_page_source = ''
        while True:
            current_page_source = self.driver.page_source
            if current_page_source == previous_page_source:
                # Reached the end of the page
                break
            previous_page_source = current_page_source

            if direction == 'top':
                self.driver.swipe(start_x, end_y, start_x, start_y, 800)
            elif direction == 'bottom':
                self.driver.swipe(start_x, start_y, start_x, end_y, 800)
            else:
                raise ValueError("Invalid direction specified: choose 'up' or 'down'")


            