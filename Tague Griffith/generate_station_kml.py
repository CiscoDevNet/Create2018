#!/usr/bin/env python3

import redis
import xml.dom.minidom as minidom

def generate_placemark(doc, document, station):
    "Generates a single place mark from a station"
        
    placemark = doc.createElement('Placemark')
    document.appendChild(placemark)
    
    # create the placemark name
    name = doc.createElement('name')
    name.appendChild(doc.createTextNode(station['name']))
    placemark.appendChild(name)
    
    # create the placemark description
    desc = doc.createElement('description')
    desc.appendChild(doc.createTextNode("{} Bike share station." .format(station['name'])))
    placemark.appendChild(desc)
    placemark.childNodes[0]
    
    # add point coords
    point = doc.createElement('Point')
    coords = doc.createElement('coordinates')
    coords.appendChild(doc.createTextNode("{},{}".format(station['lon'], station['lat'])))
    point.appendChild(coords)
    placemark.appendChild(point)

def create_kml(r, system_id):
    "Creates a KML files as a dom tree"
    
    doc = minidom.Document()
    kml = doc.createElementNS("http://www.opengis.net/kml/2.2", "kml")
    document = doc.createElement('Document')
    kml.appendChild(document)
    doc.appendChild(kml)
    
    # generate kml from a single Bike Share System (free map API allows limited number of 
    # waypoints)
    
    return doc

if __name__ == '__main__':
    
    # create a redis object
    r = None
    system_id = input("Enter system id: ")
    doc = create_kml(r, system_id)
    f = open('bikeshare.kml', 'w')
    f.write(doc.toprettyxml(indent='    '))
    
