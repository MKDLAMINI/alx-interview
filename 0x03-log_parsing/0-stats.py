#!/usr/bin/python3
"""
Create a script that reads stdin line by line and computes the metrics
"""
import sys


def read_lines(stats, size_number):
    print("File size: {}".format(size_number))
    for status, count in sorted(stats.items()):
        if count != 0:
            print("{}: {}".format(status, count))
            
            
size_number = 0
state = 0
line_count = 0
stats = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        section = line.split()
        section = section[::-1]
        
        if len(section) > 2:
           line_count += 1
           
           if line_count <= 10:
              size_number += int(section[0])
              state = section[1]
              
              if (state in stats.keys()):
                  stats[state] += 1
                  
           if (line_count == 10):
              read_lines(stats, size_number)
              line_count = 0
            
finally:
    read_lines(stats, size_number)
