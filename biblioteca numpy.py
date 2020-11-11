# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
lista = np.arange(0,10) #arange cria sequencia de numeros, do tipo (start,stop,step)
print("lista = ",lista)
lista2 = lista[lista%2==0] 
print("lista2= ",lista2)
lista3 = np.zeros((3,5)) #para fazer uma matriz, é necessario que seja utilizado uma tupla,e os parametros são o tamanho
#da linhas e colunas
print("lista3 = ",lista3)
lista5 = np.eye(4) #método para criar matriz identidade
print("lista5 = ",lista5)
lista6 = np.random.rand(5) #Cria uma lista de numeros aleatórios(a quantidade de numeros vai especificado nos parentes)
#e esses numeros vão de 0 a 1, igualmente espaçados entre si
print("lista6 = ",lista6)
lista7 = np.random.rand(2,2) # cria uma matriz 22x2 de numeros aleaórios comprendidos entre 0 e 1
print("lista7 = ",lista7)
x = np.random.randint(0,20,10) #cria uma lista aleatória do tipo (start,intervalo de numeros, tamanho da lista)
print("x = ",x)
lista8 = np.max(x) #mostra qual é o maior numero da lista
print("lista8 =  ",lista8)
lista9 = np.min(x) #mostra qual é o menor numero da lista
print("lista9 = ",lista9)