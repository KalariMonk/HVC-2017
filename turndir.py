import zonechar
import json


json_data=open("E:\SWorkSpace\Mapping_race_track\jsoncoordinates.json").read();

data = json.loads(json_data);

def turn(x):
    x=str(x)
    lat1=data['Turns'][x]['entry']['lat']
    long1=data['Turns'][x]['entry']['lng']
    
    lat2=data['Turns'][x]['peak']['lat']
    long2=data['Turns'][x]['peak']['lng']
    
    lat3=data['Turns'][x]['exit']['lat']
    long3=data['Turns'][x]['exit']['lng']
    
    dir1=zonechar.zone(lat1,long1,lat2,long2)
    dir2=zonechar.zone(lat2,long2,lat3,long3)
    
    print(dir1);
    print(dir2);    
        
    if(dir1=="North"):
        if(dir2=="East"):
            print("Right Turn")
        if(dir2=='West'):
            print("Left Turn")
        if(dir2=='South'):
            print("U Turn ahead")
    elif(dir1=='South'):     
        if(dir2=='East'):
            print("Left Turn")
        if(dir2=='West'):
            print("Right Turn")
        if(dir2=='North'):
            print("U Turn ahead")
    elif(dir1=='East'):     
        if(dir2=='North'):
            print("Left Turn")
        if(dir2=='South'):
            print("Right Turn")
        if(dir2=='West'):
            print("U Turn ahead")
    elif(dir1=='West'):     
        if(dir2=='North'):
            print("Right Turn")
        if(dir2=='South'):
            print("Left Turn")
        if(dir2=='East'):
            print("U Turn ahead")
           
turn(1);
