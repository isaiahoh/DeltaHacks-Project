# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 18:47:15 2018

@author: ashar
"""
#how to calculate code from a point
#lattitude distance km = 111.04 km per degree
#Longitude distance km = 111.32 cos(lat) km


def converter(desired_lat,desired_long,lat,long):
    import math
    lat_km = lat *111.04
    desired_lat_km = desired_lat*111.04
    
    long_km = long*111.32*math.cos(math.radians(lat))
    desired_long_km = desired_long*111.32*math.cos(math.radians(desired_lat))
    
    
    delta_lat = desired_lat_km - lat_km
    delta_long = desired_long_km - long_km
    
    distance = math.sqrt(((delta_lat)**2) + (delta_long)**2)
    
    return distance

def haversine(desired_lat,desired_long,lat,long):
    import math
    r = 6371000 #inmeters
    lat_rad = math.radians(lat)
    desired_lat_rad = math.radians(desired_lat)
    
    delta_lat = math.radians((desired_lat - lat))
    delta_long = math.radians((desired_long - long))
    
    a = (math.sin(delta_lat/2))*(math.sin(delta_lat/2)) + (math.cos(lat_rad))*(math.cos(desired_lat_rad))*(math.sin(delta_long/2))*(math.sin(delta_long/2))
    
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    drake = r*c
    
    return drake

#us
a = 43.262710 
b = -79.922200

#mcmaster
c = 43.2609 
d = -79.9192


print(haversine(a,b,c,d))


def angle(desired_lat,desired_long,lat,long):
    import math
    delta_y = desired_lat - lat
    delta_x = math.cos((math.pi/180)*lat) *(desired_long-long)
    angle = math.atan2(delta_y,delta_x)
    
    return math.degrees(angle)

print(angle(a,b,c,d))

