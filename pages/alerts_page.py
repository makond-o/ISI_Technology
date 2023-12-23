from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from selenium.webdriver.support import expected_conditions
import time


class AlertsPage(HomePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._page_url_component = "alert"
        self._add_alert_button = (By.CSS_SELECTOR, '*[ng-click="addAlert()"]')
        self._save_alert_button = (By.CSS_SELECTOR, 'button[class="btn btn-lg mr5 ml5 btn-success"]')
        self._delete_alert_button = (By.CSS_SELECTOR, 'button[ng-click="deleteAlert(alertDetail.id)"]')
        self._name_field = (By.CSS_SELECTOR, 'input[name="name"]')
        self._temperature_from_field = (By.CSS_SELECTOR, 'input[name="alert_from"]')
        self._temperature_to_field = (By.CSS_SELECTOR, 'input[name="alert_to"]')
        self._search_location_field = (By.CSS_SELECTOR, 'input[name="office_search"]')
        self._send_sms_checkbox = (By.CSS_SELECTOR, 'input[name="send_sms"]')
        self._send_email_checkbox = (By.CSS_SELECTOR, 'input[name="send_email"]')
        self._office_location_button = (By.CSS_SELECTOR, 'td[title="Office"]')
        self._alerts_list_last_page = (By.CSS_SELECTOR, 'a[ng-click="selectPage(totalPages, $event)"]')
        self._last_alert_table_item_locator =\
            'tbody[ng-hide="alertIsLoading"]>tr[class="thin-tr cursor-pointer ng-scope"]:nth-last-child(2)'
        self._last_alert_id_element = (By.CSS_SELECTOR,
                                       self._last_alert_table_item_locator + '>td:nth-child(1)')
        self._last_alert_name_element = (By.CSS_SELECTOR,
                                         self._last_alert_table_item_locator + '>td:nth-child(2)')
        self._last_alert_temperature_from_element = (By.CSS_SELECTOR,
                                                     self._last_alert_table_item_locator + '>td:nth-child(3)')
        self._last_alert_temperature_to_element = (By.CSS_SELECTOR,
                                                   self._last_alert_table_item_locator + '>td:nth-child(4)')
        self._last_alert_send_sms_element = (By.CSS_SELECTOR,
                                                   self._last_alert_table_item_locator + '>td:nth-child(5)')
        self._last_alert_send_email_element = (By.CSS_SELECTOR,
                                               self._last_alert_table_item_locator + '>td:nth-child(6)')

    def open_add_alert_form(self):
        self.click(self._add_alert_button)

    def enter_name(self, value: str):
        self.enter_text(self._name_field, value)

    def enter_temperature_from(self, value: str):
        self.enter_text(self._temperature_from_field, value)

    def enter_temperature_to(self, value: str):
        self.enter_text(self._temperature_to_field, value)

    def click_send_sms_checkbox(self):
        element = self._driver.find_element(*self._send_sms_checkbox)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(0.5)
        self._driver.execute_script("arguments[0].click();", element)

    def click_send_email_checkbox(self):
        element = self._driver.find_element(*self._send_email_checkbox)
        self._driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(0.5)
        self._driver.execute_script("arguments[0].click();", element)

    def set_office_location(self):
        self.click(self._office_location_button)

    def save_alert(self):
        self.click(self._save_alert_button)

    def add_alert_with_office_location(self, name=None, temperature_from=None, temperature_to=None,
                                       is_to_send_sms=False, is_to_send_email=False, set_office_location=True):
        self.open_add_alert_form()
        if name:
            self.enter_name(name)
        if temperature_from:
            self.enter_temperature_from(temperature_from)
        if temperature_to:
            self.enter_temperature_to(temperature_to)
        if is_to_send_sms:
            self.click_send_sms_checkbox()
        if is_to_send_email:
            self.click_send_email_checkbox()
        if set_office_location:
            self.set_office_location()
            self.is_visible((By.CSS_SELECTOR, 'div[ng-click="removeOffice(office)"]'))
        self.save_alert()

    def go_to_alerts_list_last_page(self):
        self.click(self._alerts_list_last_page)

    def get_last_alert_id(self):
        last_alert_id = self.get_element_text(self._last_alert_id_element)
        return last_alert_id

    def edit_last_alert(self, new_name=None, new_temperature_from=None, new_temperature_to=None, change_send_sms=False,
                        change_send_email=False):
        self.click(self._last_alert_id_element)
        if new_name:
            self.clear_textbox(self._name_field)
            self.enter_name(new_name)
        if new_temperature_from:
            self.clear_textbox(self._temperature_from_field)
            self.enter_temperature_from(new_temperature_from)
        if new_temperature_to:
            self.clear_textbox(self._temperature_to_field)
            self.enter_temperature_to(new_temperature_to)
        if change_send_sms:
            self.click_send_sms_checkbox()
        if change_send_email:
            self.click_send_email_checkbox()
        self.save_alert()

    def delete_last_alert(self):
        self.click(self._last_alert_id_element)
        self.click(self._delete_alert_button)

    def verify_last_alert_properties(
            self, prior_alert_id=None, expected_name=None, expected_temperature_from=None, expected_temperature_to=None,
            expected_value_send_sms=None, expected_value_send_email=None):
        if prior_alert_id:
            actual_id = self.get_element_text(self._last_alert_id_element)
            assert actual_id != prior_alert_id, \
                f"Id of last alert should be different from prior alert id." \
                f"Actual id: {actual_id}. Prior alert id: {prior_alert_id}"
        if expected_name:
            actual_name = self.get_element_text(self._last_alert_name_element)
            assert actual_name == expected_name, \
                f"Name of last alert should be {expected_name}. Actual name: {actual_name}"
        if expected_temperature_from:
            actual_temperature_from = self.get_element_text(self._last_alert_temperature_from_element)
            assert actual_temperature_from == expected_temperature_from, \
                f"'Temperature from' value of last alert should be {expected_temperature_from}." \
                f"Actual name: {actual_temperature_from}"
        if expected_temperature_to:
            actual_temperature_to = self.get_element_text(self._last_alert_temperature_to_element)
            assert actual_temperature_to == expected_temperature_to,\
                f"'Temperature to' value of last alert should be {expected_temperature_to}." \
                f"Actual name: {actual_temperature_to}"
        if expected_value_send_sms:
            actual_send_sms_value = self.get_element_text(self._last_alert_send_sms_element)
            assert actual_send_sms_value == expected_value_send_sms, \
                f"'Send sms' value of last alert should be {expected_value_send_sms}." \
                f"Actual name: {actual_send_sms_value}"
        if expected_value_send_email:
            actual_send_email_value = self.get_element_text(self._last_alert_send_email_element)
            assert actual_send_email_value == expected_value_send_email,\
                f"'Send email' value of last alert should be {expected_value_send_email}." \
                f"Actual name: {actual_send_email_value}"


