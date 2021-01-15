# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\dell\Desktop\尝试\eminer_software_release\MainWindow_e_Miner.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1650, 870)
        MainWindow.setMinimumSize(QtCore.QSize(1650, 870))
        MainWindow.setMaximumSize(QtCore.QSize(1650, 870))
        MainWindow.setSizeIncrement(QtCore.QSize(1650, 870))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagine/Lightning.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(32, 48))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"background-image: url(:/imagine/edata_of_pictures/heibeijing.jpg);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.eminer_buttonWidget = QtWidgets.QWidget(self.centralwidget)
        self.eminer_buttonWidget.setGeometry(QtCore.QRect(50, 10, 1631, 41))
        self.eminer_buttonWidget.setStyleSheet("")
        self.eminer_buttonWidget.setObjectName("eminer_buttonWidget")
        self.T_uploadfile_button = QtWidgets.QPushButton(self.eminer_buttonWidget)
        self.T_uploadfile_button.setEnabled(True)
        self.T_uploadfile_button.setGeometry(QtCore.QRect(1110, 10, 211, 31))
        self.T_uploadfile_button.setStyleSheet("border-image:url(:/imagine/edata_of_pictures/heibeijing.jpg);\n"
"font: 9pt \"微软雅黑\";\n"
"border-radius:10px;\n"
"color:white;\n"
"")
        self.T_uploadfile_button.setObjectName("T_uploadfile_button")
        self.T_help_button = QtWidgets.QPushButton(self.eminer_buttonWidget)
        self.T_help_button.setGeometry(QtCore.QRect(1340, 10, 211, 31))
        self.T_help_button.setStyleSheet("border-image:url(:/imagine/edata_of_pictures/heibeijing.jpg);\n"
"font: 9pt \"微软雅黑\";\n"
"border-radius:10px;\n"
"color:white;")
        self.T_help_button.setObjectName("T_help_button")
        self.T_explain_label = QtWidgets.QLabel(self.eminer_buttonWidget)
        self.T_explain_label.setGeometry(QtCore.QRect(0, 0, 1071, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.T_explain_label.setFont(font)
        self.T_explain_label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"")
        self.T_explain_label.setScaledContents(True)
        self.T_explain_label.setObjectName("T_explain_label")
        self.eminer_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.eminer_tabWidget.setGeometry(QtCore.QRect(30, 40, 1600, 800))
        self.eminer_tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.eminer_tabWidget.setMaximumSize(QtCore.QSize(14000, 8000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.eminer_tabWidget.setPalette(palette)
        self.eminer_tabWidget.setAutoFillBackground(False)
        self.eminer_tabWidget.setStyleSheet("QTabBar::tab{border-image:url(:/imagine/edata_of_pictures/heibeijing.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"微软雅黑\";\n"
"width：1000;\n"
"height:30;\n"
"border-width:5xp;\n"
"}\n"
"QTabWidget::pane\n"
"{\n"
"border-left-color: rgba(255, 255, 255, 50);\n"
"border-right-color: rgba(255, 255, 255, 50);\n"
"border-top-color: rgba(255, 255, 255, 50);\n"
"border-bottom-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.eminer_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.eminer_tabWidget.setIconSize(QtCore.QSize(16, 14))
        self.eminer_tabWidget.setUsesScrollButtons(True)
        self.eminer_tabWidget.setDocumentMode(False)
        self.eminer_tabWidget.setTabsClosable(False)
        self.eminer_tabWidget.setMovable(False)
        self.eminer_tabWidget.setTabBarAutoHide(False)
        self.eminer_tabWidget.setObjectName("eminer_tabWidget")
        self.T0_tab = QtWidgets.QWidget()
        self.T0_tab.setStyleSheet("#T0_tab{\n"
"border-image: url(:/imagine/edata_of_pictures/heikejibeijing.jpg);\n"
"}")
        self.T0_tab.setObjectName("T0_tab")
        self.T0_map_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T0_tab)
        self.T0_map_webEngineView.setGeometry(QtCore.QRect(60, 0, 1161, 661))
        self.T0_map_webEngineView.setStyleSheet("background:transparent;")
        self.T0_map_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/201901T0_map.html"))
        self.T0_map_webEngineView.setObjectName("T0_map_webEngineView")
        self.T0_pie_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T0_tab)
        self.T0_pie_webEngineView.setGeometry(QtCore.QRect(20, 30, 491, 431))
        self.T0_pie_webEngineView.setStyleSheet("background:transparent;")
        self.T0_pie_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/201901T0_pie1.html"))
        self.T0_pie_webEngineView.setObjectName("T0_pie_webEngineView")
        self.T0_funnel_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T0_tab)
        self.T0_funnel_webEngineView.setGeometry(QtCore.QRect(1040, 10, 541, 421))
        self.T0_funnel_webEngineView.setStyleSheet("background:transparent;")
        self.T0_funnel_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/201901T0_funnel.html"))
        self.T0_funnel_webEngineView.setObjectName("T0_funnel_webEngineView")
        self.T0_bar1_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T0_tab)
        self.T0_bar1_webEngineView.setGeometry(QtCore.QRect(10, 360, 521, 431))
        self.T0_bar1_webEngineView.setStyleSheet("background:transparent;")
        self.T0_bar1_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/201901T0_bar1.html"))
        self.T0_bar1_webEngineView.setObjectName("T0_bar1_webEngineView")
        self.T0_bar2_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T0_tab)
        self.T0_bar2_webEngineView.setGeometry(QtCore.QRect(1020, 350, 561, 431))
        self.T0_bar2_webEngineView.setStyleSheet("background:transparent;")
        self.T0_bar2_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/201901T0_bar2.html"))
        self.T0_bar2_webEngineView.setObjectName("T0_bar2_webEngineView")
        self.T0_month_comboBox = QtWidgets.QComboBox(self.T0_tab)
        self.T0_month_comboBox.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.T0_month_comboBox.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 10pt \"微软雅黑\";")
        self.T0_month_comboBox.setObjectName("T0_month_comboBox")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_month_comboBox.addItem("")
        self.T0_funnel_webEngineView.raise_()
        self.T0_bar2_webEngineView.raise_()
        self.T0_map_webEngineView.raise_()
        self.T0_pie_webEngineView.raise_()
        self.T0_bar1_webEngineView.raise_()
        self.T0_month_comboBox.raise_()
        self.eminer_tabWidget.addTab(self.T0_tab, "")
        self.T1_tab = QtWidgets.QWidget()
        self.T1_tab.setStyleSheet("#T1_tab{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.T1_tab.setObjectName("T1_tab")
        self.T1_image_label2 = MyLabel(self.T1_tab)
        self.T1_image_label2.setGeometry(QtCore.QRect(1150, 146, 345, 175))
        self.T1_image_label2.setMinimumSize(QtCore.QSize(345, 175))
        self.T1_image_label2.setMaximumSize(QtCore.QSize(345, 175))
        self.T1_image_label2.setStyleSheet("")
        self.T1_image_label2.setText("")
        self.T1_image_label2.setObjectName("T1_image_label2")
        self.T1_image_label3 = MyLabel(self.T1_tab)
        self.T1_image_label3.setGeometry(QtCore.QRect(798, 353, 345, 175))
        self.T1_image_label3.setMinimumSize(QtCore.QSize(345, 175))
        self.T1_image_label3.setMaximumSize(QtCore.QSize(345, 175))
        self.T1_image_label3.setStyleSheet("")
        self.T1_image_label3.setText("")
        self.T1_image_label3.setObjectName("T1_image_label3")
        self.T1_image_label4 = MyLabel(self.T1_tab)
        self.T1_image_label4.setGeometry(QtCore.QRect(1150, 353, 345, 175))
        self.T1_image_label4.setMinimumSize(QtCore.QSize(345, 175))
        self.T1_image_label4.setMaximumSize(QtCore.QSize(345, 175))
        self.T1_image_label4.setStyleSheet("")
        self.T1_image_label4.setText("")
        self.T1_image_label4.setObjectName("T1_image_label4")
        self.T1_image_label5 = MyLabel(self.T1_tab)
        self.T1_image_label5.setGeometry(QtCore.QRect(798, 560, 345, 175))
        self.T1_image_label5.setMinimumSize(QtCore.QSize(345, 175))
        self.T1_image_label5.setMaximumSize(QtCore.QSize(345, 175))
        self.T1_image_label5.setStyleSheet("")
        self.T1_image_label5.setText("")
        self.T1_image_label5.setObjectName("T1_image_label5")
        self.T1_image_label6 = MyLabel(self.T1_tab)
        self.T1_image_label6.setGeometry(QtCore.QRect(1150, 560, 345, 175))
        self.T1_image_label6.setMinimumSize(QtCore.QSize(345, 175))
        self.T1_image_label6.setMaximumSize(QtCore.QSize(345, 175))
        self.T1_image_label6.setStyleSheet("")
        self.T1_image_label6.setText("")
        self.T1_image_label6.setObjectName("T1_image_label6")
        self.T1_image_label1 = MyLabel(self.T1_tab)
        self.T1_image_label1.setGeometry(QtCore.QRect(798, 146, 345, 175))
        self.T1_image_label1.setMinimumSize(QtCore.QSize(345, 175))
        self.T1_image_label1.setMaximumSize(QtCore.QSize(345, 175))
        self.T1_image_label1.setStyleSheet("")
        self.T1_image_label1.setText("")
        self.T1_image_label1.setObjectName("T1_image_label1")
        self.T1_tableWidget = QtWidgets.QTableWidget(self.T1_tab)
        self.T1_tableWidget.setGeometry(QtCore.QRect(150, 470, 491, 271))
        self.T1_tableWidget.setStyleSheet("")
        self.T1_tableWidget.setAutoScroll(True)
        self.T1_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.T1_tableWidget.setShowGrid(True)
        self.T1_tableWidget.setObjectName("T1_tableWidget")
        self.T1_tableWidget.setColumnCount(3)
        self.T1_tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.T1_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.T1_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.T1_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.T1_tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.T1_tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.T1_tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.T1_tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.T1_tableWidget.setItem(5, 2, item)
        self.T1_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.T1_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.T1_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.T1_tableWidget.verticalHeader().setVisible(False)
        self.T1_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.T1_tableWidget.verticalHeader().setHighlightSections(True)
        self.T1_tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.T1_tableWidget.verticalHeader().setStretchLastSection(False)
        self.T1_graphicsView = PlotWidget(self.T1_tab)
        self.T1_graphicsView.setGeometry(QtCore.QRect(110, 110, 561, 341))
        self.T1_graphicsView.setStyleSheet("background:transparent;")
        self.T1_graphicsView.setObjectName("T1_graphicsView")
        self.layoutWidget = QtWidgets.QWidget(self.T1_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 0, 1451, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.T1_usertype_label = QtWidgets.QLabel(self.layoutWidget)
        self.T1_usertype_label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 10pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T1_usertype_label.setObjectName("T1_usertype_label")
        self.horizontalLayout.addWidget(self.T1_usertype_label)
        self.T1_usertype_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.T1_usertype_comboBox.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 10pt \"微软雅黑\";")
        self.T1_usertype_comboBox.setObjectName("T1_usertype_comboBox")
        self.T1_usertype_comboBox.addItem("")
        self.T1_usertype_comboBox.addItem("")
        self.T1_usertype_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.T1_usertype_comboBox)
        self.T1_city_label = QtWidgets.QLabel(self.layoutWidget)
        self.T1_city_label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 9pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T1_city_label.setObjectName("T1_city_label")
        self.horizontalLayout.addWidget(self.T1_city_label)
        self.T1_city_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.T1_city_comboBox.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 10pt \"微软雅黑\";")
        self.T1_city_comboBox.setObjectName("T1_city_comboBox")
        self.T1_city_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.T1_city_comboBox)
        self.T1_end_label = QtWidgets.QLabel(self.layoutWidget)
        self.T1_end_label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 9pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T1_end_label.setObjectName("T1_end_label")
        self.horizontalLayout.addWidget(self.T1_end_label)
        self.T1_start_dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.T1_start_dateEdit.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"color: rgb(0, 0, 127);\n"
