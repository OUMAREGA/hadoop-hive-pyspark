#!/usr/bin/env python3
import json
import sys
from pymongo import MongoClient

# Argument attendu : nom de la collection

sys.argv.pop(0)

client = MongoClient("mongodb://mongodb")

db = client["temperatures"]

collection = db[sys.argv[0]]
dico = json.load(sys.stdin)
collection.insert_many(dico)

#print(sys.stdin.readline())
