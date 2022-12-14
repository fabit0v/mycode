#!/usr/bin/env python3


farms = [{"name": "NE Farm", 
    "agriculture": ["sheep", 
        "cows", "pigs", "chickens", 
        "llamas", "cats"]},
         {"name": "W Farm", 
             "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", 
             "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    print(farm) #prints entire farms
    
    for agricult in farm.get("agriculture"):
        print(agricult) #calls and prints only agriculture key items
