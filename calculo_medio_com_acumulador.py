# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:47:51 2019

@author: Lucas
"""

x = 1
soma = 0
while x <= 5:
    n = int(input("%d Digite o numero: " % x))
    soma = soma + n
    x = x + 1
print("Média: %5.2f" % (soma/5))