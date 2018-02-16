# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:31:59 2016

@author: Prateek Gupta
"""

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1=0.0 
    lon2=0.0 
    lat1=0.0 
    lat2=0.0 

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

'''d = haversine(77.533662,28.353715,77.533683,28.353576)
d=d*1000;
print(d);
print('meters')   ''' 
