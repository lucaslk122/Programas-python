# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

print ("Porgrama para converter bases númericas")
numero  = int(input("Digite um numero inteiro a ser convertido: "))
print("""Digite uma opção de conversão:
              [1] para binario
              [2] para octal
              [3] para hexadecima""")
opção = int(input(f"Sua opção: "))
if opção == 1:
    print(f"{numero} em binário é {bin(numero)[2: ]}")
elif opção == 2:
    print (f"{numero} em octal é {oct(numero)[2: ]}")
elif opção == 3:
    print (f"{numero} em hexadecimal é {hex(numero)[2: ].upper()}")
else:
    print("opção invalida,tente novamente")