"border-radius:5px;\n"
"font: 10pt \"微软雅黑\";")
        self.T1_start_dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 18), QtCore.QTime(23, 59, 59)))
        self.T1_start_dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 1), QtCore.QTime(0, 0, 0)))
        self.T1_start_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.T1_start_dateEdit.setCalendarPopup(True)
        self.T1_start_dateEdit.setCurrentSectionIndex(2)
        self.T1_start_dateEdit.setObjectName("T1_start_dateEdit")
        self.horizontalLayout.addWidget(self.T1_start_dateEdit)
        self.T1_start_label = QtWidgets.QLabel(self.layoutWidget)
        self.T1_start_label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 9pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T1_start_label.setObjectName("T1_start_label")
        self.horizontalLayout.addWidget(self.T1_start_label)
        self.T1_end_dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.T1_end_dateEdit.setStyleSheet("color: rgb(0, 0, 127);\n"
"border-radius:5px;\n"
"background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"font: 10pt \"微软雅黑\";")
        self.T1_end_dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 30), QtCore.QTime(23, 59, 59)))
        self.T1_end_dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2018, 4, 14), QtCore.QTime(0, 0, 0)))
        self.T1_end_dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.T1_end_dateEdit.setCalendarPopup(True)
        self.T1_end_dateEdit.setCurrentSectionIndex(2)
        self.T1_end_dateEdit.setObjectName("T1_end_dateEdit")
        self.horizontalLayout.addWidget(self.T1_end_dateEdit)
        self.T1_progressBar = QtWidgets.QProgressBar(self.T1_tab)
        self.T1_progressBar.setGeometry(QtCore.QRect(1210, 100, 314, 35))
        self.T1_progressBar.setStyleSheet("\n"
"QProgressBar\n"
"{\n"
"background-color: rgb(0, 0, 127);\n"
"border: 2px solid grey;\n"
"border-radius: 5px; \n"
"text-align: center;\n"
"font: 10pt \"微软雅黑\"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"background-color: rgb(187, 232, 255);\n"
"width: 10px; \n"
"margin: 0.5px; \n"
"}")
        self.T1_progressBar.setProperty("value", 100)
        self.T1_progressBar.setObjectName("T1_progressBar")
        self.T_explain_label_3 = QtWidgets.QLabel(self.T1_tab)
        self.T_explain_label_3.setGeometry(QtCore.QRect(30, 60, 1141, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.T_explain_label_3.setFont(font)
        self.T_explain_label_3.setStyleSheet("background:transparent;\n"
"color:white;\n"
";")
        self.T_explain_label_3.setScaledContents(True)
        self.T_explain_label_3.setObjectName("T_explain_label_3")
        self.eminer_tabWidget.addTab(self.T1_tab, "")
        self.T2_tab = QtWidgets.QWidget()
        self.T2_tab.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T2_tab.setObjectName("T2_tab")
        self.T2_Button1_1 = QtWidgets.QPushButton(self.T2_tab)
        self.T2_Button1_1.setGeometry(QtCore.QRect(610, 70, 141, 31))
        self.T2_Button1_1.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:10px;\n"
"font: 25 11pt \"微软雅黑\";\n"
"color:white;")
        self.T2_Button1_1.setObjectName("T2_Button1_1")
        self.T2_Button1_2 = QtWidgets.QPushButton(self.T2_tab)
        self.T2_Button1_2.setGeometry(QtCore.QRect(610, 20, 141, 31))
        self.T2_Button1_2.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:10px;\n"
"font: 25 11pt \"微软雅黑\";\n"
"color:white;")
        self.T2_Button1_2.setObjectName("T2_Button1_2")
        self.T2_drawlabel1 = QtWidgets.QLabel(self.T2_tab)
        self.T2_drawlabel1.setGeometry(QtCore.QRect(30, 149, 750, 581))
        self.T2_drawlabel1.setText("")
        self.T2_drawlabel1.setObjectName("T2_drawlabel1")
        self.T2_drawlabel2 = QtWidgets.QLabel(self.T2_tab)
        self.T2_drawlabel2.setGeometry(QtCore.QRect(820, 149, 750, 581))
        self.T2_drawlabel2.setText("")
        self.T2_drawlabel2.setObjectName("T2_drawlabel2")
        self.T2_Button2_1 = QtWidgets.QPushButton(self.T2_tab)
        self.T2_Button2_1.setGeometry(QtCore.QRect(1370, 70, 151, 31))
        self.T2_Button2_1.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:10px;\n"
