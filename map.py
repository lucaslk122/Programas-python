# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:38:29 2020

@author: Lucas
"""
import math

def area(r):
    return math.pi*(r**2)
raios = [2.2,2.4,5,6,3.6,2.6]
#map é uma função que recebe dois parametros, o primeiro é uma função, o segundo é um iteravel
#retorna um objeto map, que podemos converter para o que quisermos
areas = map(area,raios)
print(list(areas))

#map com lambda
print(list(map(lambda r: math.pi*(r**2),raios)))
#Apos utilizar a função map depois da primeira utilização do resultado, ele zero
