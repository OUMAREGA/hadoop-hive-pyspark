#!/usr/bin/env python3

import builtins # fonctions natives de python : min, max
import re
# LATITUDE LONGITUDE TMP

# Déterminer la température minimale, maximale, moyenne en fonction de la latitude - longitude

# Argument de l'opération doit être passé (min,max ou moy)

from datetime import datetime
import sys

sys.argv.pop(0)

dico = {}
for line in sys.stdin:
    lat,lon,temp = line.split('\t')
    lat_lon = lat + "-" + lon
    # remove all non numeric characters (except +, - and comma)
    temp = float(re.sub("[^0-9\-+\,]","",temp).replace(',','.'))
    if lat_lon not in dico:
        dico[lat_lon] = []
    dico[lat_lon].append(temp);

op = sys.argv[0]


for lat_lon in dico.keys():
    
    # getattr : 2 arguments, nom du module, puis nom de la fonction à exécuter
    
    function_result = None 
    
    if op == "moy":
        function_result = sum(dico[lat_lon])/len(dico[lat_lon])
    if op == "range":
        function_result = max(dico[lat_lon]) - min(dico[lat_lon])
    if op == "min" or op == "max":  
        function_result = getattr(builtins,op)(dico[lat_lon])

    print("{}\t{}".format(lat_lon,function_result))


