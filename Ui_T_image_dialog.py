# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dell\Desktop\eminer_software\T_image_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_image_dialog(object):
    def setupUi(self, image_dialog):
        image_dialog.setObjectName("image_dialog")
        image_dialog.resize(780, 580)
        image_dialog.setMinimumSize(QtCore.QSize(780, 580))
        image_dialog.setMaximumSize(QtCore.QSize(780, 580))
        image_dialog.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T1_dialog_label = QtWidgets.QLabel(image_dialog)
        self.T1_dialog_label.setGeometry(QtCore.QRect(0, 0, 771, 571))
        self.T1_dialog_label.setStyleSheet("background:transparent;")
        self.T1_dialog_label.setText("")
        self.T1_dialog_label.setObjectName("T1_dialog_label")
        self.T1_save_button = QtWidgets.QPushButton(image_dialog)
        self.T1_save_button.setGeometry(QtCore.QRect(660, 10, 101, 31))
        self.T1_save_button.setStyleSheet("border-image:url(:/imagine/edata_of_pictures/heianjian.jpg);\n"
"border-radius:10px;\n"
"font: 25 11pt \"微软雅黑\";\n"
"color:white;")
        self.T1_save_button.setObjectName("T1_save_button")

        self.retranslateUi(image_dialog)
        QtCore.QMetaObject.connectSlotsByName(image_dialog)

    def retranslateUi(self, image_dialog):
        _translate = QtCore.QCoreApplication.translate
        image_dialog.setWindowTitle(_translate("image_dialog", "用户日用电量变化曲线"))
        self.T1_save_button.setText(_translate("image_dialog", "保存结果"))
import myResource_rc
