## Réchauffement climatique

Ce projet a été réalisé à partir d'outils du big data (*Hadoop MapReduce*,*MongoDB*) sous une stack Docker. L'objectif est de pouvoir récupérer les données de la NOAA afin de pouvoir procéder à des analyses et déterminer les critères qui peuvent expliquer le réchauffement climatique.

### Répertoire Map Reduce

Ici se trouve toutes les opérations d'agrégation sur les données de la NOAA

Le mapper étant générique, il peut interpréter n'importe quelle colonne des données CSV.
Il faut renseigner dans l'ordre donné, les colonnes souhaitées.

Rappel commande : `cat <fichier> | ./mapper.py <colonnes séparées avec espace> | ./<reducer> <critère>`

Rappel des colonnes :

- STATION
- DATE
- SOURCE
- LATITUDE
- LONGITUDE
- ELEVATION
- NAME
- REPORT_TYPE
- CALL_SIGN
- QUALITY_CONTROL
- WND
- CIG
- VIS
- TMP
- DEW
- SLP
- KA1
- KA2
- MA1
- MD1
- OC1
- OD1
- OD2
- REM
- EQD

### Opérations

- Calcul de température par jour :
  - Reducer : ` temp_jour.py` 
  - Colonnes : DATE, TMP
  - Critères :

| Critère | Description | 
| ------- | :----------:|
|  `max`  |  Température maximale | 
|  `min`  |  Température minimale |
|  `moy`  |  Température moyenne  |  
|  `range`|  Écart de température (max - min) |



- Calcul de température **par longitude/latitude** : 
  - Reducer : ` temp_lat.py` 
  - Colonnes : LATITUDE, LONGITUDE, TMP
  - Critères possibles : idem qu'au dessus

- Calcul de la moyenne des températures **par station météorologique** 
  - Reducer : `temp_avg.py` 
  - Colonnes : STATION, TMP

### Commandes

Les jobs MapReduce sont à lancer dans des nodes du cluster Hadoop :

1. Il faut accéder à un des services docker (`namenode`, ` datanode`, `resourcemanager`) : `docker-compose exec <service> bash`

2. Commande pour exécuter un job sur Hadoop :
`yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.4.jar -files /map_reduce/mapper.py,/map_reduce/temp_jour.py -mapper "./mapper.py <colonnes>" -reducer "./<reducer>" -input /user/hadoop/data/*.csv -output <destination>`

D'autres exemples de commandes pour manipuler le HDFS se trouvent dans le fichier `commands.txt`