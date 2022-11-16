import allure
import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("local-chrome")     # wybieram przeglądarkę (z obsługwanych w pliku driver_factory.py)
    driver.implicitly_wait(10)      # ustawia oczekiwanie przed wyrzuceniem wyjątku dla całego skryptu
    request.cls.driver = driver     # daje dostęp do driver wszystkim testom, które korzystają z fixture setup
    before_failed = request.session.testsfailed     # przed rozpoczęciem testu sprawdza ile testów zakończyło się
                                                    # niepowodzeniem
    yield
    # po wykonaniu testu sprawdzamy czy liczba niepowodzeń się zmieniła, jeżeli tak - robimy screenshota
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=allure.attachment_type.PNG)
    driver.quit()

    # allure.attach() - załącza wykonanego screena


@pytest.fixture()
def log_in(setup):
    driver.get("link do strony")
    log_in_page = LogInPage(driver)
    log_in_page.accept_cookies()
    if GlobalSettings.driver == "mobile":
        time.sleep(2)
        log_in_page.decline_notifications()
        time.sleep(2)
        log_in_page.set_login("login")
        log_in_page.set_password("hasło")
        driver.execute_script("window.scrollTo(0, 600)")
        log_in_page.perform_log_in()
        time.sleep(4)
    else:
        log_in_page.set_login("login")
        log_in_page.set_password("hasło")
        time.sleep(1)
        log_in_page.perform_log_in()
        time.sleep(4)
        log_in_page.decline_notifications()

"""
Powyższa funkcja (fixture) może być używana przez wszystkie testy, które wymagają zalogowania się (aby uniknąć osobnego
logowania w każdym teście z osobna), jako argument przyjmuje ona fixture 'setup', tzn. wywołuje ją przy swoim 
uruchomieniu i wykorzystuje utworzoną w niej przeglądarkę .

Tutaj dodatkowo widnieje podział na różne zachowania funkcji w zależności od trybu wykonywania testów - czy uruchamiane
są one w wersji desktopowej czy na emulatorze Android (często testy dla wersji desktopowej i mobilnej są bardzo podobne
lub nawet identyczne - o ile strony nie różnią się budową - jednak mobilna wersja czasami wymaga dodatkowych akcji, 
dlatego należy weryfikować działanie dla obu przypadków.
"""