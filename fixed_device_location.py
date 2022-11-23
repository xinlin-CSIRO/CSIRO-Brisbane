#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 14:01:49 2022

@author: wan397
"""
 # -*- coding: utf-8 -*-
import json
import datetime
import requests
import pandas as pd
import numpy as np





URL='https://my.rayven.io:8082/api/apipull?uid=3709a9c185814805403996cc4127800b6786&deviceid=d89790002113&from_date=2022-10-01T00:00:00Z&end_date=2022-10-01T00:10:00Z'
date_object = str(datetime.date.today())
path_raw='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_raw_data_1.json'
path_cleaned='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_cleaned_data_.csv'
information=['uuid','lat','lon','height','accelX','accelY','accelZ','time','route','rssi']

response = requests.get(URL)

lot=[]
lon=[]

open(path_raw, "wb").write(response.content)
with open(path_raw, 'r') as f:
  data = json.load(f)
for x in range (len(data)):
    if(len(data[x])==16):    
        lot.append(data[x]['lat'])
        lon.append(data[x]['lon'])
print ('1')


    



