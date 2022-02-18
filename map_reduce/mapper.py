#!/usr/bin/env python3

import sys
import csv

for line in sys.stdin:
   data = line.strip().split(",")
   if len(data) == 30:
      city, pm10, pm25 = data
      print("{0}\t{1}\t{2}".format(city, pm10, pm25))