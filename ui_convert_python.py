from PyQt5 import uic

with open("Murettebat_Ekle.py","w", encoding="utf-8") as fout:
    uic.compileUi("murettebat.ui", fout)