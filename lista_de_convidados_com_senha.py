# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:09:01 2019

@author: Lucas
"""
x = 1
y = 1
lista = input("Digite os usuarios cadastrados: ")
print("Lista de convidados autorizados = {} ".format(lista))
a = input("Digite o nome de usuario: ")
while x == 1:
    if a in lista:
        print(a+ " está na lista, vá para o proximo passo")
        x = 0
    else:
        print(a+" não esta na lista")
        a = input("Digite o nome novamente: ")
b = int(input("Digite uma senha de usuario: "))
print("Senha configurada")
c= int(input("Por favor, digite a senha: "))
while y == 1:
    if b == c:
        print("Senha correta, seja vem vindo, Sr(a) "+a)
        y = 0
    else:
        c = int(input("Senha incorreta, digite novamente: "))