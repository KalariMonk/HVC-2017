# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 18:56:51 2016

@author: Prateek Gupta
"""

import json

json_data=open("E:\SWorkSpace\Mapping_race_track\jsoncoordinates.json").read();

data = json.loads(json_data);
x='Turns'
for i in range(1,17):
    y=str(i);
    print("\n");
    print(data[x][y]["entry"]["lat"]);
    

  
    
