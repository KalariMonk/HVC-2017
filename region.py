
import json
import math
from distance import haversine

#global variables
'''distance in meters'''
x=15
'''Meters to Degrees'''
deglt=(1/110574)*15

lap=1
T='Turns'
aprz=1
gpsy=28.353805
gpsx=77.533627

#function to calculate the unit longitude for a given latitude

def long(x,s):
    deglg = (1/(111320*math.cos(math.radians(x))))
    d=s*deglg
    return d
   
json_data=open("E:\SWorkSpace\Mapping_race_track\jsoncoordinates.json").read();

data = json.loads(json_data);

'''Code above this statement should not be changed'''

x=[77.533758,77.533686,77.533684,77.533681,77.533678]   
y=[28.353422,28.353504,28.353546,28.353599,28.353625]


while(1):
    
    if(aprz>=1 and aprz<=16):
      y=str(aprz)  
      lat=data[T][y]["entry"]["lat"]
      lng=data[T][y]["entry"]["lng"]
    
    if(aprz==1):
        lap+=1;
    
    print (lat,lng)
    ltu = lat+deglt
    ltd = lat-deglt
    lgl = lng-long(lat,x)
    lgr = lng+long(lat,x)
    
    print(ltu,ltd,lgl,lgr)
    print(gpsx,gpsy)
        
    if((gpsy<ltu and gpsy>ltd) or(gpsx>lgl and gpsx<lgr)):
       print("Car has entered region"+" "+y)
    
    if(aprz>=1 and aprz<=16):
      y=str(aprz)  
      lat=data[T][y]["exit"]["lat"]
      lng=data[T][y]["exit"]["lng"]
    
    print (lat,lng)
    ltu = lat+deglt
    ltd = lat-deglt
    lgl = lng-long(lat,x)
    lgr = lng+long(lat,x)
    
    print(ltu,ltd,lgl,lgr)
    print(gpsx,gpsy)
        
    if((gpsy<ltu and gpsy>ltd) or(gpsx>lgl and gpsx<lgr)):
       print("Car is exiting zone"+" "+y)
       if(aprz<16):
           aprz+=1
       else:
           aprz=1

for i in range(0,4):
    tempx=x[i]
    tempy=y[i]
    d=haversine(lng,lat,tempx,tempy)
    print(d)  
    