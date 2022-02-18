#!/usr/bin/env python3

import builtins # fonctions natives de python : min, max

# DATE TMP

# Déterminer la température minimale, maximale, moyenne ou l'écart par jour

# Argument de l'opération doit être passé (min,max ou moy)

from datetime import datetime
import sys
import re

sys.argv.pop(0)

dico = {}
for line in sys.stdin:
    date,temp = line.split('\t')
    # remove all non numeric characters (except +, - and comma)
    temp = float(re.sub("[^0-9\-+\,]","",temp).replace(',','.'))
    # 2021-06-21T21:00:00
    day = date.split('T')
    if day[0] not in dico:
        dico[day[0]] = []
    dico[day[0]].append(temp);

op = sys.argv[0]


for day in dico.keys():
    
    # getattr : 2 arguments, nom du module, puis nom de la fonction à exécuter
    
    function_result = None 
    
    if op == "moy":
        function_result = sum(dico[day])/len(dico[day])
    if op == "range":
        function_result = max(dico[day]) - min(dico[day])
    if op == "min" or op == "max":  
        function_result = getattr(builtins,op)(dico[day])

    print("{}\t{}".format(day,function_result))


