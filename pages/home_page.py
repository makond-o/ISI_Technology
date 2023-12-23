from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._alerts_menu_button = (By.CSS_SELECTOR, 'i[class="fa fa-exclamation-circle"]')
        self._dashboard_menu_button = (By.CSS_SELECTOR, 'i[class="fa fa-bar-chart"]')
        self._logout_button = (By.CSS_SELECTOR, 'a[ng-click="logout()"]')

    def open_alerts_page(self):
        self.click(self._alerts_menu_button)

    def open_dashboard_page(self):
        self.click(self._dashboard_menu_button)

    def logout(self):
        self.click(self._logout_button)
        self._wait.until(expected_conditions.invisibility_of_element_located(self._logout_button))
