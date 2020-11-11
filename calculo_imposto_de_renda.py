# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
 
print("Calculo do imposto de renda")
salario = int(input("Digite seu salario: "))
if salario < 1868:
    print ("Isento de imposto de renda")
if salario == 1868 and salario < 2799:
    imposto = salario*0.075
    print("Voce vai pagar "+str(imposto)+" de renda")
if salario == 2799 and salario < 3773:
    imposto_1 = salario*0.15
    print("Voce vai pagar "+str(imposto_1)+" de imposto")
if salario == 3775 and salario < 4664:
    imposto_2 = salario*0.225
    print("Voce vai pagar "+str(imposto_2)+" de imposto")
if salario > 4664:
    imposto_3 = salario*0.275
    print("Voce vai pagar "+str(imposto_3)+" de imposto")
