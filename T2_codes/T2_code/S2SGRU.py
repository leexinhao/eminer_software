#预测用电量
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense,GRU
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import time


class GRU_prediction:
    seed = 9
    step = 50
    epochs = 50
    batch_size = 25


    # 定义split_sequence函数，返回值X含有n_steps个之前的值，y是下一时刻的值
    def split_sequence(self,sequence, n_steps):
        X, y = list(), list()
        for i in range(len(sequence)):
            end_ix = i + n_steps
            if end_ix > len(sequence) - 1:
                break
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    def build_model(self):
        step = self.step
        model = Sequential()
        # model.add(GRU(4, activation="relu", input_shape=(step, 1)))
        model.add(GRU(150,activation="relu",input_shape=(step,1),return_sequences=True))
        model.add(GRU(50,activation="relu",return_sequences=True))
        model.add(GRU(20,activation="relu"))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        return model

    # 设置随机种子
    def predict(self,samples):
        # 数据归一化
        scaler = MinMaxScaler()
        data = scaler.fit_transform(samples)
        step=self.step
        epochs=self.epochs
        batch_size=self.batch_size

        # print(data[0])
        # print(data)
        # 建立模型

        # 设置随机种子
        seed=self.seed

        data, labels = GRU_prediction.split_sequence(self,samples, n_steps=step)
        data = data.reshape((len(data), step, 1))
        np.random.seed(seed)
        model=GRU_prediction.build_model(self)
        model.summary()

        history = model.fit(data, labels, epochs=epochs, batch_size=batch_size, validation_split=0.2)
        # loss = history.history['loss']
        # val_loss = history.history['val_loss']
        # plt.plot(range(epochs), loss, "bo", label="loss")
        # plt.plot(range(epochs), val_loss, "b", label='val_loss')
        # plt.legend()
        # plt.show()

        # 定义方法，可以预测从101到150的结果
        def predict101_150(samples):
            results = []
            for i in range(3 * 95):
                # print(samples[-1].shape)
                result = model.predict(samples[-1].reshape(1, step, 1))

                results.append(result)

                sample = np.append(samples[-1][1:], result)
                # print(samples[-1][1:].shape)
                # 序列是从0开始的 第一个不要 加入一个

                sample = sample.reshape((1, step, 1))
                # print(sample.shape)
                samples = np.concatenate((samples, sample), axis=0)
            return results

        results = predict101_150(data)
        results = np.array(results).reshape(-1, 1)

        # 反标准化数据 --- 目的是保证MSE的准确性

        results = scaler.inverse_transform(results)
        samples = scaler.inverse_transform(samples)

        # plt.plot(range(len(samples)), samples)
        # plt.plot(range(len(samples), len(samples) + len(results)), results.reshape(len(results)))

        # plt.plot(range(50),np.array(results).reshape(50,))

        y = model.predict(data[-1].reshape(1, step, 1))
        # print('单步预测结果' + str(y))
        # print(results[-1])

        plt.show()
        return results


import numpy as np
import pandas as pd
import os


# 输入你的数据文件路径 用电量
dir=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_training')
# 输入你的数据文件路径 温度
dir2=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'T2_temperature')

# 读取目标文件所有csv文件
def all_csv_list(dir):
    csv_list = []
    for root_dir, sub_dir, files in os.walk(dir):  # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
        for file in files:
            if file.endswith('csv'):
                # 构造绝对路径
                file_name = os.path.join(root_dir, file)
                csv_list.append(file_name)
    return csv_list

print(len(all_csv_list(dir)))

# 合并csv文件
def merge_csv(file_list):
    df1 = pd.read_csv(file_list[0], header=None)
    cols = [i for i in df1.columns if i not in [0,1, 2, 3]] #除去无关数据
    df2 = df1[cols]
    df3 = df2.T
    #df_sum = df3.drop(columns=[0])
    df_sum=df3.drop(labels=0, axis=1)
    for filename in file_list[1:]:
        df0 = pd.read_csv(filename, header=None)
        cols0 = [j for j in df0.columns if j not in [0, 1,2,3]]
        df20 = df0[cols0]
        df30 = df20.T
        #df30 = df30.drop(columns=[0])
        df30=df30.drop(labels=0, axis=1)
        # 纵向向表行对齐连接
        df_sum = pd.concat([df_sum, df30], axis=0)
    return df_sum




filelist=all_csv_list(dir)
df=merge_csv(filelist)
dataset=df.values


print(dataset.shape)


# 保存合并csv
# filename = 'C:/Users/gaohongcheng/Desktop/temp.csv'
# df.to_csv(filename, encoding='utf-8')



# filename = 'C:/Users/gaohongcheng/Desktop/temp.csv'
# data = pd.read_csv(filename, usecols=[2], engine='python')
# dataset = data.values.astype('float32')
# samples=dataset
# prediction1=GRU_prediction()
# results=prediction1.predict(samples)
# print(results.shape)
# # print(results)
#
# final_results=np.concatenate((results,results),axis=1)
# print(final_results.shape)

# 对序列分别预测
samples0=dataset[:,0].reshape(-1,1)
prediction0 = GRU_prediction()
results0=prediction0.predict(samples0)
final_results=results0
for i in range(1,dataset.shape[1]):
    samples=dataset[:,i].reshape(-1,1)
    prediction1 = GRU_prediction()
    results=prediction1.predict(samples)
    final_results=np.concatenate((final_results,results),axis=1)


print(final_results.shape)

result_df = pd.DataFrame(final_results)
# result_df.columns# 修改DataFrame的列名


# 输出结果保存合并csv
filename = 'results.csv'
result_df.to_csv(filename, encoding='utf-8')