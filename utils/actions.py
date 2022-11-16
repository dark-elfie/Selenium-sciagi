import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure


@pytest.mark.usefixtures("log_in_admin")
class Test:

    @allure.title("Stwórz nową awizację")
    @pytest.mark.znacznik
    def test_searching_elements(self, log_in_admin):
        # szukanie elementu po ID
        self.driver.find_element_by_id("clickOnMe")     # dwie metody na to samo
        self.driver.find_element(By.ID, "clickOnMe")    # ^

        # szukanie elementu po name
        self.driver.find_element_by_name("fname")

        # szukanie przy pomocy tekstu z linka
        self.driver.find_element_by_link_text("Visit W3Schools.com!")       # musi być cały tekst
        self.driver.find_element_by_partial_link_text("Visit W3Schools")    # może być fragment tekstu

        # szukanie elementu po klasie
        self.driver.find_element_by_class_name("topSecret")     # jak element ma więcej niż jedną klasę też działa

        # szukanie elementu po tagu
        self.driver.find_element_by_tag_name("a")

        # selektory CSS
        self.driver.find_element_by_css_selector("a")
        self.driver.find_element_by_css_selector("img#smileImage")      # #klasa
        self.driver.find_element_by_css_selector("p.topSecret")         # .id
        self.driver.find_element_by_css_selector("th:first-child")

        # szukanie po XPath (wtyczka do Chrome - CHROPATH - bardzo ułatwia życie)
        self.driver.find_element_by_xpath("html/body/table/tbody/tr/th")
        self.driver.find_element_by_xpath("//tbody//th")
        self.driver.find_element_by_xpath("//th")       # lepiej jest nie podawać całej ścieżki (może się ona zmienić)
        self.driver.find_element_by_xpath("//th[text()='Month']")
        self.driver.find_element_by_xpath("//button[@id='clickOnMe']")
        self.driver.find_element_by_xpath("//input[@name='fname']/following-sibling::table")    # following-sibling - są
                                                                                            # na tej samej "głębokości"
        # branie listy elementów (zamiast pierwszego znalezionego)
        self.driver.find_elements_by_xpath("//input[@name='fname']/following-sibling::table")

    def test_checking_elements(self):
        element = self.driver.find_element_by_xpath("")
        element.is_selected()
        element.is_displayed()
        element.is_enabled()

        # sprawdzenie czy element istnieje bez 'wywalenia' testu
        try:
            self.driver.find_element_by_tag_name("jdjfeoi")
            print("Element istnieje na stronie")
        except NoSuchElementException:
            print("Element nie istnieje")

    def test_actions(self):
        # symulowanie podwójnego kliknięcia
        webdriver.ActionChains(self.driver).double_click(self.button).perform()

        # symulowanie PPM
        webdriver.ActionChains(self.driver).context_click(self.button).perform()

        # klikanie elementu i obsługa alertów
        self.driver.find_element_by_id("clickOnMe").click()
        self.driver.switch_to.alert.accept()
        click_me_button = self.driver.find_element_by_id("clickOnMe")
        click_me_button.click()
        self.driver.switch_to.alert.dismiss()

        # wprowadzenie wartości do inputa
        self.driver.find_element_by_id("fname").send_keys("Bartek")

        # usuwanie danych z pola
        self.driver.find_element_by_name("username").send_keys("Nick")       # bez wyczyszczenia dopisuje na końcu
        username_input = self.driver.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys("Nick")

        # symulowanie wciśnięcia Entera
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)  # klasa Keys pomaga symulować różne klawisze

        # wybieranie opcji z select
        auto_select = Select(self.driver.find_element_by_tag_name("select"))
        # auto_select.select_by_value("volvo")
        # auto_select.select_by_visible_text("Saab")
        auto_select.select_by_index(0)

        # sprawdzenie wyświetlania obrazków
        self.driver.find_element_by_id("smileImage").size.get("height")
        self.driver.find_element_by_id("smileImage").get_attribute("naturalHeight")
        # jeżeli atrybut naturalHeight jest >0, to obrazek jest poprawnie załadowany

        # przełączanie do nowego okna przeglądarki
        self.driver.find_element_by_id("newPage").click()
        current_window_name = self.driver.current_window_handle
        window_names = self.driver.window_handles

        for window in window_names:
            if window != current_window_name:
                self.driver.switch_to.window(window)

        self.driver.switch_to.window(current_window_name)

        # robienie screenshotów
        self.driver.save_screenshot("screenshots/after_upload.png")

    def test_waiting(self):
        time.sleep(10)      # zatrzymuje wykonanie programu na 10 sek.

        wait = WebDriverWait(self.driver, 10, 0.5, NoSuchElementException)  # (driver, timeout w sek, co ile sprawdza,
                                                                            # jakie wyjątki ignorować)
        # wystarczy podać driver i timeout: wait = WebDriverWait(self.driver, 10)
        xpath = ""
        wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))
        """
        wait.until - czeka aż nie zostanie spełniony podany warunek
        ec - zaimportowana bibliioteka expected_conditions jako ec
        W tej bibliotece jest dużo przydatnych warunków np:
            > visibility_of_element_located - czy element jest widoczny
            > element_to_be_clickable - czy można kliknąć w dany element
        """

        wait.until(lambda wd: len(self.driver.find_elements_by_tag_name("p")) == 1)
        """
        można też określać warunki przy pomocy lambdy np. tutaj - sprawdza czy liczba elementów znalezionych elementów 
        jest równa 1
        """
