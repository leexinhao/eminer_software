'''
模块一主线程
@author lxh
2020.08.09
utf-8
'''
from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtCore import *
import time, random
from T1_codes.T1_Canopy import *
from T1_codes.T1_AutoEncoder import *
import T1_codes.T1_DataDrawer as T1_DataDrawer
import T1_codes.T1_DataReader as T1_DataReader
from sklearn.metrics import *
from sklearn.cluster import KMeans
import sklearn.utils._cython_blas
import sklearn.neighbors.typedefs
import sklearn.neighbors.quad_tree
import sklearn.tree
import sklearn.tree._utils
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os
# 继承QThread
class T1_main_thread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    n_signal = pyqtSignal(int)
    lines_signal = pyqtSignal(list)
    table_signal = pyqtSignal(object)
    progress_signal = pyqtSignal(int)

    def __init__(self, days, typechoice, filepaths, city,
                 istrain, isDebug, isnew, parent=None):
        super(T1_main_thread, self).__init__(parent)
        self.days = days
        self.typechoice = typechoice
        self.filepaths = filepaths
        self.city = city
        self.istrain = istrain
        self.isDebug = isDebug
        self.isnew = isnew

    def __del__(self):
        self.wait()

    def run(self):
        # self.n_signal.emit(T1_main(days=self.days, typechoice=self.typechoice, filepaths=self.filepaths, city=self.city,
        #                            istrain=self.istrain, isDebug=self.isDebug, isnew=self.isnew))

        if self.city != '成都市':
            print("城市不存在！")  # demo阶段只有成都
        '''
        获得预处理后的数据
        '''
        ori_datas, pure_datas, ok_lists = T1_DataReader.read_preprocess_data(
            days=self.days, typechoice=self.typechoice, filepaths=self.filepaths, isnew=self.isnew)

        self.progress_signal.emit(random.randint(25, 35))
        '''
        自编码器降维
        24 * (60 / 15) = 96 - 1 = 95 刚好一天间隔15分钟的用电量
        '''

        input_dim = pure_datas.shape[0] * pure_datas.shape[2]  # 14 * 95 = 1330
        output_dim = 48  # 降至48维

        x_test_shape = pure_datas.shape[1] // 10
        new_datas = np.zeros((pure_datas.shape[1], input_dim))
        for i in range(0, pure_datas.shape[1]):
            new_datas[i, :] = pure_datas[:, i, :].reshape(-1)

        self.progress_signal.emit(random.randint(35, 45))

        if self.istrain:
            # 训练模型
            x_test = new_datas[0:x_test_shape, :]
            x_train = new_datas[x_test_shape:-1, :]
            learning_rate = 1.0
            loss = tf.keras.losses.MSE
            # loss = 'binary_crossentropy'
            epochs = 100
            batch_size = pure_datas.shape[1] // 200
            autoencoder = AutoEncoder(input_dim, output_dim, learning_rate, loss)
            # autoencoder.showNet()
            autoencoder.train(x_train, x_test, epochs, batch_size)
            # 将模型序列化存起来
            autoencoder.saveNet()
        else:
            # 加载训练好的模型，获得降维后的数据
            autoencoder = AutoEncoder()
            autoencoder.loadNet()

        # new_df = pd.DataFrame(new_data, index=df2.index, columns=[("特征"+str(i)) for i in range(1, output_dim+1)])
        result_datas = autoencoder.query(new_datas)

        self.progress_signal.emit(random.randint(55, 65))
        '''
        Canopy算法 + K_means聚类
        '''
        t = result_datas.mean()
        t1 = t * 4  # t1 > t2
        t2 = t * 1
        canopy = Canopy(result_datas, t1=t1, t2=t2, random_generate=True)
        canopy.clustering()
        cluster_centers = canopy.getClusteringCenter()
        n_clusters = len(cluster_centers)
        if n_clusters <= 2:  # 聚类数太少了放弃canopy算法
            if isDebug:
                print("聚类数太少了")
            n_clusters = 2
            km = KMeans(n_clusters=n_clusters)
        elif n_clusters > 6:  # 聚类数太多了放弃canopy算法
            n_clusters = 6
            km = KMeans(n_clusters=n_clusters)
        else:
            km = KMeans(n_clusters=n_clusters, init=cluster_centers,  n_init=1)

        labels = km.fit_predict(result_datas)

        cons_no_Cluster = [[] for i in range(n_clusters)]
        for i in range(len(ok_lists)):
            cons_no_Cluster[labels[i]].append(ok_lists[i])
        
        self.progress_signal.emit(random.randint(65, 75))
        '''
        画图
        '''
        # 绘制六个label
        lines, EUT = T1_DataDrawer.showClustering(
            ori_datas, labels, n_clusters, isDebug=self.isDebug)

        
        self.n_signal.emit(n_clusters)

        # 绘制lines
        self.lines_signal.emit(lines)
        
        line_count = np.zeros(n_clusters)
        for i in labels:
            line_count[i] += 1
        
        table_data = np.zeros((n_clusters, 3))
        for i in range(n_clusters):
            table_data[i, 0] = i + 1
            table_data[i, 1] = EUT[i]
            table_data[i, 2] = line_count[i] / len(labels)
        

        # 绘制table
        table_df = pd.DataFrame(table_data, 
        index=['Type' + str(i) for i in range(1, n_clusters+1)],
        columns=['User type', 'EUT', 'Percentile'])
        self.progress_signal.emit(random.randint(85, 95))
        self.table_signal.emit(table_df)
        

        
