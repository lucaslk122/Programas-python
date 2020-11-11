# -*- coding: utf-8 -*-
"""
Created on Fri May 29 08:54:59 2020

@author: Lucas
"""

print("Programa que calcula fatorial")
n = int(input("Digite o numero que quer saber o fatorial: "))
c = n
f=1
while c > 0:
    print(f"{c}", end="")
    print ("x" if c>1 else '=', end="")
    f *= c
    c -= 1
print (f"{f}")    