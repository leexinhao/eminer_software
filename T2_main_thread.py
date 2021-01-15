from T2_codes.T2_code.T2_draw import *
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
class T2_main_thread1(QtCore.QThread):

    def __init__(self, city, usertype, parent=None):
        super(T2_main_thread1, self).__init__(parent)
        self.city = city
        self.usertype = usertype

    def __del__(self):
        self.wait()

    def run(self):
        T2draw1(self.city, self.usertype)


class T2_main_thread2(QtCore.QThread):

    def __init__(self, cons, parent=None):
        super(T2_main_thread2, self).__init__(parent)
        self.cons = cons

    def __del__(self):
        self.wait()

    def run(self):
        T2draw2(self.cons) 
