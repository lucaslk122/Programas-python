# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:42:41 2020

@author: Lucas
"""
print("Programa que mostra o dia da semana correspondente a um inteiro de 1 a 7")
dia = int(input("Digite de 1 a 7: "))
if dia == 1:
    print("Domingo")
elif dia ==2:
    print("Segunda-feira")
elif dia ==3:
    print("Terça-feira")
elif dia ==4:
    print("Quarta-feira")
elif dia ==5:
    print("Quinta-feira")
elif dia ==6:
    print("Sexta-feira")
elif dia ==7:
    print("Sabado")
else:
    print("Dia invalido, digite outro!")
