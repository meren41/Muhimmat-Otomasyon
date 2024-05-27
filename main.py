import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Muhimmat_Ekle import*
from Murettebat_Ekle import*

uygulama = QApplication(sys.argv)
pencere = QMainWindow() 
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

murettebat=QMainWindow()
Ui2=Ui_MainWindow2()
Ui2.setupUi(murettebat)



# Veritabanı işlemleri 
import sqlite3

baglanti = sqlite3.connect("muhimmat.db")
islem = baglanti.cursor()
baglanti.commit()


table = islem.execute("create table if not exists muhimmat( urunKodu int, urunAdi text, birimFiyat int,  stokMiktari int, urunAciklaması text, marka text, kategori text )")
baglanti.commit()

def kayit_ekle():
    UrunKodu = int(ui.lneurunKodu.text()) #Mühimmat kodu
    UrunAdi = ui.lneurunAdi.text()#Mühimmat adı
    BirimFiyat = int(ui.lnebirimFiyat.text())
    StokMiktari = int(ui.lnestokMiktari.text())
    UrunAciklama = ui.lneurunAciklama.text()
    Marka = ui.cmbMarka.currentText()#Tank markası
    Kategori = ui.cmbKategori.currentText()#Mühimmat kategori

    try:
        ekle = "insert into muhimmat(urunKodu,urunAdi,birimFiyat,stokMiktari,urunAciklaması,marka,kategori) values(?,?,?,?,?,?,?)"
        islem.execute(ekle,(UrunKodu,UrunAdi,BirimFiyat,StokMiktari,UrunAciklama,Marka,Kategori))
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Ekleme işlemi Başarılı",1000)
    except Exception as error:
        ui.statusbar.showMessage("Kayit Eklenemedi Hata Çıktı === " +str(error))

def kayit_listele():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("Mühimmat Kodu","Mühimmat Adi","Birim Fiyatı","Stok Miktarı","mühimmat Açıklama","TANK Markası","Kategori"))
    ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents,)

    sorgu ="select* from muhimmat"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))


def kategoriye_gore_listele():
    listelenecek_kategori = ui.cmbKategoriListele.currentText()

    sorgu = "select * from muhimmat where kategori = ?"
    islem.execute(sorgu,(listelenecek_kategori,))
    ui.tableWidget.clear()
    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))
            ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents,)

def kayit_sil():
    sil_mesaj = QMessageBox.question(pencere,"Silme Onayı","Silmek İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = ui.tableWidget.selectedItems()
        silinecek_kayit = secilen_kayit[0].text()

        sorgu = "delete from muhimmat where urunKodu = ?"
        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            ui.statusbar.showMessage("Kayıt Başarıyla Silindi")
            kayit_listele()
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Silinirken Hata Çıktı === "+str(error))
    
    else:
        ui.statusbar.showMessage("Silme İşlemi İptal Edildi")

def kayit_guncelle():
    guncelle_mesaj = QMessageBox.question(pencere,"Güncelleme Onayı","Bu kaydı Güncellemek istediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No)

    if guncelle_mesaj == QMessageBox.Yes:
        try:
            UrunKodu = ui.lneurunKodu.text()
            UrunAdi = ui.lneurunAdi.text()
            BirimFiyati = ui.lnebirimFiyat.text()
            StokMiktari = ui.lnestokMiktari.text()
            UrunAciklama = ui.lneurunAciklama.text()
            Marka = ui.cmbMarka.currentText()
            Kategori = ui.cmbKategori.currentText()

            if UrunAdi == "" and BirimFiyati == "" and StokMiktari == "" and UrunAciklama == "" and Marka == "":
                islem.execute("update muhimmat set kategori = ? where urunKodu = ?",(Kategori,UrunKodu))

            elif UrunAdi == "" and BirimFiyati == "" and StokMiktari == "" and UrunAciklama == "" and Kategori == "":
                islem.execute("update muhimmat set marka = ? where urunKodu = ?",(Marka,UrunKodu)) 

            elif UrunAdi == "" and BirimFiyati == "" and StokMiktari == "" and Marka == "" and Kategori == "":
                islem.execute("update muhimmat set urunAciklaması = ? where urunKodu = ?",(UrunAciklama,UrunKodu))

            elif UrunAdi == "" and BirimFiyati == "" and UrunAciklama == "" and Marka == "" and Kategori == "":
                islem.execute("update muhimmat set stokMiktari = ? where urunKodu = ?",(StokMiktari,UrunKodu))

            elif UrunAdi == "" and StokMiktari == "" and UrunAciklama == "" and Marka == "" and Kategori == "":
                islem.execute("update muhimmat set birimFiyat = ? where urunKodu = ?",(BirimFiyati,UrunKodu))

            elif BirimFiyati == "" and StokMiktari == "" and UrunAciklama == "" and Marka == "" and Kategori == "":
                islem.execute("update muhimmat set urunAdi = ? where urunKodu = ?",(UrunAdi,UrunKodu))
            else:
                islem.execute("update muhimmat set urunAdi = ?, birimFiyat = ? , stokMiktari = ?, urunAciklaması = ?, marka = ?, kategori = ? where urunKodu = ?",(UrunAdi,BirimFiyati,StokMiktari,UrunAciklama,Marka, Kategori,UrunKodu))
            baglanti.commit()
            kayit_listele()
            ui.statusbar.showMessage("Kayıt Başarıyla Güncellendi")
        except Exception as error:
            ui.statusbar.showMessage("Kayıt Güncellemede Hata Çıktı === "+str(error))
    else:
        ui.statusbar.showMessage("Güncelleme İptal Edildi")
    kayit_listele()
def KAYIT_ARA():
    aranan1=ui.lneurunKodu.text()
    aranan2=ui.lnestokMiktari.text()
    aranan3=ui.lnebirimFiyat.text()
    aranan4=ui.lneurunAdi.text()
    islem.execute("SELECT * FROM muhimmat WHERE urunKodu=? OR stokMiktari=? OR birimFiyat=?  OR urunAdi=?", \
                 (aranan1,aranan2,aranan3,aranan4,))
    baglanti.commit()
    ui.tableWidget.clear()
    for satirIndeks,satirVeri in enumerate(islem): #tablewidget içerisine dönen sorgu yerleşir
        for sutunIndeks,sutunVeri in enumerate(satirVeri):
            ui.tableWidget.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))

