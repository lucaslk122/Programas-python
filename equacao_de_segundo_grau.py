# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:34:11 2019

@author: Lucas
"""

print("programa para calcular as duas raizes de uma equação de segundo grau")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = ((b**2)-(4*a*c))**0.5
if delta == 0:
    x_1 = b/(2*a)
    print ("equação com apenas uma raiz igual a: "+str(x_1))
if delta > 0:
    x_2 = (b + delta)/(2*a)
    x_3 = (b - delta)/(2*a)
    print ("as raizes são "+str(x_2)+" e "+str(x_3))
if delta < 0:
    print("A raiz negatuva, a solução é imaginaria")