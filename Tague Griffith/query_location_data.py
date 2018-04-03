#!/usr/bin/env python3

import redis
import sys

def query_location(r, lon, lat):
    "Use the lon and lat values to find nearby stations"
    
    # query redis for all stations near the current station
    
    

def parse_location_string(s):
    "Parse the location string from the location tool"
    pass
    

if __name__ == '__main__':
    
    # create a redis object
    r = None
    
    # you may need to change this based on your location tool 
    lon, lat = parse_location_string(sys.argv[1])
    
    query_location(r, lon, lat)


