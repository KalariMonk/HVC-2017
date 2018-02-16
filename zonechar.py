import math
from math import sin,cos

def zone(lat1,long1,lat2,long2):
    long1, lat1, long2, lat2 = map(math.radians, [long1, lat1, long2, lat2])
    diff = (long2-long1)
    X = cos(lat2)*sin(diff)
    Y = cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(diff)
    b = math.atan2(X,Y)
    b = math.degrees(b)
    if(b>=0 and b<=20):
        return "North"
    elif(b>20 and b<=80):
        return "North east"
    elif(b>80 and b<=100):
        return "East"
    elif(b>100 and b<=160):
        return "South east"
    elif(b>160 and b<=190):
        return "South"    
    elif(b>190 and b<=260):
        return "South west"
    elif(b>260 and b<=280):
        return "West" 
    elif(b>280 and (b<=360 or b<=0)):
        return "North west"    
   # print(b);
    
#b = zone(39.099912, -94.581213,38.627089, -90.200203)
#print(b);