# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'muhimmat_Ekle.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 746)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-color: qconicalgradient(cx:0.886, cy:0.516682, angle:185.8, stop:0 rgba(0, 206, 23, 166), stop:1 rgba(0, 0, 0, 0));\n"
"background-color: qconicalgradient(cx:1, cy:0.398, angle:225.4, stop:0 rgba(0, 206, 23, 166), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(820, 60, 251, 16))
        self.label_5.setObjectName("label_5")
        self.cmbMarka = QtWidgets.QComboBox(self.centralwidget)
        self.cmbMarka.setGeometry(QtCore.QRect(400, 80, 111, 31))
        self.cmbMarka.setObjectName("cmbMarka")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbMarka.addItem("")
        self.cmbKategori = QtWidgets.QComboBox(self.centralwidget)
        self.cmbKategori.setGeometry(QtCore.QRect(590, 80, 111, 31))
        self.cmbKategori.setObjectName("cmbKategori")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 50, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 50, 131, 16))
        self.label_7.setObjectName("label_7")
        self.lneurunAciklama = QtWidgets.QLineEdit(self.centralwidget)
        self.lneurunAciklama.setGeometry(QtCore.QRect(820, 80, 391, 141))
        self.lneurunAciklama.setObjectName("lneurunAciklama")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(130, 370, 921, 321))
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.cmbKategoriListele = QtWidgets.QComboBox(self.centralwidget)
        self.cmbKategoriListele.setGeometry(QtCore.QRect(920, 290, 131, 31))
        self.cmbKategoriListele.setObjectName("cmbKategoriListele")
        self.cmbKategoriListele.addItem("")
        self.cmbKategoriListele.addItem("")
        self.cmbKategoriListele.addItem("")
        self.cmbKategoriListele.addItem("")
        self.cmbKategoriListele.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(760, 290, 181, 22))
        self.label_8.setObjectName("label_8")
        self.btnEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnEkle.setGeometry(QtCore.QRect(390, 230, 171, 28))
        self.btnEkle.setObjectName("btnEkle")
        self.btnSil = QtWidgets.QPushButton(self.centralwidget)
        self.btnSil.setGeometry(QtCore.QRect(390, 150, 171, 28))
        self.btnSil.setObjectName("btnSil")
        self.btnGuncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuncelle.setGeometry(QtCore.QRect(390, 190, 171, 28))
        self.btnGuncelle.setObjectName("btnGuncelle")
        self.btnListele = QtWidgets.QPushButton(self.centralwidget)
        self.btnListele.setGeometry(QtCore.QRect(130, 340, 171, 28))
        self.btnListele.setObjectName("btnListele")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 40, 93, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.btnKategoriyeGoreListele = QtWidgets.QPushButton(self.centralwidget)
        self.btnKategoriyeGoreListele.setGeometry(QtCore.QRect(900, 330, 151, 31))
        self.btnKategoriyeGoreListele.setObjectName("btnKategoriyeGoreListele")
        self.lnestokMiktari = QtWidgets.QLineEdit(self.centralwidget)
        self.lnestokMiktari.setGeometry(QtCore.QRect(210, 190, 151, 31))
        self.lnestokMiktari.setObjectName("lnestokMiktari")
        self.lneurunAdi = QtWidgets.QLineEdit(self.centralwidget)
        self.lneurunAdi.setGeometry(QtCore.QRect(210, 90, 151, 31))
        self.lneurunAdi.setObjectName("lneurunAdi")
        self.lneurunKodu = QtWidgets.QLineEdit(self.centralwidget)
        self.lneurunKodu.setGeometry(QtCore.QRect(210, 50, 151, 31))
        self.lneurunKodu.setObjectName("lneurunKodu")
        self.lnebirimFiyat = QtWidgets.QLineEdit(self.centralwidget)
        self.lnebirimFiyat.setGeometry(QtCore.QRect(210, 140, 151, 31))
        self.lnebirimFiyat.setObjectName("lnebirimFiyat")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 350, 55, 16))
        self.label_9.setObjectName("label_9")
        self.btnMuhimmatAra = QtWidgets.QPushButton(self.centralwidget)
        self.btnMuhimmatAra.setGeometry(QtCore.QRect(270, 230, 93, 28))
        self.btnMuhimmatAra.setObjectName("btnMuhimmatAra")
        self.btnmurettebat = QtWidgets.QPushButton(self.centralwidget)
        self.btnmurettebat.setGeometry(QtCore.QRect(1090, 610, 93, 28))
        self.btnmurettebat.setObjectName("btnmurettebat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1218, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmbMarka.setCurrentIndex(-1)
        self.cmbKategori.setCurrentIndex(-1)
        self.cmbKategoriListele.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Mühimmat açıklaması"))
        self.cmbMarka.setItemText(0, _translate("MainWindow", "Leopar2A4"))
        self.cmbMarka.setItemText(1, _translate("MainWindow", "Leopar2A6"))
        self.cmbMarka.setItemText(2, _translate("MainWindow", "Tiger2"))
        self.cmbMarka.setItemText(3, _translate("MainWindow", "Stug"))
        self.cmbMarka.setItemText(4, _translate("MainWindow", "T-34"))
        self.cmbKategori.setItemText(0, _translate("MainWindow", "Zırh Delici"))
        self.cmbKategori.setItemText(1, _translate("MainWindow", "Patlayıcı Mermiler"))
        self.cmbKategori.setItemText(2, _translate("MainWindow", "Yanıcı Mermiler"))
        self.cmbKategori.setItemText(3, _translate("MainWindow", "Gözetleme Mermisi"))
        self.cmbKategori.setItemText(4, _translate("MainWindow", "Füze Mermileri"))
        self.label_6.setText(_translate("MainWindow", "Tank Markası"))
        self.label_7.setText(_translate("MainWindow", "Mühimmat Katogorisi"))
        self.cmbKategoriListele.setItemText(0, _translate("MainWindow", "Zırh Delici"))
        self.cmbKategoriListele.setItemText(1, _translate("MainWindow", "Gözetleme Mermisi"))
        self.cmbKategoriListele.setItemText(2, _translate("MainWindow", "Füze Mermileri"))
        self.cmbKategoriListele.setItemText(3, _translate("MainWindow", "Yanıcı Mermiler"))
        self.cmbKategoriListele.setItemText(4, _translate("MainWindow", "Patlayıcı Mermiler"))
        self.label_8.setText(_translate("MainWindow", "Katogoriye Göre Listele"))
        self.btnEkle.setText(_translate("MainWindow", "Mühimmat Ekle"))
        self.btnSil.setText(_translate("MainWindow", "Mühimmat  Sil"))
        self.btnGuncelle.setText(_translate("MainWindow", "Muhimmat Güncelleme"))
        self.btnListele.setText(_translate("MainWindow", "Mühimmat Listeleme"))
        self.label.setText(_translate("MainWindow", "Mühimmat kodu"))
        self.label_2.setText(_translate("MainWindow", "Mühimmat adı"))
        self.label_3.setText(_translate("MainWindow", "Birim fiyatı"))
        self.label_4.setText(_translate("MainWindow", "stok miktarı"))
        self.btnKategoriyeGoreListele.setText(_translate("MainWindow", "Kategoriye Göre Listele"))
        self.label_9.setText(_translate("MainWindow", "LİSTE"))
        self.btnMuhimmatAra.setText(_translate("MainWindow", "Ara"))
        self.btnmurettebat.setText(_translate("MainWindow", "Murettebat"))
