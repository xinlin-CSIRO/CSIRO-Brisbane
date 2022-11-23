#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:09:29 2022

@author: wan397
"""
from math import sin, cos, sqrt, atan2, radians
import math
import random 
import numpy as np
import decimal
import datetime

def rssi (moving, fixed):
    current_x=moving[0]
    current_y=moving[1]
    fix_x=fixed[0]
    fix_y=fixed[1]
    
    
    alpha=2
    d_0=1
    thra=1
    rssi_do=-44.8
    R = 6373.0

    lat1 = radians(current_x)
    lon1 = radians(current_y)
    lat2 = radians(fix_x)
    lon2 = radians(fix_y)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    noise=random.uniform(-1,1)
    rssi_x=rssi_do-10*alpha*math.log10(distance)+noise
    
    return (distance, rssi_x)

date_object = str(datetime.date.today())
result_location='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_simulation_long.csv'
failure_location='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_failure_location.csv'
correct_location='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_correct_location.csv'
fix_1= np.array([-37.906023,145.1331578])
fix_2= np.array([-37.906023,145.1325358])
fix_3= np.array([-37.905867,145.1325358])
fix_4= np.array([-37.905867,145.1331578])

fix_1= np.array([-37.906023,145.1331578])
fix_2= np.array([-37.906023,145.1321111])
fix_3= np.array([-37.905567,145.1321111])
fix_4= np.array([-37.905567,145.1331578])


fix_devices = [-37.906023,145.1331578],[-37.906023,145.1325358],[-37.905867,145.1325358],[-37.905867,145.1331578]

fix_devices = [-37.906023,145.1331578],[-37.906023,145.1321111],[-37.905567,145.1321111],[-37.905567,145.1331578]

fix_devices=np.array(fix_devices, dtype=decimal.Decimal)
moving_tag=np.zeros(2)

max_lat=max(fix_devices[:,0])
min_lat=min(fix_devices[:,0])

max_lon=max(fix_devices[:,1])
min_lon=min(fix_devices[:,1])

with open(result_location, 'w', encoding='utf-8') as my_file:
      my_file.write('lat_moving,lon_moving, min_dis,max_power\n')   
with open(failure_location, 'w', encoding='utf-8') as my_fail:
      my_fail.write('correct_power,confused_power,average_power,correct_dis,confused_dis,average_dis\n')   
with open(correct_location, 'w', encoding='utf-8') as my_correct:
      my_correct.write('correct_power,second_power,average_power,correct_dis,second_dis,average_dis\n')  
      
for x in range(0, 200):
    lat_moving_tag=random.uniform(min_lat,max_lat)
    lon_moving_tag=random.uniform(min_lon,max_lon)
    moving_tag=np.array([lat_moving_tag,lon_moving_tag ])
    physical_distance_=np.zeros(len (fix_devices))
    rssi_=np.zeros(len (fix_devices))
    for y in range (0, len (fix_devices)):    
       physical_distance_[y], rssi_[y]=rssi (moving_tag , fix_devices[y])   
    min_dis = np.argmin(physical_distance_)
    min_rssi = np.argmax(rssi_)
    if(min_dis!=min_rssi):
        correct_power=rssi_[min_dis]
        confused_power=rssi_[min_rssi]
        average_power=np.average(rssi_)
        diff_power=abs(correct_power-confused_power)
        
        correct_distance=physical_distance_[min_dis]
        confused_distance=physical_distance_[min_rssi]
        average_distance=np.average(physical_distance_)
        diff_dis=abs(correct_distance-confused_distance)
        
        restult_fail=str(correct_power)+','+ str(confused_power)+','+ str(diff_power)+','+str(correct_distance)+','+ str(confused_distance)+','+str(diff_dis)
        with open(failure_location, 'a', encoding='utf-8') as my_fail:
                my_fail.write(restult_fail + '\n')          
    else:
            correct_power=rssi_[min_dis]
            second_power=sorted(rssi_)[-2]
            average_power=np.average(rssi_)
            diff_power=abs(correct_power-second_power)
            
            
            correct_distance=physical_distance_[min_dis]
            second_distance=sorted(physical_distance_)[1]
            average_distance=np.average(physical_distance_)
            diff_dis=abs(correct_distance-second_distance)
            
            restult_fail=str(correct_power)+','+ str(second_power)+','+ str(diff_power)+','+str(correct_distance)+','+ str(second_distance)+','+str(diff_dis)
            with open(correct_location, 'a', encoding='utf-8') as my_correct:
                    my_correct.write(restult_fail + '\n')          
    
    #restult=str(lat_moving_tag)+','+ str(lon_moving_tag)+','+ min_dis+','+min_rssi+','+ str(physical_distance_)+','+str(rssi_)
    restult=str(lat_moving_tag)+','+ str(lon_moving_tag)+','+ str(min_dis)+','+str(min_rssi)+','+ str(physical_distance_)+','+str(rssi_)
    print (restult)
    with open(result_location, 'a', encoding='utf-8') as my_file:
            my_file.write(restult + '\n')           
print ('completed')
