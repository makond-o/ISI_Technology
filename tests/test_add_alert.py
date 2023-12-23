import pytest
from config.config import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.alerts_page import AlertsPage
from Objects.warning import WarningObject
import time


@pytest.mark.usefixtures('setup')
class TestAlert:

    def test_add_alert_with_valid_data(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alerts_page.go_to_alerts_list_last_page()
        last_alert_id = alerts_page.get_last_alert_id()
        expected_alert_name = "test_name"
        expected_temperature_from = "50"
        expected_temperature_to = "100"
        expected_send_sms_value = "Yes"
        expected_send_email_value = "Yes"
        alerts_page.add_alert_with_office_location(expected_alert_name, expected_temperature_from,
                                                   expected_temperature_to, is_to_send_sms=True,  is_to_send_email=True)
        time.sleep(1)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.verify_last_alert_properties(last_alert_id, expected_alert_name, expected_temperature_from,
                                                 expected_temperature_to, expected_send_sms_value, expected_send_email_value)
        alerts_page.delete_last_alert()

    def test_add_alert_with_empty_name(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alerts_page.go_to_alerts_list_last_page()
        expected_alert_id = alerts_page.get_last_alert_id()
        alerts_page.add_alert_with_office_location(temperature_from=10, temperature_to=70)
        last_alert_id = alerts_page.get_last_alert_id()
        assert last_alert_id == expected_alert_id, "Alert with empty name is added"
        WarningObject(self.driver).verify_visible()

    def test_add_alert_with_empty_temperature_from(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alerts_page.go_to_alerts_list_last_page()
        expected_alert_id = alerts_page.get_last_alert_id()
        alerts_page.add_alert_with_office_location(name="testname", temperature_to=70)
        last_alert_id = alerts_page.get_last_alert_id()
        assert last_alert_id == expected_alert_id, "Alert with empty temperature_from field is added"
        WarningObject(self.driver).verify_visible()

    def test_add_alert_with_empty_temperature_to(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alerts_page.go_to_alerts_list_last_page()
        expected_alert_id = alerts_page.get_last_alert_id()
        alerts_page.add_alert_with_office_location(name="testname", temperature_from=70)
        last_alert_id = alerts_page.get_last_alert_id()
        assert last_alert_id == expected_alert_id, "Alert with empty temperature_to field is added"
        WarningObject(self.driver).verify_visible()

    def test_add_alert_with_empty_location(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alerts_page.go_to_alerts_list_last_page()
        expected_alert_id = alerts_page.get_last_alert_id()
        alerts_page.add_alert_with_office_location(
            name="testname", temperature_from=70, temperature_to=80, set_office_location=False)
        last_alert_id = alerts_page.get_last_alert_id()
        assert last_alert_id == expected_alert_id, "Alert without location is added"
        WarningObject(self.driver).verify_visible()

    def test_edit_alert_name(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alert_name = "test_name"
        expected_name = "new_test_name"
        temperature_from = "50"
        temperature_to = "100"
        alerts_page.add_alert_with_office_location(alert_name, temperature_from, temperature_to)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.edit_last_alert(new_name=expected_name)
        alerts_page.verify_last_alert_properties(expected_name=expected_name)
        alerts_page.delete_last_alert()

    def test_edit_alert_temperature_from(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alert_name = "test_name"
        temperature_from = "50"
        expected_temperature_from = "70"
        temperature_to = "100"
        alerts_page.add_alert_with_office_location(alert_name, temperature_from, temperature_to)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.edit_last_alert(new_temperature_from=expected_temperature_from)
        alerts_page.verify_last_alert_properties(expected_temperature_from=expected_temperature_from)
        alerts_page.delete_last_alert()

    def test_edit_alert_temperature_to(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alert_name = "test_name"
        temperature_from = "50"
        temperature_to = "100"
        expected_temperature_to = "120"
        alerts_page.add_alert_with_office_location(alert_name, temperature_from, temperature_to)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.edit_last_alert(new_temperature_to=expected_temperature_to)
        alerts_page.verify_last_alert_properties(expected_temperature_to=expected_temperature_to)
        alerts_page.delete_last_alert()

    def test_edit_alert_send_sms(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alert_name = "test_name"
        temperature_from = "50"
        temperature_to = "100"
        expected_send_sms_value = "Yes"
        alerts_page.add_alert_with_office_location(alert_name, temperature_from, temperature_to)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.edit_last_alert(change_send_sms=True)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.verify_last_alert_properties(expected_value_send_sms=expected_send_sms_value)
        alerts_page.delete_last_alert()

    def test_edit_alert_send_email(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        alerts_page = AlertsPage(self.driver)
        login_page.login(TestData.LOGIN, TestData.PASSWORD)
        home_page.open_alerts_page()
        alert_name = "test_name"
        temperature_from = "50"
        temperature_to = "100"
        expected_send_email_value = "Yes"
        alerts_page.add_alert_with_office_location(alert_name, temperature_from, temperature_to)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.edit_last_alert(change_send_email=True)
        alerts_page.go_to_alerts_list_last_page()
        alerts_page.verify_last_alert_properties(expected_value_send_email=expected_send_email_value)
        alerts_page.delete_last_alert()
