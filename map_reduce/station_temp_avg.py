#!/usr/bin/env python3

# STATION TMP

# Avoir la moyenne des températures par station

import sys
import re
sum = 0
counter = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store


for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
        
    station, temp = data_mapped

    if oldKey and oldKey != station:
        print(oldKey, "\t", sum)
        oldKey = temp
        sum = 0

    oldKey = station
    counter+=1
    # remove all non numeric characters (except +, - and comma)
    temp = float(re.sub("[^0-9\-+\,]","",temp).replace(',','.'))

    sum += temp
    
if  oldKey != None and counter != 0:
    print("{}".format(sum/counter))
