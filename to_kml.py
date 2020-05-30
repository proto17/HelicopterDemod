#!/usr/bin/python

import sys
import re

lat_patt = re.compile('^AN (\d+) (\d+)$')
lon_patt = re.compile('^BW (\d+) (\d+)$')

pair = [0, 0]
counter = 0

print('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Helo</name>')
for line in sys.stdin:
    line = line.rstrip()

    lat_match = lat_patt.match(line)
    if lat_match is not None:
        pair[0] = float('%s.%s' % (lat_match.group(1), lat_match.group(2)))
    else:
        lon_match = lon_patt.match(line)
        if lon_match is not None:
            pair[1] = -1 * float('%s.%s' % (lon_match.group(1), lon_match.group(2)))
            counter += 1
            print('<Placemark><TimeStamp><when>%d</when></TimeStamp><Point><coordinates>%f,%f,0</coordinates></Point></Placemark>' % (counter, pair[1], pair[0]))

print('</Document></kml>')
