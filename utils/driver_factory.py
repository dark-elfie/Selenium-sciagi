"""
W tym pliku znajdują się ustawienia dla wszystkich przeglądarek, na jakich przewidujemy moźliwość odpalenia testów.
Ja na razie korzystałam tylko z maksymalizacji okna na starcie (szybciej jest otwierać okno jako zmaksymalizowane, niż
otwierać przeglądarkę i dopiero maksymalizować (w perspektywie kilku testów to nie robi jakiejś dużej różnicy, ale
jak testów będzie dużo, to pozwoli oszczędzić trochę czasu).

Na razie wpisałam ustawienia dla:
    > local-chrome - lokalna przegladarka Chrome
    > local-firefox - lokalna przeglądarka Firefox
    > chrome - Chrome dostępne na serwerze Selenium Grid
    > firefox - Firefox dostępne na serwerze Selenium Grid
    > mobile - emulator Android dostępny przez Appium

W razie czego można dopisac następne tylo trzeba pamiętać o importowaniu odpowiednich DriverManagerów.

W executable_path można wpisać plik exe DriverManagera danej przeglądarki, tutaj korzystam z ułatwienia i np. dla Chrome
używam ChromeDriverManager().install(), który pobiera odpowiednią wersję managera do pamięci podręcznej i usuwa go po
zakończeniu testów.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from msedge.selenium_tools import EdgeOptions, Edge
from utils.helpers import ANDROID_BASE_CAPS
import copy


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "local-chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser == "local-firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

        """
        Zarówno powyższe, jak i poniższe wersje lokalnego uruchamiania przeglądarki są poprawne i obecnie działają -
        ^ górna wersja jest jednak przestarzała i w kolejnych wersjach webdriver może zostać usunięta, dlatego zalecane
        jest korzystane z dolnej wersji opartej na Service \/

        if browser == "local-chrome":
            s = ServiceCh(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            return webdriver.Chrome(service=s, options=options)
        elif browser == "local-firefox":
            s = ServiceF(GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Firefox(service=s, options=options)
            return driver
        elif browser == "chrome":
            options = webdriver.ChromeOptions()
            options.set_capability("browserName", "chrome")
            options.set_capability("applicationName", "8105cdf5-69a0-483a-b119-df325a726754")
            options.add_argument("--window-size=1350,1000")
            return webdriver.Remote("link do serwera Selenium Grid", options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.set_capability("browserName", "firefox")
            options.set_capability("applicationName", "9dd4fccf-6c54-4b3c-89d8-462324066bef")
            options.add_argument("--window-size=1920,1080")
            return webdriver.Remote("link do serwera Selenium Grid", options=options)
        elif browser == "mobile":
            PACKAGE = 'io.appium.android.apis'
            SEARCH_ACTIVITY = '.app.SearchInvoke'
            ALERT_DIALOG_ACTIVITY = '.app.AlertDialogSamples'

            caps = copy.copy(ANDROID_BASE_CAPS)
            caps['appActivity'] = SEARCH_ACTIVITY

            driver = webdriver.Remote(
                'link do serwera Appium',
                desired_capabilities=caps
            )
            return driver
        """
        return Exception("Provide valid driver name")
