# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 11:46:42 2020
自定义的Canopy类，实现了Canopy算法
@author: lxh
"""
import math
import copy
import numpy as np



class Canopy(object):
    def __init__(self, dataset, t1=0, t2=0, recompute=True, random_generate=True, shuffle_data=True): 
        self.dataset = copy.deepcopy(dataset) # 不改变原数据
        if type(dataset) is not np.ndarray:
            self.dataset = np.array(self.dataset)
        if shuffle_data: # 打乱原数据
            np.random.seed(666) # 固定随机种子，确保每次运行结果一样
            np.random.shuffle(self.dataset)

        self.recompute = recompute   # 重新计算聚类中心
        self.random_generate = random_generate # 随机生成初始聚类中心
        self.canopies = None
        if t1 > t2:
            self.t1 = t1
            self.t2 = t2
        else:
            print('t1 needs to be larger than t2!')

    # 设置初始阈值
    def setThreshold(self, t1, t2):
        if t1 > t2:
            self.t1 = t1
            self.t2 = t2
        else:
            print('t1 needs to be larger than t2!')

    # 使用欧式距离进行距离的计算
    def euclideanDistance(self, vec1, vec2) -> float:
        return math.sqrt(((vec1 - vec2)**2).sum())

    # 根据当前dataset的长度随机选择一个下标
    def getRandIndex(self) -> int:
        np.random.seed(666)  # 固定随机种子，确保每次运行结果一样
        return np.random.randint(0, len(self.dataset))
    
    # 选取当前dataset的中点作为下标
    def getMidIndex(self) -> int:
        return int(len(self.dataset) // 2)

    def getClusteringCenter(self):
        if self.canopies != None:
            return np.array([canopy[0] for canopy in self.canopies])
        else:
            print("You hadn't train this model!")

    def getCanopy(self):
        if self.canopies != None:
            return self.canopies
        else:
            print("You hadn't train this model!")
            
    def clustering(self):
        if self.t1 == 0:
            print('Please set the threshold.')
        else:
            self.canopies = []  # 用于存放最终归类结果
            while len(self.dataset) != 0:
                if self.random_generate:
                    my_index = self.getRandIndex()
                else:
                    my_index = self.getMidIndex()

                current_center = self.dataset[my_index] # 选择中心点
                self.dataset = np.delete(
                    self.dataset, my_index, 0)  # 删除选择的中心点P

                current_center_list = [current_center]  # 初始化P点的canopy类容器
                delete_list = []  # 初始化P点的删除容器
                
                for i in range(len(self.dataset)):
                    tmpdata = self.dataset[i]
                    distance = self.euclideanDistance(
                        current_center, tmpdata)  # 计算选取的中心点P到每个点之间的距离
                    if distance <= self.t1:
                        # 若距离小于t1，则将点归入P点的canopy类
                        current_center_list.append(tmpdata)
                    if distance <= self.t2:
                        delete_list.append(i)  # 若小于t2则归入删除容器
                # 根据删除容器的下标，将元素从数据集中删除
                self.dataset = np.delete(self.dataset, delete_list, 0)
                if len(current_center_list) > 1: # 太小就不要了
                    current_center_list = np.array(current_center_list)
                    if self.recompute:
                        # 重新计算聚类中心
                        current_center = current_center_list.mean(axis=0)
                    self.canopies.append([current_center, current_center_list])
        
