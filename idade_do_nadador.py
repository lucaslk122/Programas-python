# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:52:59 2020

@author: Lucas
"""

print("Idade do nadador")
idade = int(input("Digite sua idade: "))
if 7 >= idade >= 5:
    print("Infantil A")
elif 10 >= idade >=8:
    print ("Infantil B")
elif 13 >= idade >=11:
    print ("Juvenil A")
elif 17 >= idade >=14:
    print ("Juvenil B")
elif idade <= 4:
    print("Voce não tem idade para nadar")
else:
    print ("Senior")
