# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:50:02 2020

@author: Lucas
"""

print("Programa de calculo matematico")
print("""Digite a opção desejada
      [1] para Soma
      [2] para subtração
      [3] para divisão
      [4] para multiplicação""")
opção = int(input("Sua opção: "))
if opção == 1:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    soma = num1 + num2
    print(f"A soma de {num1} e {num2} é {soma}")
elif opção == 2:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    subtração = num1 - num2
    print(f"A subtração de {num1} e {num2} é {subtração}")
elif opção == 3:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    divisão = num1 / num2
    print(f"A subtração de {num1} e {num2} é {divisão}")
elif opção == 4:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    multiplicação = num1 * num2
    print(f"A subtração de {num1} e {num2} é {multiplicação}")
else:
    print("Sopção invalida")