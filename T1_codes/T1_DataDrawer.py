# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:03:53 2020
可视化数据
@author: lxh
"""

import threading
import pickle
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('Qt5Agg')   # 没这个多线程会报错
'''
ori_data: 数据集 (14, n, 95)
label: 对应的标签 (n,)
n_clusters: 聚类数
km_cluster_centers: 聚类中心 
'''

rlock = threading.RLock()


def showClustering(ori_data, label, n_clusters=1, km_cluster_centers=[], saveit=True, isDebug=False):
    x = np.arange(0, 95)
    label_lists = []
    for i in range(n_clusters):
        label_lists.append([])
        for j in range(0, ori_data.shape[1]):
            if label[j] == i:
                label_lists[i].append(j)
    lines = []
    EUT = []
    with rlock:
        for i in range(n_clusters):
            y_mean = np.zeros(95)
            plt.figure(figsize=(7.0, 4.0), dpi=120, num=i+1)
            for j in label_lists[i]:
                for k in range(14):
                    plt.plot(x, ori_data[k, j, :], '-',
                             color='#E6E6FA', linewidth=0.5) 
                    y_mean = y_mean + ori_data[k, j, :]
            y_mean /= (14 * len(label_lists[i]))
            lines.append(y_mean)
            EUT.append(y_mean.sum())
            plt.plot(x, y_mean, color='#8B0000', linewidth=3)
            if len(km_cluster_centers) > 0:
                for k in range(14):
                    plt.plot(
                        x, km_cluster_centers[k, i, :], color='r', linewidth=1)
            ax = plt.gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.spines['left'].set_color('white')
            ax.spines['bottom'].set_color('white')

            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.spines['bottom'].set_position(('data', 0))
            ax.spines['left'].set_position(('data', 0))
            plt.xlim((0, 95))
            plt.ylim((0, 40))
            plt.xlabel('TIME', color='white')
            plt.ylabel('POWER CONSUMPTION', color='white')
            plt.tick_params(axis='x', colors='white')
            plt.tick_params(axis='y', colors='white')
            ynew_ticks = np.linspace(0, 40, 10)
            plt.xticks([0, 8,  16,  24,  32,  40,
                        48, 56,  64,  72, 80,  88],
                       ['0:00',  '2:00', '4:00',  '6:00',
                        '8:00',  '10:00',  '12:00',
                        '14:00',  '16:00',  '18:00',  '20:00',
                        '22:00'], color='white')
            plt.yticks(ynew_ticks, label='时间', color='white')
            plt.title('Pattern ' + str(i+1), color='white')
            if saveit:
                nowPaths = os.path.dirname(os.path.dirname(__file__))
                plt.savefig(os.path.join(nowPaths, 'edata_of_pictures', 'T1_type' + str(i + 1) +
                            '_tmp.png'), transparent=True)

                if isDebug:
                    plt.show()
            else:
                plt.show()
        plt.cla() 
        plt.clf()
        plt.close('all')
    return lines, EUT



