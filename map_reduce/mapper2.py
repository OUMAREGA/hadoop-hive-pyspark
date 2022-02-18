#!/usr/bin/env python3

import sys
import csv

sys.argv.pop(0)


with sys.stdin as csvfile:
    reader = csv.DictReader(csvfile) 
    for row in reader:
       for index in sys.argv:
          print(row[index],end="\t" if index is not sys.argv[-1] else "\n")

