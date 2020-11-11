# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:38:27 2019

@author: Lucas
"""

import random
numero = random.randint(0,20)
numero_2 = random.randint(0,20)
if numero > numero_2:
    print (str(numero)+ " é maior que "+str(numero_2))
if numero < numero_2:
    print (str(numero)+ " é menor que "+str(numero_2))
if numero == numero_2:
     print ("os dois numeros são iguais a "+str(numero))