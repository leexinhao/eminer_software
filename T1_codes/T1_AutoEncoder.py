# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 14:11:32 2020
封装了一个自编码器
@author: lxh
"""
import sys, os
#import tensorflow as tf
import tensorflow.keras.models
import pickle
import tensorflow.keras.optimizers
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import tensorflow.python.keras.engine.base_layer_v1

# 封装了一个深度自编码器
class AutoEncoder(object):
    def __init__(self, input_dim=1330, output_dim=48, learning_rate=1.0, loss='binary_crossentropy'):
        self.input_dim = input_dim
        self.output_dim = output_dim
        encoder_input = Input(shape=(input_dim,))
        # 编码器网络结构
        encoded = Dense(640, activation='relu')(encoder_input)
        encoded = Dense(320, activation='relu')(encoded)
        encoded = Dense(160, activation='relu')(encoded)
        encoded = Dense(96, activation='relu')(encoded)
        encoder_output = Dense(output_dim, activation='sigmoid')(encoded)
        self.encoder = Model(encoder_input, encoder_output, name='encoder')
        
        # 解码器网络结构
        decoder_input = Input(shape=(output_dim,))
        decoded = Dense(96, activation='relu')(decoder_input)
        decoded = Dense(160, activation='relu')(decoded)
        decoded = Dense(320, activation='relu')(decoded)
        decoded = Dense(640, activation='relu')(decoded)
        decoder_output = Dense(input_dim, activation='sigmoid')(decoded)
        self.decoder = Model(decoder_input, decoder_output, name='decoder')
        
        # 合成自动编码器
        autoencoder_input = Input(shape=(input_dim,))
        autoencode = self.encoder(autoencoder_input)
        autoencoder_output = self.decoder(autoencode)
        self.autoencoder = Model(autoencoder_input, autoencoder_output, name='autoencoder')
        
        # 配置
        self.autoencoder.compile(optimizer=tensorflow.keras.optimizers.Adadelta(
    lr=learning_rate, rho=0.95, epsilon=None, decay=0.0), loss=loss)
        
    def train(self, x_train, x_test, epochs=50, batch_size=256):
        self.autoencoder.fit(x_train, x_train,
                epochs=epochs,
                batch_size=batch_size,
                shuffle=True,
                validation_data=(x_test, x_test))
    def query(self, x_test, isReverse=False, isTesting=False):
        if isTesting: # 试试还原度高不高
            return self.autoencoder.predict(x_test)
        else:
            if isReverse:
                return self.decoder.predict(x_test)
            else:
                return self.encoder.predict(x_test)
    
    def showNet(self):
        self.encoder.summary()
        self.decoder.summary()
        self.autoencoder.summary()
        
    def saveNet(self):
        nowPaths = os.path.dirname(__file__)
        self.encoder.save(os.path.join(nowPaths, 'T1_encoderfile'))
        
        self.decoder.save(os.path.join(nowPaths,  'T1_decoderfile'))
        self.autoencoder.save(os.path.join(nowPaths, 'T1_autocoderfile'))
        with open(os.path.join(nowPaths, 'T1_input_dim'), 'wb') as f:
            pickle.dump(self.input_dim, f)
        with open(os.path.join(nowPaths, 'T1_output_dim'), 'wb') as f:
            pickle.dump(self.output_dim, f)
            
    def loadNet(self, filenames=None):
        if filenames == None:
            nowPaths = os.path.dirname(__file__)
            self.encoder = tensorflow.keras.models.load_model(os.path.join(nowPaths, 'T1_encoderfile'))
            self.decoder = tensorflow.keras.models.load_model(os.path.join(nowPaths, 'T1_decoderfile'))
            self.autoencoder = tensorflow.keras.models.load_model(os.path.join(nowPaths, 'T1_autocoderfile'))
            with open(os.path.join(nowPaths, 'T1_input_dim'), 'rb') as f:
                self.input_dim = pickle.load(f)
            with open(os.path.join(nowPaths, 'T1_output_dim'), 'rb') as f:
                self.output_dim = pickle.load(f)
        else:
            pass  # 先放同一个目录吧
'''
if __name__ == '__main__':
    from keras.datasets import mnist
    import numpy as np
    (x_train, _), (x_test, _) = mnist.load_data()
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
    x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
    autoencoder = AutoEncoder()
    autoencoder.saveNet()
    #autoencoder.loadNet()
    #autoencoder.train(x_train, x_test)
'''
