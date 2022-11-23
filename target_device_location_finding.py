

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


head = 'https://my.rayven.io:8082/api/apipull?uid=3709a9c185814805403996cc4127800b6786&deviceid='
rear = '&from_date=2022-10-01T00:00:00Z&end_date=2022-10-05T00:30:00Z'
fixed_devices_lib = '/Users/wan397/Desktop/IoT_and_Privacy/clayton_rayven_devices.csv'
date_object = str(datetime.date.today())

loc_lib = '/Users/wan397/Desktop/IoT_and_Privacy/device_locations_confirmed.csv'
location_lib = np.array(pd.read_csv(loc_lib, usecols=[0, 1, 2, 3]))

tag_1=['d89790002059','d89790002073','d89790002080','d89790002109']

which_one=0
URL = head+tag_1[which_one]+rear
response = requests.get(URL)

print ('Target Tag id is', tag_1[which_one])
data_raw = '/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_'+tag_1[which_one]+'.json'
open(data_raw, "wb").write(response.content)
with open(data_raw, 'r') as f:
    data = json.load(f)
    
lat_tag=0
lon_tag=0
b=7
len_=len(data)
for x in range (len_-1, 0, -1):
    temp=data[x]
    
    if (len(temp)==20):
        lat_tag=round(float(temp['lat']),b)
        lon_tag=round(float(temp['lon']),b)
        break;
found=0 
  
for x in range (0, len(location_lib)):
  candid_lat = round(location_lib[x, 2], b)
  candid_lon = round(location_lib[x, 3], b)
  #print (candid_lat)
  #print (candid_lon)
  if(candid_lat==lat_tag) and (candid_lon== lon_tag):
      print('source device is ',location_lib[x,0])
      found=1
  elif(candid_lat==lat_tag) and (candid_lon!= lon_tag):
      print('same lat with ',location_lib[x,0])
      print('but lon cannot be matched ')
      same_lon=0
      for y in range (0, len(location_lib)):
          candid_lon_1 = round(location_lib[y, 3], b)
          if (candid_lon_1== lon_tag):    
             print('same lon is matched with another device ', location_lib[y,0])
             same_lon=1
      if(same_lon==0):
          print ('No device is matched with the same lon of the target Tag')
      
      
  elif(candid_lat!=lat_tag) and (candid_lon== lon_tag):
        print('same lon with ',location_lib[x,0])
        print('but loat cannot be matched ')
      
      #break;
if(found==0) :    print('failed')
        
        

print('program ended')
