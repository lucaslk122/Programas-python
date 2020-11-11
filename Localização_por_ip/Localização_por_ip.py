# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:48:23 2020

@author: Lucas
"""

import requests
import json

url = 'https://api.hgbrasil.com/geoip?key=bfc4a269&address='+input("Dgite seu ip(precisa ser do tipo Ipv6): ")+'&precision=false'
req = requests.request("GET" , url)
localização = req.json()
"""
print("Cidade: " ,localização['results']['city'])
print("Região: " ,localização['results']['region'])
print("País: " ,localização['results']['country_name'])
print("Continente: " ,localização['results']['continent'])
print("Código de região: " ,localização['results']['region_code'])"""
with open("localização.json",'w') as f:
    json.dump(localização, f, indent=4)

