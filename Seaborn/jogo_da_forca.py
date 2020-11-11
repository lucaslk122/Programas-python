# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

palavra = input("Digite a palavra secreta: ").lower().strip()
for X in range(100):
    print()
digitadas =  []
acertos = []
erros = 0
while 1:
    senha=""
    for letra in palavra:
        senha +=letra if letra in acertos else "."
        print(senha)
    if senha == palavra:
        print("Voce acertou")
        break
    tentativa = input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print ("Voce já tentou essa palavra")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print ("Voce errou")
    print("X==:==\nX : ")
    print ("x o " if erros >=1 else "X")
    linha2=""
    if erros == 2:
        linha2 = " | "
    elif erros == 3:
        linha2 = " \| "
    elif erros == 4:
        linha2 = " \|/ "
        
    print("X%s" % linha2)
    linha3=""
    if erros == 5:
        linha3+= " /  "
    elif erros>=6:
        linha3+=" / \ "
    print ("X%s" % linha3)
    print ("X\n===========")
    if erros == 6:
        print ("Enforcado")
        break
    