"font: 25 11pt \"微软雅黑\";\n"
"color:white;")
        self.T2_Button2_1.setObjectName("T2_Button2_1")
        self.T2_Button2_2 = QtWidgets.QPushButton(self.T2_tab)
        self.T2_Button2_2.setGeometry(QtCore.QRect(1372, 18, 151, 31))
        self.T2_Button2_2.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:10px;\n"
"font: 25 11pt \"微软雅黑\";\n"
"color:white;")
        self.T2_Button2_2.setObjectName("T2_Button2_2")
        self.T2_usertype_label2 = QtWidgets.QLabel(self.T2_tab)
        self.T2_usertype_label2.setGeometry(QtCore.QRect(1040, 20, 76, 24))
        self.T2_usertype_label2.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 10pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T2_usertype_label2.setObjectName("T2_usertype_label2")
        self.T2_lineEdit = QtWidgets.QLineEdit(self.T2_tab)
        self.T2_lineEdit.setGeometry(QtCore.QRect(1040, 60, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 52, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.T2_lineEdit.setPalette(palette)
        self.T2_lineEdit.setText("")
        self.T2_lineEdit.setObjectName("T2_lineEdit")
        self.T2_label2_1 = QtWidgets.QLabel(self.T2_tab)
        self.T2_label2_1.setGeometry(QtCore.QRect(849, 11, 171, 54))
        self.T2_label2_1.setStyleSheet("background:transparent;\n"
"font: 20pt \"微软雅黑\";\n"
"")
        self.T2_label2_1.setObjectName("T2_label2_1")
        self.T2_label1_1 = QtWidgets.QLabel(self.T2_tab)
        self.T2_label1_1.setGeometry(QtCore.QRect(30, 10, 221, 56))
        self.T2_label1_1.setStyleSheet("background:transparent;\n"
"font: 20pt \"微软雅黑\";\n"
"")
        self.T2_label1_1.setObjectName("T2_label1_1")
        self.T2_progressBar1 = QtWidgets.QProgressBar(self.T2_tab)
        self.T2_progressBar1.setGeometry(QtCore.QRect(50, 70, 171, 35))
        self.T2_progressBar1.setStyleSheet("\n"
"QProgressBar\n"
"{\n"
"background-color: rgb(0, 0, 127);\n"
"border: 2px solid grey;\n"
"border-radius: 5px; \n"
"text-align: center;\n"
"font: 10pt \"微软雅黑\"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"background-color: rgb(187, 232, 255);\n"
"width: 10px; \n"
"margin: 0.5px; \n"
"}")
        self.T2_progressBar1.setProperty("value", 100)
        self.T2_progressBar1.setObjectName("T2_progressBar1")
        self.T2_progressBar2 = QtWidgets.QProgressBar(self.T2_tab)
        self.T2_progressBar2.setGeometry(QtCore.QRect(850, 70, 171, 35))
        self.T2_progressBar2.setStyleSheet("\n"
"QProgressBar\n"
"{\n"
"background-color: rgb(0, 0, 127);\n"
"border: 2px solid grey;\n"
"border-radius: 5px; \n"
"text-align: center;\n"
"font: 10pt \"微软雅黑\"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"background-color: rgb(187, 232, 255);\n"
"width: 10px; \n"
"margin: 0.5px; \n"
"}")
        self.T2_progressBar2.setProperty("value", 100)
        self.T2_progressBar2.setObjectName("T2_progressBar2")
        self.T_explain_label_2 = QtWidgets.QLabel(self.T2_tab)
        self.T_explain_label_2.setGeometry(QtCore.QRect(40, 110, 1101, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.T_explain_label_2.setFont(font)
        self.T_explain_label_2.setStyleSheet("background:transparent;\n"
"color:white;\n"
";")
        self.T_explain_label_2.setScaledContents(True)
        self.T_explain_label_2.setObjectName("T_explain_label_2")
        self.widget = QtWidgets.QWidget(self.T2_tab)
        self.widget.setGeometry(QtCore.QRect(250, 20, 331, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.T2_city_label = QtWidgets.QLabel(self.widget)
        self.T2_city_label.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 9pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T2_city_label.setObjectName("T2_city_label")
        self.horizontalLayout_2.addWidget(self.T2_city_label)
        self.T2_city_comboBox = QtWidgets.QComboBox(self.widget)
        self.T2_city_comboBox.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 10pt \"微软雅黑\";")
        self.T2_city_comboBox.setObjectName("T2_city_comboBox")
        self.T2_city_comboBox.addItem("")
        self.T2_city_comboBox.addItem("")
        self.T2_city_comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.T2_city_comboBox)
        self.widget1 = QtWidgets.QWidget(self.T2_tab)
        self.widget1.setGeometry(QtCore.QRect(250, 70, 331, 27))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.T2_usertype_label1 = QtWidgets.QLabel(self.widget1)
        self.T2_usertype_label1.setStyleSheet("background:transparent;\n"
"color:white;\n"
"font: 10pt \"宋体\";\n"
"font: 25 11pt \"微软雅黑\";")
        self.T2_usertype_label1.setObjectName("T2_usertype_label1")
        self.horizontalLayout_3.addWidget(self.T2_usertype_label1)
        self.T2_usertype_comboBox = QtWidgets.QComboBox(self.widget1)
        self.T2_usertype_comboBox.setStyleSheet("background-image:url(:/imagine/edata_of_pictures/anjian.jpg);\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 10pt \"微软雅黑\";")
        self.T2_usertype_comboBox.setObjectName("T2_usertype_comboBox")
        self.T2_usertype_comboBox.addItem("")
        self.T2_usertype_comboBox.addItem("")
        self.T2_usertype_comboBox.addItem("")
        self.T2_usertype_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.T2_usertype_comboBox)
        self.eminer_tabWidget.addTab(self.T2_tab, "")
        self.T3_tab = QtWidgets.QWidget()
        self.T3_tab.setStyleSheet("#T3_tab{\n"
"background-image: url(:/imagine/edata_of_pictures/heibeijing.jpg);\n"
"}")
        self.T3_tab.setObjectName("T3_tab")
        self.T3_tabWidget = QtWidgets.QTabWidget(self.T3_tab)
        self.T3_tabWidget.setGeometry(QtCore.QRect(0, 0, 1600, 780))
        self.T3_tabWidget.setStyleSheet("QTabBar::tab{border-image:url(:/imagine/edata_of_pictures/heibeijing.jpg);\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"微软雅黑\";\n"
"width：1000;\n"
"height:30;\n"
"border-width:2xp;\n"
"}\n"
"QTabWidget::pane\n"
"{\n"
"border-left-color: rgba(0, 0, 0, 0);\n"
"border-right-color: rgba(0, 0, 0, 0);\n"
"border-top-color: rgba(0, 0, 0, 0);\n"
"border-bottom-color: rgba(0, 0, 0, 0);\n"
"}")
        self.T3_tabWidget.setObjectName("T3_tabWidget")
        self.T3_nenghao_tab = QtWidgets.QWidget()
        self.T3_nenghao_tab.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T3_nenghao_tab.setObjectName("T3_nenghao_tab")
        self.T3_nenghao_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T3_nenghao_tab)
        self.T3_nenghao_webEngineView.setGeometry(QtCore.QRect(10, 0, 1581, 741))
        self.T3_nenghao_webEngineView.setStyleSheet("\n"
"background:transparent;\n"
"")
        self.T3_nenghao_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/T3_picture1.html"))
        self.T3_nenghao_webEngineView.setObjectName("T3_nenghao_webEngineView")
        self.T3_tabWidget.addTab(self.T3_nenghao_tab, "")
        self.T3_fugong_tab = QtWidgets.QWidget()
        self.T3_fugong_tab.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.T3_fugong_tab.setObjectName("T3_fugong_tab")
        self.T3_fugong_webEngineView = QtWebEngineWidgets.QWebEngineView(self.T3_fugong_tab)
        self.T3_fugong_webEngineView.setGeometry(QtCore.QRect(10, 0, 1581, 741))
        self.T3_fugong_webEngineView.setStyleSheet("background:transparent;")
        self.T3_fugong_webEngineView.setUrl(QtCore.QUrl("qrc:/html_file/edata_of_htmls/T3_picture2.html"))
        self.T3_fugong_webEngineView.setObjectName("T3_fugong_webEngineView")
        self.T3_tabWidget.addTab(self.T3_fugong_tab, "")
        self.eminer_tabWidget.addTab(self.T3_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.T1_end_label.setBuddy(self.T1_start_dateEdit)
        self.T1_start_label.setBuddy(self.T1_end_dateEdit)

        self.retranslateUi(MainWindow)
        self.eminer_tabWidget.setCurrentIndex(0)
        self.T3_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "电力大数据智能处理分析系统"))
        self.T_uploadfile_button.setText(_translate("MainWindow", "重新上传文件"))
        self.T_help_button.setText(_translate("MainWindow", "使用帮助"))
        self.T_explain_label.setText(_translate("MainWindow", "注：我们使用的数据来源绝大部分为复赛提供数据，其数据仍不够完整且经过了脱敏处理，因此我们的模型所展示结果可能与实际有一定偏差。"))
        self.T0_month_comboBox.setItemText(0, _translate("MainWindow", "2019年1月"))
        self.T0_month_comboBox.setItemText(1, _translate("MainWindow", "2019年2月"))
        self.T0_month_comboBox.setItemText(2, _translate("MainWindow", "2019年3月"))
        self.T0_month_comboBox.setItemText(3, _translate("MainWindow", "2019年4月"))
        self.T0_month_comboBox.setItemText(4, _translate("MainWindow", "2019年5月"))
        self.T0_month_comboBox.setItemText(5, _translate("MainWindow", "2019年6月"))
        self.T0_month_comboBox.setItemText(6, _translate("MainWindow", "2019年7月"))
        self.T0_month_comboBox.setItemText(7, _translate("MainWindow", "2019年8月"))
        self.T0_month_comboBox.setItemText(8, _translate("MainWindow", "2019年9月"))
        self.T0_month_comboBox.setItemText(9, _translate("MainWindow", "2019年10月"))
        self.T0_month_comboBox.setItemText(10, _translate("MainWindow", "2019年11月"))
        self.T0_month_comboBox.setItemText(11, _translate("MainWindow", "2019年12月"))
        self.T0_month_comboBox.setItemText(12, _translate("MainWindow", "2020年1月"))
        self.T0_month_comboBox.setItemText(13, _translate("MainWindow", "2020年2月"))
        self.T0_month_comboBox.setItemText(14, _translate("MainWindow", "2020年3月"))
        self.T0_month_comboBox.setItemText(15, _translate("MainWindow", "2020年4月"))
        self.T0_month_comboBox.setItemText(16, _translate("MainWindow", "2020年5月"))
        self.eminer_tabWidget.setTabText(self.eminer_tabWidget.indexOf(self.T0_tab), _translate("MainWindow", "电力数据概览"))
        item = self.T1_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Type1"))
        item = self.T1_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Type2"))
        item = self.T1_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Type3"))
        item = self.T1_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type4"))
        item = self.T1_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Type5"))
        item = self.T1_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Type6"))
        item = self.T1_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User Pattern"))
        item = self.T1_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "EUT"))
        item = self.T1_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Percentile"))
        __sortingEnabled = self.T1_tableWidget.isSortingEnabled()
        self.T1_tableWidget.setSortingEnabled(False)
        item = self.T1_tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        item = self.T1_tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "32.0726"))
        item = self.T1_tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "21.90%"))
        item = self.T1_tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "2"))
        item = self.T1_tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "273.1234"))
        item = self.T1_tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "11.68%"))
        item = self.T1_tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "3"))
        item = self.T1_tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "7.8491"))
        item = self.T1_tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "36.50%"))
        item = self.T1_tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "4"))
        item = self.T1_tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "78.5571"))
        item = self.T1_tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "16.79%"))
        item = self.T1_tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "5"))
        item = self.T1_tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "603.7234"))
        item = self.T1_tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "6.57%"))
        item = self.T1_tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "6"))
        item = self.T1_tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "149.0639"))
        item = self.T1_tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", "6.57%"))
        self.T1_tableWidget.setSortingEnabled(__sortingEnabled)
        self.T1_usertype_label.setText(_translate("MainWindow", "             用户类型:"))
        self.T1_usertype_comboBox.setItemText(0, _translate("MainWindow", "大工业用电"))
        self.T1_usertype_comboBox.setItemText(1, _translate("MainWindow", "城镇居民生活用电"))
        self.T1_usertype_comboBox.setItemText(2, _translate("MainWindow", "商业用电"))
        self.T1_city_label.setText(_translate("MainWindow", "             所在城市:"))
        self.T1_city_comboBox.setItemText(0, _translate("MainWindow", "成都市"))
        self.T1_end_label.setText(_translate("MainWindow", "             开始时间:"))
        self.T1_start_label.setText(_translate("MainWindow", "             结束时间:"))
        self.T_explain_label_3.setText(_translate("MainWindow", "* 目前demo阶段仅仅是展示我们的功能，可选择的用户类型、城市范围尚不完全，可选择的时间段为2018年4到6月，聚类使用数据以14天为一个周期。"))
        self.eminer_tabWidget.setTabText(self.eminer_tabWidget.indexOf(self.T1_tab), _translate("MainWindow", "    用电行为画像   "))
        self.T2_Button1_1.setText(_translate("MainWindow", "开始预测"))
        self.T2_Button1_2.setText(_translate("MainWindow", "保存结果"))
        self.T2_Button2_1.setText(_translate("MainWindow", "开始预测"))
        self.T2_Button2_2.setText(_translate("MainWindow", "保存结果"))
        self.T2_usertype_label2.setText(_translate("MainWindow", "用户编号:"))
        self.T2_lineEdit.setPlaceholderText(_translate("MainWindow", "请输入用户编号，如：39"))
        self.T2_label2_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">预测模式2:</span></p></body></html>"))
        self.T2_label1_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">预测模式1:</span></p></body></html>"))
        self.T_explain_label_2.setText(_translate("MainWindow", " * 本demo使用数据为2020年4月28日-5月28日期间的电力数据；“全部城市”选项暂时仅包括成都市与天府新区。"))
        self.T2_city_label.setText(_translate("MainWindow", "          所在城市:"))
        self.T2_city_comboBox.setItemText(0, _translate("MainWindow", "全部城市"))
        self.T2_city_comboBox.setItemText(1, _translate("MainWindow", "成都市"))
        self.T2_city_comboBox.setItemText(2, _translate("MainWindow", "天府新区"))
        self.T2_usertype_label1.setText(_translate("MainWindow", "          用户类型:"))
        self.T2_usertype_comboBox.setItemText(0, _translate("MainWindow", "全部类型"))
        self.T2_usertype_comboBox.setItemText(1, _translate("MainWindow", "大工业用电"))
        self.T2_usertype_comboBox.setItemText(2, _translate("MainWindow", "城镇居民生活用电"))
        self.T2_usertype_comboBox.setItemText(3, _translate("MainWindow", "商业用电"))
        self.eminer_tabWidget.setTabText(self.eminer_tabWidget.indexOf(self.T2_tab), _translate("MainWindow", " 用电负荷预测  "))
        self.T3_tabWidget.setTabText(self.T3_tabWidget.indexOf(self.T3_nenghao_tab), _translate("MainWindow", "区县能耗分布图"))
        self.T3_tabWidget.setTabText(self.T3_tabWidget.indexOf(self.T3_fugong_tab), _translate("MainWindow", "   区县复工指数图"))
        self.eminer_tabWidget.setTabText(self.eminer_tabWidget.indexOf(self.T3_tab), _translate("MainWindow", "   经济检测评估   "))
from PyQt5 import QtWebEngineWidgets
from T_MyLabel import MyLabel
from pyqtgraph import PlotWidget
import myResource_rc
