import pytest
from pages.log_in_page import LogInPage
import allure
import time


@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Zaloguj")
    def test_log_in(self, setup):
        self.driver.get("https://www.saucedemo.com")
        log_in_page = LogInPage(self.driver)
        log_in_page.set_login("standard_user")
        log_in_page.set_password("secret_sauce")
        log_in_page.perform_log_in()
        time.sleep(10)
        