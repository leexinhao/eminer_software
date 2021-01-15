import sys
from PyQt5 import QtWidgets, QtCore
import MainWidget
app = QtWidgets.QApplication(sys.argv)

mw = MainWidget.MainWidget()
mw.show()

sys.exit(app.exec_())
        
