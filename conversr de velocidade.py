# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:55:22 2020

@author: Lucas
"""

print ("Conversor de unidade de medida")
velocidade = float(input("Digite sua velocidade: "))
print ("""Para qual velocidade pretende converter?
       [1] Para Km/m
       [2] Para m/s""")
opção = int(input("Sua opção: "))
if opção == 1:
    k = velocidade*3.6
    print(f"V = {k} m/s")
else:
    m = velocidade/3.6
    print(f"V = {m} Km/h")
    
    