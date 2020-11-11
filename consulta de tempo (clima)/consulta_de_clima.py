# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:05:51 2020

@author: Lucas
"""

#API para consulta de tempo
"""
Acessamos os valores de um dicionario, passando o nome da chave, e para acessar
os valores de uma lista, passamos o indice que queremos saber o valor
"""
import requests

url = 'https://api.hgbrasil.com/weather?key=bfc4a269&city_name='+input("Digite o nome da cidade: ")
req = requests.request("GET", url)
tempo = req.json()
print("Cidade: ",tempo['results']['city'])
print("Temperatura: ",tempo['results']['temp'])
print("Data: ",tempo['results']['date'])
print("Hora: ",tempo['results']['time'])
print("Temperatura: ",tempo['results']['temp'])
print("Descrição: ",tempo['results']['description'])
print("Humidade: ",tempo['results']['humidity'],"%")
print("Velocidade dos ventos: ",tempo['results']['wind_speedy'])
print("Dia: ",tempo['results']['forecast'][0]['weekday'])
print("máxima: ",tempo['results']['forecast'][0]['max'])
print("minima: ",tempo['results']['forecast'][0]['min'])











