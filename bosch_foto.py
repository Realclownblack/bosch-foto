import os.path

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog
import shutil
import getpass

import matplotlib.pyplot as plt
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean


class bosch_foto():
    def __init__(self):
        self.button_edit = True
        self.nameFoto = ''
        self.besePathSeve = f'C:/Users/{getpass.getuser()}/Desktop'
        self.besePath = f'cache/img-edit'
        self.besePathBackup = f'cache/img-edit/backup-img'
        self.initial()


    def initial(self):
        self.bosch_foto_initial = uic.loadUi('screen/screen_bosch_foto.ui')
        self.bosch_foto_initial.show()
        self.fuction()

    def fuction(self):
        self.bosch_foto_initial.UPLOAD.clicked.connect(self.foto_abrir)
        self.bosch_foto_initial.SEVE.clicked.connect(self.seve_foto)


    def foto_abrir(self):
        self.arquivo = QFileDialog.getOpenFileName()[0]
        shutil.copy2(self.arquivo,self.besePath)
        self.nameFoto = os.path.basename(self.arquivo)
        shutil.copy2(f'{self.besePath}/{self.nameFoto}',self.besePathBackup)
        self.time = QTimer()
        self.time.start(100)
        self.time.timeout.connect(lambda: self.treds_upload())


    def treds_upload(self):
        self.bosch_foto_initial.IMG_2.setIcon(QIcon(f'{self.arquivo}'))
        self.bosch_foto_initial.IMG.setIcon(QIcon(f'{self.besePath}/{self.nameFoto}'))

    def seve_foto(self):
        shutil.copy2(f'{self.besePathBackup}/{self.nameEditfoto}',self.besePathSeve)


