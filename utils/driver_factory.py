"""
W tym pliku znajdują się ustawienia dla wszystkich przeglądarek, na jakich przewidujemy moźliwość odpalenia testów.
Ja na razie korzystałam tylko z maksymalizacji okna na starcie (szybciej jest otwierać okno jako zmaksymalizowane, niż
otwierać przeglądarkę i dopiero maksymalizować (w perspektywie kilku testów to nie robi jakiejś dużej różnicy, ale
jak testów będzie dużo, to pozwoli oszczędzić trochę czasu).

Na razie wpisałam ustawienia dla:
    > chrome
    > firefox
    > internet explorer
    > microsoft egde
    > 'remote' dla selenium grida

* IE i Edge mają jakiś problem i nie działają *

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
from msedge.selenium_tools import EdgeOptions, Edge


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        """
        elif browser == "ie":
            options = webdriver.IeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Ie(executable_path=IEDriverManager().install(), options=options)
        elif browser == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            options.add_argument("--start-maximized")
            return Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)
        """
        elif browser == "remote":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.set_capability("browserName", browser)
            return webdriver.Remote("http://10.10.15.121:4444/wd/hub", options=options)
        return Exception("Provide valid driver name")
