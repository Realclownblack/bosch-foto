from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic.properties import QtGui


class bosch_foto():
    def __init__(self):
        self.button_edit = True
        self.initial()


    def initial(self):
        self.bosch_foto_initial = uic.loadUi('screen/screen_bosch_foto.ui')
        self.bosch_foto_initial.show()
        self.fuction()

    def fuction(self):
        self.bosch_foto_initial.UPLOAD.clicked.connect(self.foto_abrir)

        self.bosch_foto_initial.EDITAR.clicked.connect(
            lambda: self.bosch_foto_initial.stackedWidget.setCurrentWidget(
                self.bosch_foto_initial.SCREEN_BUTON))




    def foto_abrir(self):
        self.arquivo = QFileDialog.getOpenFileName()[0]
        print(self.arquivo)
        self.time = QTimer()
        self.time.start(100)
        self.time.timeout.connect(lambda: self.treds_upload())


    def treds_upload(self):
        self.bosch_foto_initial.IMG.setIcon(QIcon(f'{self.arquivo}'))



