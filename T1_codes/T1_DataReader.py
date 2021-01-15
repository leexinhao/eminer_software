# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:03:35 2020
读入数据
@author: lxh
"""
import sys, os
import numpy as np
import pandas as pd
import copy

def read_data(filepath=None, isnew=True, ispickle=False, filepath_pickle=None):
    if not isnew: # 直接读取序列化的文件
        if filepath_pickle == None:
            print("没输序列化地址")
        else:
            df = pd.read_pickle(filepath_pickle)
    else:
        if filepath == None:
            print("没输文件地址")
        else:
            # 读文件，注意指定编码为utf-8
            df = pd.read_csv(filepath, encoding='utf-8', delimiter='[,\t]', engine='python')            
            
            # 去除数据缺失的项，处理数据异常的项
            # df.replace(0, np.nan)
            # df.dropna(inplace=True)
            df.fillna(0, inplace=True)
            # 用后一列减前一列
            for i in range(1, 96):
                df['R'+str(i)] = df['R' + str(i+1)] - df['R'+str(i)]
                df.loc[df['R' + str(i)] < 0, 'R' + str(i)] = 0
                df.loc[df['R' + str(i)] > 40, 'R' + str(i)] = 0
            df.drop('R96', axis=1, inplace=True)
            
            df = df.groupby(by=['CONS_NO', 'NAME', 'SHIFT_NO', 'ORG_NAME']).sum()
            df.reset_index(inplace=True)
            df.set_index('CONS_NO', inplace=True)
            # 把成都的序列化，省的每次都要读一遍文件
            if ispickle:
                if filepath == None:
                    print("没输序列化地址")
                else:
                    df.to_pickle(filepath_pickle)
    
    return df
'''
读入数据并进行数据预处理
'''
def read_preprocess_data(days, typechoice, filepaths, isnew=True):
    cons_no_lists = []
    cons_no_sets = set()
    ori_datas = []
    pure_datas = []
    for test in range(days):
        if isnew:
            # 读取源文件
            df = read_data(filepath=filepaths[test] + ".csv",
                                      ispickle=True, 
                                      filepath_pickle=filepaths[test] + ".pkl")
        else:
            # 直接从序列化文件中读
            df = read_data(isnew=False, 
                                      filepath_pickle=filepaths[test] + ".pkl")
       
        '''
        print(test, ":")
        NAME_set = set()
        for i in df['NAME']:
            NAME_set.add(i)
        NAME_list = list(NAME_set)
        for name in NAME_set:
            print(name, len(df[df['NAME'] == name]))
        '''
        # 选择用户种类NAME
        df_tmp = df[df['NAME'] == typechoice]
    
        cons_no_list = set(df_tmp.index.to_list())  # 转成集合
        cons_no_sets |= cons_no_list
        cons_no_lists.append(cons_no_list)  # 记录用户编号
         
    cons_no_sets = list(cons_no_sets)
    cons_no_sets = sorted(cons_no_sets)
    ok_lists = []
    for cons in cons_no_sets:  # 对于缺失数据太多的用户，我们直接丢弃，缺失较少的给他补0
        count = 0
        for i in cons_no_lists:
            if cons in i:
                count += 1
        if count > 10:
            ok_lists.append(cons)
        
    
    for test in range(days):
    
        # 直接从序列化文件中读
        df = read_data(isnew=False, 
                                  filepath_pickle=filepaths[test] + ".pkl")
    
        # 选择用户种类NAME
        df_tmp = df[df['NAME'] == typechoice]
        ori_data = []
        for ok in ok_lists:
            if ok in cons_no_lists[test]:
                ori_data.append(copy.deepcopy(df_tmp.loc[ok,:][3:]))
            else:
                ori_data.append(np.zeros(95))
    
        ori_data = np.array(ori_data)
        pure_data = copy.deepcopy(ori_data)
        ori_datas.append(ori_data)
        try:
            # 归一化数据
            pure_data = (pure_data - pure_data.min()) / (pure_data.max() - pure_data.min())
            pure_datas.append(pure_data)
        except ValueError as e:
            print(typechoice)
            print(e)
    
    ori_datas = np.array(ori_datas)
    pure_datas = np.array(pure_datas)
    return ori_datas, pure_datas, ok_lists

'''
if __name__ == '__main__':

    # 读取源文件
    df = read_data(filepath="edata_of_csv/20180510.csv",
                              ispickle=True, 
                              filepath_pickle="edata_of_csv/20180510.pkl")

    # 直接从序列化文件中读
    df = read_data(isnew=False, 
                              filepath_pickle="edata_of_csv/20180510.pkl")
    days = 14    # 以days为周期
    typechoice = '城镇居民生活用电'
    filepaths = ["edata_of_csv/20180427", "edata_of_csv/20180428",
                 "edata_of_csv/20180429", "edata_of_csv/20180430",
                 "edata_of_csv/20180501", "edata_of_csv/20180502",
                 "edata_of_csv/20180503", "edata_of_csv/20180504",
                 "edata_of_csv/20180505", "edata_of_csv/20180506",
                 "edata_of_csv/20180507", "edata_of_csv/20180508",
                 "edata_of_csv/20180509", "edata_of_csv/20180510"]
    
    ori_datas, pure_datas, ok_lists = preprocess_data(days, typechoice, filepaths)
'''   
