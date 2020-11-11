# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:06:33 2019

@author: Lucas
"""

a = float(input("Dgite a primeira nota: "))
b = float(input("Dgite a segunda nota: "))
m = float((a+b)/2)
if m >= 6:
    print ("A média é "+str(m)+" portanto,está aprovado")
else:
    print ("A média é "+str(m)+" portanto,está reprovado")