#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:28:03 2022

@author: wan397
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:18:20 2022

@author: wan397
"""

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
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest


def rssi (distance):
         
    alpha=2
    d_0=1
    thra=1
    rssi_do=-44.8
    noise=random.uniform(-1,1)
    rssi_x=rssi_do-10*alpha*math.log10(distance)+noise   
    return (rssi_x)

def rssi_fake (distance):
         
    alpha=2
    d_0=1
    thra=1
    rssi_do=-54.8
    noise=random.uniform(-1,1)
    rssi_x=rssi_do-10*alpha*math.log10(distance)+noise   
    return (rssi_x)


def distance (moving, fixed):
    current_x=moving[0]
    current_y=moving[1]
    fix_x=fixed[0]
    fix_y=fixed[1]
    distance=((abs(current_x)-abs(fix_x))**2 + (abs(current_y)-abs(fix_y))**2)**0.5
    return (distance)

constant_real=1
constand_fake_=round(random.uniform(0,1))

print (constand_fake_)

date_object = str(datetime.date.today())
result_location='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_simulation_long.csv'
failure_location='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_failure_location.csv'
correct_location='/Users/wan397/Desktop/IoT_and_Privacy/' + date_object+'_correct_location.csv'
with open(result_location, 'w', encoding='utf-8') as my_file:
      my_file.write('lat_moving,lon_moving, min_dis,max_power\n')   
with open(failure_location, 'w', encoding='utf-8') as my_fail:
      my_fail.write('correct_power,confused_power,average_power,correct_dis,confused_dis,average_dis\n')   
with open(correct_location, 'w', encoding='utf-8') as my_correct:
      my_correct.write('correct_power,second_power,average_power,correct_dis,second_dis,average_dis\n')  
a=4
seg_x_1=np.arange(0,20)
seg_x_2=np.ones(20)*20
seg_x_3=np.arange(20,40)
seg_x_4=np.ones(20)*40
seg_x_5=np.arange(40,60)
seg_x_6=np.ones(20)*60
seg_x_7=np.arange(60,80)
seg_x_8=np.ones(20)*80
seg_x_9=np.arange(80,100)
seg_x_10=np.ones(20)*100


seg_y_1=np.ones(20)*a
seg_y_up=np.linspace(a, 50-a,20)
seg_y_down=np.linspace(50-a, a,20)
seg_y_2=np.ones(20)*(50-a)

path_1=np.concatenate((seg_x_1.reshape(-1,1),seg_y_1.reshape(-1,1)),axis=1)
path_2=np.concatenate((seg_x_2.reshape(-1,1),seg_y_up.reshape(-1,1)),axis=1)
path_3=np.concatenate((seg_x_3.reshape(-1,1),seg_y_2.reshape(-1,1)),axis=1)
path_4=np.concatenate((seg_x_4.reshape(-1,1),seg_y_down.reshape(-1,1)),axis=1)
path_5=np.concatenate((seg_x_5.reshape(-1,1),seg_y_1.reshape(-1,1)),axis=1)
path_6=np.concatenate((seg_x_6.reshape(-1,1),seg_y_up.reshape(-1,1)),axis=1)
path_7=np.concatenate((seg_x_7.reshape(-1,1),seg_y_2.reshape(-1,1)),axis=1)
path_8=np.concatenate((seg_x_8.reshape(-1,1),seg_y_down.reshape(-1,1)),axis=1)
path_9=np.concatenate((seg_x_9.reshape(-1,1),seg_y_1.reshape(-1,1)),axis=1)
path_10=np.concatenate((seg_x_10.reshape(-1,1),seg_y_up.reshape(-1,1)),axis=1)

path=np.concatenate((path_1,path_2,path_3,path_4,path_5,path_6,path_7,path_8,path_9,path_10))
fix_devices = [0,0],[100,0],[100,100],[0,100],[105,50]
fix_devices=np.array(fix_devices)

rssi_last=np.zeros(5)
correct=icorrect=0

saving=[]
for x in range (len(path)):
    tag=path[x]
    distances=np.zeros(5)
    rssi_=np.zeros(5)
    for x_1 in range (5):
         if(x_1!=4):
            distances[x_1]=distance(tag, fix_devices[x_1])
            rssi_[x_1]=rssi(distances[x_1])
         else:
            #print ('constant= ',constand_fake_)
            distances[x_1]=distance(tag, fix_devices[x_1])
            if(constand_fake_==1)and (x>100):         
              rssi_[x_1]=rssi_fake (distances[x_1])
            else:
                rssi_[x_1]=-10000000
            #print ('fake= ',rssi_[x_1])
    real_=np.argmin(distances)
    guess=np.argmax(rssi_)
    guess_rssi=np.max(rssi_)
    
    
    if(x<100):
      saving.append(rssi_[0:4])
    else:
        test=np.sort(rssi_)
        test=test[1:5].reshape(1, 4)
        saving=np.array(saving)
        clf = OneClassSVM(kernel='rbf', gamma='auto').fit(saving)
        y= clf.predict(test)
        print ('guess= ', y)
            
    if(x!=0):
        rssi_last=rssi_last.reshape(-1,1)
        rssi_diff=guess_rssi-rssi_last
        #if(rssi_diff)
        #np.partition(k.flatten(), -2)[-2]
    label=0


    if(guess==4):
        
        
            
            
            
        #print ('index= ',x)
        print ('location= ',tag)

        
        #print ('distance ',distances)
        #print ('rssi ',rssi_)
        
        label=1
        icorrect+=1
        correct_power=rssi_[real_]
        confused_power=rssi_[guess]
        average_power=np.average(rssi_)
        diff_power=abs(correct_power-confused_power)
        
        correct_distance=distances[real_]
        confused_distance=distances[guess]
        average_distance=np.average(distances)
        diff_dis=abs(correct_distance-confused_distance)
        
        restult_fail=str(correct_power)+','+ str(confused_power)+','+ str(diff_power)+','+str(correct_distance)+','+ str(confused_distance)+','+str(diff_dis)
        with open(failure_location, 'a', encoding='utf-8') as my_fail:
                my_fail.write(restult_fail + '\n') 
    
    

    #if(x>0):
           #print ('diff =',rssi_diff[0], 'label=',label)
    rssi_last=np.max(rssi_)   
    
print ('correct',correct)       
print ('icorrect',icorrect)             
print ('completed')
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
