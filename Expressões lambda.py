# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

"""
expressões lambda
calc = lambda x: (x**2) + (20-10)
x = int(input("valor de x: "))
print(calc(x))
"""

"""
nome_completo = lambda nome,sobrenome: nome.strip().title()+" "+sobrenome.strip().title()
#strip retira os espaços que eventualmente alguem pode colocar entre as palavras,pode ser
#no inicio ou no fim da palavra
nome = str(input("Seu nome: "))
sobrenome = str(input("Seu sobrenome: "))
print(nome_completo(nome, sobrenome))
"""

"""
amar = lambda: "como não amar python"
uma = lambda x : x**2
duas = lambda x : x**3
tres = lambda x : (x**3)**(x+7)
print(amar())
print(uma(10))
print(duas(5))
print(tres(5))
Se passarmos parametros mais do que declaramos no lambda, teremos um typeerror
"""

"""
autores = ["Hayao Miazaki" , "Lucas Samofalov", "Arthur C Clark", "Kentaro miura",
           "Kite Kubo", "Ada Lovelace", "Yoshihiro Togashi"]
autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(autores)
"""

