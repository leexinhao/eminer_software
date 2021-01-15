from PyQt5 import QtCore, QtGui, QtWidgets
from T_image_dialog import *

'''
重写label使其响应点击事件
'''


class MyLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)
        self.parent = parent

    def mousePressEvent(self, e):
        image_dialog = T_image_dialog(self.parent)
        image_dialog.show_label(self.pixmap())
        image_dialog.exec_()
