

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




head='https://my.rayven.io:8082/api/apipull?uid=3709a9c185814805403996cc4127800b6786&deviceid='
rear='&from_date=2022-10-01T00:00:00Z&end_date=2022-10-01T00:10:00Z'
fixed_devices_lib='/Users/wan397/Desktop/IoT_and_Privacy/clayton_rayven_devices.csv'
date_object = str(datetime.date.today())

path_cleaned='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_relaylocation_.csv'

strings='id,lat_m,lat_max,lot_m,lot_max'
with open(path_cleaned, 'w', encoding='utf-8') as my_file:
        my_file.write(strings + '\n')           
print ('0')

location_lib=np.array(pd.read_csv(fixed_devices_lib, usecols=[0,3]))
for x in range (0, len(location_lib)):
    if(location_lib[x,1])=='relay':
        id_=str(location_lib[x,0])
        URL=head+id_+rear
        response = requests.get(URL)
        lot=[]
        lon=[]
        path_raw='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_relay' 
        path_raw=path_raw+str(x)+'.json'
        open(path_raw, "wb").write(response.content)
        with open(path_raw, 'r') as f:
          data = json.load(f)
        if (len(data)>1):  
            for y in range (len(data)):
                if(len(data[y])==20):    
                    lot.append(data[y]['lat'])
                    lon.append(data[y]['lon'])
            lot=np.array(lot)
            lon=np.array(lon)
            if (len(lot)>0):
                max_lot=max(lot)
                min_lot=min(lot)
            else:
                max_lot=0
                min_lot=0
                
            if (len(lon)>0):
                max_lon=max(lon)
                min_lon=min(lon)
            else:
                max_lon=0
                min_lon=0
                
            strings=''         
            strings=id_+','+str(max_lot)+','+str(min_lot)+','+str(max_lon)+','+str(min_lon)
            
            with open(path_cleaned, 'a', encoding='utf-8') as my_file:
                    my_file.write(strings + '\n')           
            print ('1')
        
print ('over')






    
    


