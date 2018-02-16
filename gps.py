# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:10:58 2017

@author: Prateek
"""

import serial
import pynmea2
#import time

#serial port initialization
ser=serial.Serial('COM4',9600)
sub="GPGGA"
cmd = ("AT_OGPS=3,2")
response=ser.write(cmd.encode())
print(response)
#ser.open()
s=""

#s = ser.readline() 
#s=str(s)
while(1):
    s = ser.readline() 
    s=str(s)
    if (sub in s):
#        print("true")
#        print(s)
        data=s.replace("b'","")
        data=data.replace("\\r\\n'","")
#.        print(data)
        gps=pynmea2.parse(data)
        print(gps.latitude,gps.lat_dir,",",gps.longitude,gps.lon_dir)
        d= str(gps.latitude)+str(gps.lat_dir)+","+str(gps.longitude)+str(gps.lon_dir)+"\n"
        g = open("gps.txt","a");
        g.writelines(d)
        g.close()
    else:
        pass
  
ser.close()
