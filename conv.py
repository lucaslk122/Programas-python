# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
aniversario = int(input("É seu aniversario? responda 1 para sim e 2 para não "))
guarda = int(input("Um guarda parou voce, qual sua velocidade? "))
if aniversario == 1:
    if guarda < 65:
        print ("Sem multa")
    elif (guarda == 65) and (guarda <= 85):
        print ("Multa pequena")
    else:
        print("Multa grande")
if aniversario == 0:
    if guarda < 60:
        print ("Sem multa")
    elif (guarda == 60) and (guarda <= 80):
        print ("Multa pequena")
    else:
        print("Multa grande")
 
