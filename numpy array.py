# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:55:01 2020

@author: Lucas
"""

import numpy as np
lista = np.random.randint(0,30,10)
print(lista)
lista[2]
arr = np.arange(50).reshape((5,10)) #esta função agrupa numeros de 0 a 50,ordenando em 5 linhas por 10 colunas
print("array = ",arr)
arr3 = np.arange(0,31)
arr4 = arr3 + arr3 #é possivel afzer operações algebricas entre listas,tanto subtração,mutiplicação e divisão
#também é possivel fazer operações algebricas de arrays  com numeros algebricos
print("arr4 = ",arr4) 
arr5 = np.sqrt(arr3)
print ("arr5 = ",arr5)
arr6 = np.mean(arr) #mean tira a média da minha array
print ("arr6 = ",arr6)
arr7 = np.std(arr) #calculo de desvio padrão
print("arr7 = ",arr7)
x = [10,9,7.8,8,2.30,7.8]
y = np.mean(x)
print("Sua média é ",y)