import logging
import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LogInPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.login_xpath = "//input[@id='user-name']"
        self.password_xpath = "//input[@id='password']"
        self.log_in_button_xpath = "//input[@id='login-button']"
        self.wait = WebDriverWait(self.driver, 10)

    @allure.step("Wprowadzam login")
    def set_login(self, login):
        self.logger.info("Wprowadzam login")
        log_in_input = self.driver.find_element(By.XPATH, self.login_xpath)
        log_in_input.click()
        log_in_input.send_keys(login)

    @allure.step("Wprowadzam hasło")
    def set_password(self, password):
        self.logger.info("Wprowadzam hasło")
        password_input = self.driver.find_element(By.XPATH, self.password_xpath)
        password_input.click()
        password_input.send_keys(password)

    @allure.step("Loguję się")
    def perform_log_in(self):
        self.logger.info("Loguję się")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.log_in_button_xpath)))
        self.driver.find_element(By.XPATH, self.log_in_button_xpath).click()

    @allure.step("Akceptacja cookies")
    def accept_cookies(self):
        self.logger.info("Akceptacja cookies")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.cookies_accept_xpath)))
        self.driver.find_element(By.XPATH, self.cookies_accept_xpath).click()

    @allure.step("Wylaczenie powiadomien")
    def decline_notifications(self):
        self.logger.info("Wylaczenie powiadomien")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.decline_notifications_xpath)))
        self.driver.find_element(By.XPATH, self.decline_notifications_xpath).click()