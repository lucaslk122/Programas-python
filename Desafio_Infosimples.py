# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

from itertools import combinations
lista = eval ("["+ input("Digite os preços dos sorvetes: ") +"]")
print(f"L = {lista}")
M = int(input("Digite a quantidade de dinheiro que voce tem: "))
print(f"M = {M}")
combinação = [x[0]+x[1] for x in combinations(lista,2)]
print (combinação)
if M in combinação:
    print("Voce pode comprar os dois sorvetes")
else:
    print("Voce não pode comprar os sorvetes")
