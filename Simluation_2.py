#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:09:35 2022

@author: wan397
"""

from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest


failure_location='/Users/wan397/Desktop/IoT_and_Privacy/2022-10-20_failure_location.csv'
correct_location='/Users/wan397/Desktop/IoT_and_Privacy/2022-10-20_correct_location.csv'
training = np.array(pd.read_csv(failure_location, usecols=[2]))

testing = np.array(pd.read_csv(correct_location, usecols=[2]))

initial_correct = np.array(pd.read_csv(correct_location, usecols=[2]))


clf = OneClassSVM(kernel='rbf', gamma='auto').fit(training)
y= clf.predict(testing)

long=len(y)
xx=0
for x in y:
    if x ==1:
        xx+=1
percent=1-xx/long
print (percent)


model = IsolationForest(contamination=0.01)

model.fit(training)
yhat = model.predict(testing)


long2=len(yhat)
xxx=0
for x in yhat:
    if x ==1:
        xxx+=1
percent2=1-xxx/long2
print (percent2)
