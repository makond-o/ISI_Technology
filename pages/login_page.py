from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._login_field = (By.CSS_SELECTOR, 'input[name="username"]')
        self._password_field = (By.CSS_SELECTOR, 'input[name="password"]')
        self._accept_terms_checkbox = (By.CSS_SELECTOR, 'input[name="accept_terms_and_conditions"]')
        self._login_button = (By.CSS_SELECTOR,
                              'button[class="login-button btn btn-default btn-block btn-lg mb15 ng-binding ng-scope"]')

    def set_login(self, value: str):
        self.enter_text(self._login_field, value)

    def set_password(self, value: str):
        self.enter_text(self._password_field, value)

    def click_login_button(self):
        self.click(self._login_button)

    def click_accept_terms_checkbox(self):
        self.click(self._accept_terms_checkbox)

    def login(self, email: str, password: str):
        self.set_login(email)
        self.set_password(password)
        self.click_accept_terms_checkbox()
        self.click_login_button()

