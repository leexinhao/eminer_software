'''
点击按钮出现的提示窗口
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Ui_T_message_dialog import Ui_message_dialog


class T_message_dialog(QtWidgets.QDialog, Ui_message_dialog):
    def __init__(self, parent,title, message):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(title)
        self.T_message_label.setText(message)
    def setMessage(self, message):
        self.T_message_label.setText(message)
