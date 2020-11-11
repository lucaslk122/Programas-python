# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:09:01 2019

@author: Lucas
"""
x = 1
y = 1
a = input("Digite o nome do convidado: ")
minha_lista = ["sarah", "pedro","samuel","lucas", "miriam"]
while x == 1:
    if a in minha_lista:
        print(a+ " está na lista, seja bem vindo")
        x = 0
    else:
        print("o nome não esta na lista\n")
        a = input("Digite o nome do convidado: ")
b = int(input("Digite uma senha de usuario"))
