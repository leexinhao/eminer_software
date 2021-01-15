'''
点击图片标签后弹出的放大窗口
'''
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Ui_T_image_dialog import Ui_image_dialog


class T_image_dialog(QtWidgets.QDialog, Ui_image_dialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.T1_dialog_label.setVisible(False)

    def show_label(self, picture):
        self.T1_dialog_label.setVisible(True)
        self.T1_dialog_label.setPixmap(picture)
        self.T1_dialog_label.setScaledContents(True)
    def on_T1_save_button_released(self):
        fileName, ok = QFileDialog.getSaveFileName(self,
                                                   "文件保存",
                                                   "/result",
                                                   "jpg Files (*.png);;png Files (*.jpg")
        if fileName == '':
            return

        if ok[0] == 'p':
            self.T1_dialog_label.pixmap().save(fileName, 'PNG')
        else:
            self.T1_dialog_label.pixmap().save(fileName, 'JPG')
        
