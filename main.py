
import sys
from PyQt5 import QtWidgets

from bosch_foto import bosch_foto
def main ():
    app = QtWidgets.QApplication(sys.argv)
    foto = bosch_foto()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()