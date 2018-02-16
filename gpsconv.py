# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 10:28:43 2017

@author: Prateek
"""

import pynmea2
data="$GPGGA,042004.000,1251.7252,N,07739.8343,E,1,6,1.46,925.2,M,-88.7,M,,*7E"
gps=pynmea2.parse(data)
print(gps.latitude,gps.lat_dir,",",gps.longitude,gps.lon_dir)

d= str(gps.latitude)+str(gps.lat_dir)+","+str(gps.longitude)+str(gps.lon_dir)+"\n"

g = open("gps.txt","a");
g.write(d)
g.close()


