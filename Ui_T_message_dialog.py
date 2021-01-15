# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dell\Desktop\尝试\eminer_software_release\T_message_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_message_dialog(object):
    def setupUi(self, message_dialog):
        message_dialog.setObjectName("message_dialog")
        message_dialog.resize(547, 363)
        message_dialog.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T_message_label = QtWidgets.QLabel(message_dialog)
        self.T_message_label.setGeometry(QtCore.QRect(20, 30, 521, 291))
        self.T_message_label.setStyleSheet("background:transparent;\n"
"color:white;")
        self.T_message_label.setText("")
        self.T_message_label.setObjectName("T_message_label")

        self.retranslateUi(message_dialog)
        QtCore.QMetaObject.connectSlotsByName(message_dialog)

    def retranslateUi(self, message_dialog):
        _translate = QtCore.QCoreApplication.translate
        message_dialog.setWindowTitle(_translate("message_dialog", "友情提醒！！！"))
