# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'murettebat.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 676)
        MainWindow.setStyleSheet("#centralwidget{\n"
"background-color: qconicalgradient(cx:1, cy:0.262, angle:218.5, stop:0 rgba(206, 0, 0, 166), stop:1 rgba(0, 0, 0, 0));\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(240, 300, 801, 321))
        self.tableWidget.setRowCount(30)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.btnListele = QtWidgets.QPushButton(self.centralwidget)
        self.btnListele.setGeometry(QtCore.QRect(870, 270, 171, 28))
        self.btnListele.setObjectName("btnListele")
        self.lneName = QtWidgets.QLineEdit(self.centralwidget)
        self.lneName.setGeometry(QtCore.QRect(160, 60, 151, 31))
        self.lneName.setObjectName("lneName")
        self.lneSoyisim = QtWidgets.QLineEdit(self.centralwidget)
        self.lneSoyisim.setGeometry(QtCore.QRect(160, 100, 151, 31))
        self.lneSoyisim.setObjectName("lneSoyisim")
        self.lneRutbe = QtWidgets.QLineEdit(self.centralwidget)
        self.lneRutbe.setGeometry(QtCore.QRect(160, 140, 151, 31))
        self.lneRutbe.setObjectName("lneRutbe")
        self.lneBoluk = QtWidgets.QLineEdit(self.centralwidget)
        self.lneBoluk.setGeometry(QtCore.QRect(160, 180, 151, 31))
        self.lneBoluk.setObjectName("lneBoluk")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 91, 40))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 91, 40))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 91, 40))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 91, 40))
        self.label_4.setObjectName("label_4")
        self.btnEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnEkle.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.btnEkle.setObjectName("btnEkle")
        self.btnSil = QtWidgets.QPushButton(self.centralwidget)
        self.btnSil.setGeometry(QtCore.QRect(310, 240, 93, 28))
        self.btnSil.setObjectName("btnSil")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 50, 111, 16))
        self.label_5.setObjectName("label_5")
        self.lneWrite = QtWidgets.QLineEdit(self.centralwidget)
        self.lneWrite.setGeometry(QtCore.QRect(890, 40, 351, 41))
        self.lneWrite.setObjectName("lneWrite")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnListele.setText(_translate("MainWindow", "Mürettebat Listeleme"))
        self.label.setText(_translate("MainWindow", "İSİM"))
        self.label_2.setText(_translate("MainWindow", "Soyisim"))
        self.label_3.setText(_translate("MainWindow", "Rütbe"))
        self.label_4.setText(_translate("MainWindow", "Bölük"))
        self.btnEkle.setText(_translate("MainWindow", "EKLE"))
        self.btnSil.setText(_translate("MainWindow", "Sil"))
        self.label_5.setText(_translate("MainWindow", "Mühimmat Kodu"))
