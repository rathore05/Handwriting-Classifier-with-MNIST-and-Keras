#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:29:03 2018

@author: slytherin
"""

import keras
from keras.datasets import mnist
#data=mnist.load_data()
(features_train,labels_train), (features_test,labels_test)=mnist.load_data()
features_train=features_train.reshape(features_train.shape[0],28,28,1)
print(features_train.shape)