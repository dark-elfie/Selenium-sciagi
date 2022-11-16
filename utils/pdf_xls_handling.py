"""
Poniższe komendy mają za zadanie spróbować otworzyć pliki pdf lub xls - jeżeli plik jest uszkodzony, zwracany jest błąd
(używane w scenariuszach sprawdzających generowane przez systemy plików z fakturami, rozliczeniami itp.)
"""

import PyPDF2
from xlrd import open_workbook

path = "/ścieżka/do/pliku.pdf"
pdfFileObj = open(path, 'rb')

#pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

path_xls = "/ścieżka/do/pliku.xls"

wb_obj = open_workbook(path_xls, on_demand=True)