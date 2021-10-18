import allure
import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")     # wybieram przeglądarkę (z obsługwanych w pliku driver_factory.py)
    driver.implicitly_wait(10)      # ustawia oczekiwanie przed wyrzuceniem wyjątku dla całego skryptu
    request.cls.driver = driver     # daje dostęp do driver wszystkim testom, które korzystają z fixture setup
    before_failed = request.session.testsfailed     # przed rozpoczęciem testu sprawdza ile testów zakończyło się
                                                    # niepowodzeniem
    yield
    # po wykonaniu testu sprawdzamy czy liczba niepowodzeń się zmieniła, jeżeli tak - robimy screenshota
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=allure.attachment_type.PNG)
    driver.quit()

    # allure.attach() - powinno załączać wykonanego screena, ale w praktyce ma z tym czasami problem (nie wiem dlaczego)
