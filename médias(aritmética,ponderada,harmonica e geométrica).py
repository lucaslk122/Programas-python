# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:03:08 2020

@author: Lucas
"""

import math
print ("Calculo de médias")
num1 = int(input("Digite um numero inteiro e positivo: "))
num2 = int(input("Digite um numero inteiro e positivo: "))
num3 = int(input("Digite um numero inteiro e positivo: "))
print("""Digite uma opção de conversão:
              [1] Geométrica
              [2] Ponderada
              [3] Harmonica
              [4] Aritimética""")
opção = int(input("Digite a opção desejada: "))
if opção == 1:
    geometrica = math.pow((num1*num2*num3), 1/3)
    print(f"Média geométrica = {geometrica}")
elif opção == 2:
    ponderada = (num1 + 2*num2 + 3*num3)/6
    print (f"Média ponderada = {ponderada}")
elif opção == 3:
    harmonica = 1/ ((1/num1)+(1/num2)+(1/num3))
    print(f"Harmonica = {harmonica}")
elif opção == 4:
    arimética = (num1 + num2 + num3)/3
    print(f"arimética = {arimética}")
else:
    print("Opção invalidade, tente novamente!")