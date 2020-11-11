# -*- coding: utf-8 -*-
"""
Created on Thu May 28 09:14:03 2020

@author: Lucas
"""

notalab = float(input("Nota do labratório: "))
prova = float(input("Nota da prova: "))
exame = float(input("Nota do exame: "))
media = ((notalab*2) + (prova*3) + (exame*5))/10
if media <= 2.9:
    print(f"Sua média é {media} ,Aluno reprovado!")
elif 5 > media >= 3:
    print(f"Sua média é {media}, alnno recuperação!")
else:
    print(f"Sua média é {media}, aluno aprovado")
