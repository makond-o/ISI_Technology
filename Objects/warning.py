from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class WarningObject:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self.warning_message_locator = (By.CSS_SELECTOR, 'div[class="message ng-binding"]')

    def is_visible(self):
        element = self._wait.until(expected_conditions.visibility_of_element_located(self.warning_message_locator))
        return bool(element)

    def verify_visible(self, should_be_visible=True):
        if should_be_visible:
            assert self.is_visible(), "Warning message should be displayed"
        else:
            assert not self.is_visible(), "Warning message should not be displayed"
