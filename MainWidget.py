import Ui_MainWindow_e_Miner
import sys
import os
import time
import random
import pickle
from PyQt5 import QtCore, QtWidgets, QtGui, QtWebEngineWidgets
from PyQt5.QtWidgets import QSizePolicy, QFileDialog, QHeaderView, QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QPixmap
from T1_main_thread import T1_main_thread
from T2_main_thread import *
import pyqtgraph as pg
from T2_codes.T2_code.T2_draw import *
from datetime import datetime, timedelta
from T_message_dialog import *
import shutil
import matplotlib.pyplot as plt
import pandas as pd

class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow_e_Miner.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)

        ####################公共部分###################
        pg.setConfigOptions(leftButtonPan=False)  # 防拖动
        pg.setConfigOptions(antialias=True)  # 启用抗锯齿( 让曲线更加光滑)
        pg.setConfigOption('background', (255, 255, 255, 0))  # 背景颜色
        pg.setConfigOption('foreground', (255, 255, 255))  # 坐标轴颜色
        # pyqtgraph的设置必须在控件创立前才能生效
        self.setupUi(self)

        ####################公共部分###################

        ####################模块零部分##################
        # 使web透明
        self.T0_pie_webEngineView.page().setBackgroundColor(Qt.transparent)
        self.T0_bar1_webEngineView.page().setBackgroundColor(Qt.transparent)
        self.T0_bar2_webEngineView.page().setBackgroundColor(Qt.transparent)
        self.T0_funnel_webEngineView.page().setBackgroundColor(Qt.transparent)
        self.T0_map_webEngineView.page().setBackgroundColor(Qt.transparent)
        # 隐藏滚动条
        self.T0_pie_webEngineView.page().settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.ShowScrollBars, False)
        self.T0_bar1_webEngineView.page().settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.ShowScrollBars, False)
        self.T0_bar2_webEngineView.page().settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.ShowScrollBars, False)
        self.T0_funnel_webEngineView.page().settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.ShowScrollBars, False)
        self.T0_map_webEngineView.page().settings().setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.ShowScrollBars, False)
        ####################模块一部分##################

        self.T1_period = 14  # 周期
        self.T1_start_dateEdit.dateChanged['QDate'].connect(
            lambda: self.T1_add_date())  # 或者self.T_add_date
        self.T1_end_dateEdit.dateChanged['QDate'].connect(
            lambda: self.T1_sub_date())  # connect要连的是函数不是他的返回值

        self.T1_n_clusters = 6  # 聚类数
        '''
        table
        '''
        # 使表格适应容器大小
        self.T1_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.T1_tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表格字体，颜色
        self.T1_table_font = QtGui.QFont()
        self.T1_table_font.setBold(True)
        self.T1_table_font.setWeight(75)
        self.T1_table_brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        self.T1_table_brush.setStyle(QtCore.Qt.NoBrush)
        for i in range(6):
            for j in range(3):
                item = self.T1_tableWidget.item(i, j)
                item.setFont(self.T1_table_font)
                item.setForeground(self.T1_table_brush)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 居中
        '''
        labels
        '''
        self.T1_image_labels = []
        self.T1_image_labels.append(self.T1_image_label1)
        self.T1_image_labels.append(self.T1_image_label2)
        self.T1_image_labels.append(self.T1_image_label3)
        self.T1_image_labels.append(self.T1_image_label4)
        self.T1_image_labels.append(self.T1_image_label5)
        self.T1_image_labels.append(self.T1_image_label6)
        '''
        初始先设好示例图片,表格，比较好看的那种,选择大工业用电
        '''

        self.T1_show_backup()

        '''
        lines
        '''
        self.T1_ptr = 0
        self.T1_show_period = 10  # lines展示窗口的周期
        self.T1_tmpdatas = None
        self.T1_datas = None
        self.T1_curves = None
        # 六根线的颜色
        self.T1_Pens = [
            pg.mkPen({'color': "#DC143C", 'width': 3}),
            pg.mkPen({'color': "#DA70D6", 'width': 3}),
            pg.mkPen({'color': "#800080", 'width': 3}),
            pg.mkPen({'color': "#FFFF00", 'width': 3}),
            pg.mkPen({'color': "#E6E6FA", 'width': 3}),
            pg.mkPen({'color': "#B0E0E6", 'width': 3})]
        T1_e_x = range(95)
        T1_e_str = ["{:0>2d}:{:0>2d}".format(
            i // 4, (i % 4) * 15) for i in T1_e_x]
        T1_e_ticks = [(i, j) for i, j in zip(T1_e_x, T1_e_str)]
        strAxis = pg.AxisItem(orientation='bottom')
        strAxis.setTicks([T1_e_ticks])
        self.T1_graphicsView.setYRange(0, 15)
        self.T1_graphicsView.setAxisItems(axisItems={'bottom': strAxis})
        self.T1_graphicsView.setLabel('left', 'AVERAGE POWER CONSUMPTION')
        self.T1_graphicsView.setLabel('bottom', 'TIME')  # 这个要放后面
        self.T1_graphicsView.addLegend( offset=(10, 5), rowCount=2, colCount=4, horSpacing=20) # 控制legend
        nowPaths = os.path.dirname(__file__)
        with open(os.path.join(nowPaths, 'T1_line'), 'rb') as f:
            tmplines = pickle.load(f)
        self.T1_handle_draw_lines(tmplines)
        # self.T1_compute_result()
        ####################模块一部分###################

        ####################模块二部分###################
        self.T2_has_draw1 = False
        self.T2_has_draw2 = False
        self.T2_Button1_1.released.connect(self.T2_f1_1)
        self.T2_Button1_2.released.connect(self.T2_f1_2)
        self.T2_Button2_1.released.connect(self.T2_f2_1)
        self.T2_Button2_2.released.connect(self.T2_f2_2)
        a = QPixmap(os.path.join(os.path.dirname(__file__), 'T2_codes', 'T2_png','prep1.png'))
        self.T2_drawlabel1.setPixmap(a)
        self.T2_drawlabel1.setScaledContents(True)
        a = QPixmap(os.path.join(os.path.dirname(__file__), 'T2_codes', 'T2_png','prep2.png'))
        self.T2_drawlabel2.setPixmap(a)
        self.T2_drawlabel2.setScaledContents(True)
        ####################模块二部分###################

        ####################模块三部分###################
        self.T3_fugong_webEngineView.page().setBackgroundColor(Qt.transparent)
        self.T3_nenghao_webEngineView.page().setBackgroundColor(Qt.transparent)
        ####################模块三部分###################

    ###################公共部分###################
   
    def on_T_uploadfile_button_released(self):
        tmpdialog = T_message_dialog(self, "重新上传文件", "demo阶段暂不开放上传自定义数据文件功能！")
        tmpdialog.exec_()
    def on_T_help_button_released(self):
        tmpdialog = T_message_dialog(self, "使用帮助", "软件功能及使用请查看附件：README(帮助文档).pdf，介绍视频.mp4。")
        tmpdialog.exec_()
    
    ####################公共部分###################
    
    ####################模块零部分###################
    def on_T0_month_comboBox_currentTextChanged(self):
        tmpStr = self.T0_month_comboBox.currentText()
        if len(tmpStr) < 8:
            tmpStr = tmpStr[0:4] + '0' + tmpStr[5:-1]
        else:
            tmpStr = tmpStr[0:4] + tmpStr[5:-1]
        tmpStr = "qrc:/html_file/edata_of_htmls/" + tmpStr
        self.T0_map_webEngineView.setUrl(QtCore.QUrl(
            tmpStr + "T0_map.html"))

        self.T0_pie_webEngineView.setUrl(QtCore.QUrl(
            tmpStr + "T0_pie1.html"))

        self.T0_funnel_webEngineView.setUrl(QtCore.QUrl(
            tmpStr + "T0_funnel.html"))

        self.T0_bar1_webEngineView.setUrl(QtCore.QUrl(
            tmpStr + "T0_bar1.html"))

        self.T0_bar2_webEngineView.setUrl(QtCore.QUrl(
            tmpStr + "T0_bar2.html"))

    ####################模块零部分###################

    ####################模块一部分###################
    '''
    控制日期控件相差固定周期(我们这为14)
    同时监控几个选项控件变化，变化了就重新计算
    '''

    def T1_add_date(self):
        self.T1_end_dateEdit.setDateTime(
            self.T1_start_dateEdit.dateTime().addDays(+self.T1_period))
        # 修改日期后重新计算各模块，只需要写一个就行了，因为改了一个另一个肯定会跟着改
        self.T1_compute_result()  # 模块1

    def T1_sub_date(self):
        self.T1_start_dateEdit.setDateTime(
            self.T1_end_dateEdit.dateTime().addDays(-self.T1_period))

    def on_T1_usertype_comboBox_currentTextChanged(self):
        # print(self.T1_usertype_comboBox.currentText())
        self.T1_compute_result()

    def on_T1_city_comboBox_currentTextChanged(self):
        # print(self.T1_city_comboBox.currentText())
        self.T1_compute_result()

    '''
    停用所有按键
    '''
    def T1_set_unable_all(self):
        self.T1_start_dateEdit.setEnabled(False)
        self.T1_end_dateEdit.setEnabled(False)
        self.T1_city_comboBox.setEnabled(False)
        self.T1_usertype_comboBox.setEnabled(False)
        # self.T1_start_dateEdit.setStyleSheet(
        #     '''
        #     background-image: url(: / imagine/edata_of_pictures/heianjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )
        # self.T1_end_dateEdit.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/heianjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # ) 
        # self.T1_city_comboBox.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/heianjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )
        # self.T1_usertype_comboBox.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/heianjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )

    '''
    启用所有按键
    '''
    def T1_set_able_all(self):
        self.T1_start_dateEdit.setEnabled(True)
        self.T1_end_dateEdit.setEnabled(True)
        self.T1_city_comboBox.setEnabled(True)
        self.T1_usertype_comboBox.setEnabled(True)
        # self.T1_start_dateEdit.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/anjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )
        # self.T1_end_dateEdit.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/anjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )
        # self.T1_city_comboBox.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/anjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )
        # self.T1_usertype_comboBox.setStyleSheet(
        #     '''
        #     background-image: url(:/imagine/edata_of_pictures/anjian.jpg)
        #     border-radius: 5px
        #     color: white
        #     font: 10pt "微软雅黑"
        #     '''
        # )
    '''
    根据当前选项跑一遍结果
    '''
    def T1_compute_result(self):
        self.T1_set_unable_all()
        self.T1_progressBar.setValue(0)
        start_time = self.T1_start_dateEdit.date().toString("yyyyMMdd")
        end_time = self.T1_end_dateEdit.date().toString("yyyyMMdd")
        user_type = self.T1_usertype_comboBox.currentText()
        city = self.T1_city_comboBox.currentText()
        begindate = datetime(int(start_time[0:4]), int(
            start_time[4:6]), int(start_time[6:]))
        filepaths = []
        self.T1_progressBar.setValue(5)
        for i in range(self.T1_period):
            nowPaths = os.path.dirname(__file__)
            filepaths.append(os.path.join(nowPaths,  'edata_of_csv' , 'edata_of_csv_2018' , begindate.strftime("%Y%m%d")))
            begindate += timedelta(days=1)

        # 启动模块一线程
        self.T1_progressBar.setValue(random.randint(5, 15))
        self.T1_thread = T1_main_thread(days=14, typechoice=user_type, filepaths=filepaths, city=city,
                                        istrain=False, isDebug=False, isnew=False, parent=self)
        self.T1_thread.finished.connect(self.T1_set_able_all)
        self.T1_thread.n_signal.connect(self.T1_handle_set_n)
        self.T1_thread.progress_signal.connect(self.T1_handle_set_progress)
        self.T1_thread.lines_signal.connect(self.T1_handle_draw_lines)
        self.T1_thread.table_signal.connect(self.T1_handle_draw_table)
        self.T1_thread.start()

    # 处理模块一线程发出的各信号
    def T1_handle_set_progress(self, t):
        self.T1_progressBar.setValue(t)

    def T1_handle_set_n(self, n):
        self.T1_n_clusters = n
        self.T1_reshow()

    def T1_handle_draw_lines(self, lines):
        self.T1_datas = []
        self.T1_tmpdatas = []
        for line in lines:
            self.T1_datas.append(line)
            self.T1_tmpdatas.append(line[0:self.T1_show_period])
        self.T1_graphicsView.clear()
        self.T1_curves = []
        for i in range(self.T1_n_clusters):
            curve = pg.PlotCurveItem(pen=self.T1_Pens[i], name='Pattern'+str(i+1))
            self.T1_curves.append(curve)
            self.T1_graphicsView.addItem(curve)

        self.T1_timer = pg.QtCore.QTimer()
        self.T1_timer.timeout.connect(self.T1_lines_update)
        self.T1_timer.start(500)

    def T1_lines_update(self):

        for i in range(self.T1_n_clusters):
            self.T1_tmpdatas[i][:-1] = self.T1_tmpdatas[i][1:]
            self.T1_tmpdatas[i][-1] = self.T1_datas[i][self.T1_ptr +
                                                       self.T1_show_period]
        self.T1_ptr += 1
        if self.T1_ptr + self.T1_show_period >= 95:
            self.T1_ptr = 0
        for i in range(self.T1_n_clusters):
            self.T1_curves[i].setData(self.T1_tmpdatas[i])
            self.T1_curves[i].setPos(self.T1_ptr, 0)

    def T1_handle_draw_table(self, table_df):
        self.T1_tableWidget.setRowCount(self.T1_n_clusters)
        self.T1_tableWidget.setVerticalHeaderLabels(table_df.index.to_list())
        table_data = table_df.to_numpy()

        for i in range(self.T1_n_clusters):
            for j in range(3):
                if j == 0:
                    item = QTableWidgetItem("{:.0f}".format(table_data[i, j]))
                elif j == 1:
                    item = QTableWidgetItem("{:.4f}".format(table_data[i, j]))
                elif j == 2:
                    item = QTableWidgetItem(
                        "{:.2f}%".format(100 * table_data[i, j]))
                item.setFont(self.T1_table_font)
                item.setForeground(self.T1_table_brush)
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 居中
                self.T1_tableWidget.setItem(i, j, item)

        self.T1_progressBar.setValue(100)
    '''
    显示模块一预设图片
    '''
    def T1_show_backup(self):
        for i in range(1, 7):
            if i > self.T1_n_clusters:
                self.T1_image_labels[i-1].setVisible(False)
            else:
                tmp_picture = QPixmap(os.path.join(os.path.dirname(__file__), 
                    'edata_of_pictures', 'T1_type' + str(i) + '.png'))
                self.T1_image_labels[i-1].setVisible(True)
                self.T1_image_labels[i-1].setPixmap(tmp_picture)
                self.T1_image_labels[i-1].setScaledContents(
                    True)  # 让图片自适应label大小
    '''
    刷新展示结果
    '''
    def T1_reshow(self):

        try:
            for i in range(1, 7):
                if i > self.T1_n_clusters:
                    self.T1_image_labels[i-1].setVisible(False)
                else:
                    tmp_picture = QPixmap(os.path.join(os.path.dirname(__file__),
                        'edata_of_pictures' , 'T1_type' + str(i) + '_tmp.png'))
                    self.T1_image_labels[i-1].setVisible(True)
                    self.T1_image_labels[i-1].setPixmap(tmp_picture)
                    self.T1_image_labels[i-1].setScaledContents(
                        True)  # 让图片自适应label大小
        except Exception as e:
            print(e)
            self.T1_show_backup()

    #####################模块一部分###################

    ####################模块二部分###################
    def T2_set_unable(self, flag):
        if flag == 1:
            self.T2_Button1_1.setEnabled(False)
            self.T2_Button1_1.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/heianjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
            self.T2_Button1_2.setEnabled(False)
            self.T2_Button1_2.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/heianjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
            self.T2_city_comboBox.setEnabled(False)
            self.T2_usertype_comboBox.setEnabled(False)
            # self.T2_city_comboBox.setStyleSheet(
            #     '''
            #     background-image: url(:/imagine/edata_of_pictures/heianjian.jpg)
            #     border-radius: 5px
            #     color: white
            #     font: 10pt "微软雅黑"
            #     '''
            # )
            # self.T2_usertype_comboBox.setStyleSheet(
            #     '''
            #     background-image: url(:/imagine/edata_of_pictures/heianjian.jpg)
            #     border-radius: 5px
            #     color: white
            #     font: 10pt "微软雅黑"
            #     '''
            # )
        else:
            self.T2_Button2_1.setEnabled(False)
            self.T2_Button2_2.setEnabled(False)
            self.T2_Button2_1.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/heianjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
            self.T2_Button2_2.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/heianjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
    
    def T2_set_able(self, flag):
        if flag == 1:
            self.T2_Button1_1.setEnabled(True)
            self.T2_Button1_2.setEnabled(True)
            self.T2_city_comboBox.setEnabled(True)
            self.T2_usertype_comboBox.setEnabled(True)
            self.T2_Button1_1.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/anjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
            self.T2_Button1_2.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/anjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
            # self.T2_city_comboBox.setStyleSheet(
            #     '''
            #     background-image: url(:/imagine/edata_of_pictures/anjian.jpg)
            #     border-radius: 5px
            #     color: white
            #     font: 10pt "微软雅黑"
            #     '''
            # )
            # self.T2_usertype_comboBox.setStyleSheet(
            #     '''
            #     background-image: url(:/imagine/edata_of_pictures/anjian.jpg)
            #     border-radius: 5px
            #     color: white
            #     font: 10pt "微软雅黑"
            #     '''
            # )
        else:
            self.T2_Button2_1.setEnabled(True)
            self.T2_Button2_1.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/anjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
            self.T2_Button2_2.setEnabled(True)
            self.T2_Button2_2.setStyleSheet(
                '''
                background-image:url(:/imagine/edata_of_pictures/anjian.jpg);
                border-radius:10px;
                font: 25 11pt "微软雅黑";
                color:white;
                '''
            )
    def T2_handle_finish1(self):
        self.T2_has_draw1 = True
        a = QPixmap(os.path.join(os.path.dirname(__file__), 'T2_codes', 'T2_png','p1.png'))
        self.T2_drawlabel1.setPixmap(a)
        self.T2_drawlabel1.setScaledContents(True)
        self.T2_progressBar1.setValue(100)
        self.T2_set_able(1)

    def T2_handle_finish2(self):
        self.T2_has_draw2 = True
        a = QPixmap(os.path.join(os.path.dirname(__file__), 'T2_codes', 'T2_png','p2.png'))
        self.T2_drawlabel2.setPixmap(a)
        self.T2_drawlabel2.setScaledContents(True)
        self.T2_progressBar2.setValue(100)
        self.T2_set_able(2)

    def T2_f1_1(self):  # 预测按钮1
        self.T2_progressBar1.setValue(random.randint(55, 65))
        self.T2_set_unable(1)
        self.T2_thread1 = T2_main_thread1(self.T2_city_comboBox.currentText(),
                                                   self.T2_usertype_comboBox.currentText(), self)
        self.T2_thread1.finished.connect(self.T2_handle_finish1)
        self.T2_thread1.start()
        # T2draw1(self.T2_city_comboBox.currentText(),
        #         self.T2_usertype_comboBox.currentText())
        

    def T2_f2_1(self):  # 预测按钮2
        self.T2_progressBar2.setValue(random.randint(55, 65))
        self.T2_set_unable(2)
        cons = int(self.T2_lineEdit.text())
        self.T2_thread2 = T2_main_thread2(cons, self)
        self.T2_thread2.finished.connect(self.T2_handle_finish2)
        self.T2_thread2.start()
        # T2draw2(int(cons))
        

    def T2_f1_2(self):
        fileName, ok = QFileDialog.getSaveFileName(self,
                                                    "文件保存",
                                                    "/result",
                                                    "xlsx Files (*.xlsx);;csv Files (*.csv)")
        if fileName == '':
            return
        if not self.T2_has_draw1:
            
            a = pd.read_csv(os.path.join(os.path.dirname(
                __file__), 'T2_codes', 'T2_file', 'pretmp1.csv'), encoding='ansi')
        else:
            a = pd.read_csv(os.path.join(os.path.dirname(
                __file__), 'T2_codes', 'T2_file', 'tmp1.csv'), encoding='ansi')
            
        if ok[0] == 'x':
            a.to_excel(fileName, index=0)
        else:
            a.to_csv(fileName, index=0)
    def T2_f2_2(self):
        fileName, ok = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "/result",
                                                     "xlsx Files (*.xlsx);;csv Files (*.csv)")
        if fileName == '':
            return
        global T2drawcnt2
        if not self.T2_has_draw2:
            a=pd.read_csv(os.path.join(os.path.dirname(__file__), 'T2_codes', 'T2_file','pretmp2.csv'),encoding='ansi')
        else:
            a=pd.read_csv(os.path.join(os.path.dirname(__file__), 'T2_codes', 'T2_file','tmp2.csv'),encoding='ansi')

        if ok[0] == 'x':
            a.to_excel(fileName,index=0)
        else:
            a.to_csv(fileName,index=0)


    ####################模块二部分###################