def giriş():
    murettebat.show()

#......................................................................................................................................................#

# Veritabanı işlemleri 

baglanti = sqlite3.connect("muhimmat.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists murettebat( Name text, Soyisim text, Rutbe text, Boluk int)")
baglanti.commit()

def kayit2_ekle():
    UrunKodu2 = Ui2.lneName.text()
    UrunAdi2 = Ui2.lneSoyisim.text()
    BirimFiyat2 = Ui2.lneRutbe.text()
    UrunAciklama2 = int(Ui2.lneBoluk.text())

    try:
        ekle = "insert into murettebat( Name,Soyisim,Rutbe,Boluk) values(?,?,?,?)"
        islem.execute(ekle,(UrunKodu2,UrunAdi2,BirimFiyat2,UrunAciklama2))
        baglanti.commit()
        Ui2.statusbar.showMessage("Kayıt Ekleme işlemi Başarılı",1000)
    except Exception as error:
        Ui2.statusbar.showMessage("Kayit Eklenemedi Hata Çıktı === " +str(error))

def kayit2_listele():
    Ui2.tableWidget.clear()
    Ui2.tableWidget.setHorizontalHeaderLabels(("İsim","Soyisim ","Rütbe","Bölük"))
    Ui2.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents,)

    sorgu ="select* from murettebat"
    islem.execute(sorgu)

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            Ui2.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kayit2_sil():
    sil_mesaj = QMessageBox.question(pencere,"Silme Onayı","Silmek İstediğinizden Emin Misiniz ?",QMessageBox.Yes | QMessageBox.No)

    if sil_mesaj == QMessageBox.Yes:
        secilen_kayit = Ui2.tableWidget.selectedItems()
        silinecek_kayit = secilen_kayit[0].text()

        sorgu = "delete from muhimmat where urunKodu = ?"
        try:
            islem.execute(sorgu,(silinecek_kayit,))
            baglanti.commit()
            Ui2.statusbar.showMessage("Kayıt Başarıyla Silindi")
            kayit_listele()
        except Exception as error:
            Ui2.statusbar.showMessage("Kayıt Silinirken Hata Çıktı === "+str(error))
    
    else:
        Ui2.statusbar.showMessage("Silme İşlemi İptal Edildi")

# butonlar 
ui.btnEkle.clicked.connect(kayit_ekle)
ui.btnListele.clicked.connect(kayit_listele)
ui.btnGuncelle.clicked.connect(kayit_guncelle)
ui.btnSil.clicked.connect(kayit_sil)
ui.btnKategoriyeGoreListele.clicked.connect(kategoriye_gore_listele)
ui.btnMuhimmatAra.clicked.connect(KAYIT_ARA)
ui.btnmurettebat.clicked.connect(giriş)
Ui2.btnEkle.clicked.connect(kayit_ekle)
Ui2.btnListele.clicked.connect(kayit_listele)
Ui2.btnSil.clicked.connect(kayit_sil)

sys.exit(uygulama.exec_())



