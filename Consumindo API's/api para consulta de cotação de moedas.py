# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:16:08 2020

@author: ldiniz
"""

# Programa para procurar padrões de palavras em email

import requests
import json

moeda = requests.get('https://economia.awesomeapi.com.br/json/all')
cotação = json.loads(moeda.text)

print ("$$$ cotação $$$$")

print("Dolar: " ,cotação['USD']['high'])
print("EUR: " ,cotação['EUR']['high'])
print("GBP: " ,cotação['GBP']['high'])