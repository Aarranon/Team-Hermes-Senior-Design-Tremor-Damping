# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:52:01 2020

@author: Aarranon

Using data/code from the micropython IMU project, specifically the sensor fusion
https://github.com/micropython-IMU/micropython-fusion

"""



from fusion import Fusion
import numpy as np


data = np.loadtxt('ztremor_data.csv', delimiter=',');
#loads data that is in the form of a csv with 
#ax, ay, az, gx, gy, gz
f= open("OutputOrientationy_tremor_z.csv","w+");

fuse = Fusion();

count = 0
dim = data.shape;
toIterateTo = dim[0];




f.write("Heading, Pitch, Roll:\n");

while count < toIterateTo:
    accel = (data[count][0],data[count][1],data[count][2]);
    gyro = (data[count][3],data[count][4],data[count][5]);
    fuse.update_nomag(accel, gyro, 100); #100 uS between measurements
    print("Pitch: {:7.3f}".format(fuse.pitch))
    f.write("{:7.3f}\n".format(fuse.pitch))
    count += 1
f.close
    