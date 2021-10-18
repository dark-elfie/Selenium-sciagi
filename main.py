"""
Wymagane biblioreki:
    > selenium
    > pytest
    > webdriver-manager         (do uruchamiania instancji przeglądarek)
    > msedge-selenium-tools	    (od odpalania Egde)
    > allure                    (generowanie raportów)
    > pytest-xdist              (m.in. do równoległego uruchamiania testów - kilka przeglądarek na raz)


Komendy do uruchamiania testów:
    > pytest                                    - uruchamia wszystkie testy, które znajdzie w danym projekcie
    > pytest -n x                               - uruchamia testy równolegle na x przeglądarkach
    > pytest -k 'nazwa'                         - uruchamia wszystkie testy, które w nazwie klasy lub funcji
                                                  zawierają wyrażenie 'nazwa'
    > pytest -x                                 - przerywa testy po pierwszej porażce (error/fail)
    > pytest -v                                 - zwiększa szczegółowość raportu w konsoli
    > pytest --alluredir=ścieżka\do\folderu    - uruchamia testy ze wskazaniem folderu, do którego mają zostać wrzucone
                                                  pliki do wygenerowania raportu w Allure

Komendy Allure:
    > allure serve ścieżka\do\folderu           - generuje raport na podstawie plików z podanego folderu

"""