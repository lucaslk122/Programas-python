# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:06:36 2020

@author: Lucas
"""

print("Calculo de aposentadoria")
idade = int(input("Digite sua idade: "))
tempo_serviço = int(input("Digite seu tempo de serviço (em anos): "))
if idade>=65 or tempo_serviço >=30 or (tempo_serviço >=25 and idade >= 60 ):
    print("Voce pode se aposentar")
else:
    print("Não pode se aposesntar")
    