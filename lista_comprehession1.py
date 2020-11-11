""" 
Para fazer uma list comprehesion, usamos a seguinte sintaxe:
[dado for dado in iteravel]
"""
"""
#Exemplo 1
numeros = [1,2,3,4,5]
res = [teste*10 for teste in numeros] #para cada numeros contido em numeros,pegue esse numero e multiplique por 10
print(res)
"""
"""
#exemplo 2
numeros = [10,20,30,50,8]
numeros_dobrados = [(numeros/2)*10 for numeros in numeros]
print(numeros_dobrados)
"""
"""
#exemplo 3
nome = ['lucas samofalov diniz']
tantofaz = [letra.upper() for letra in nome]
print(tantofaz)
"""
"""
#exemplo 4
def caixa_alta(nome):
    nome = nome.replace(nome[0],nome[0].upper()) #vai pegar o nome e realocar de lugar,com apenas a primeira letra da palavra
    return nome
amigos = ["lucas", 'samantha','rebecca','clara']
print([caixa_alta(amigo) for amigo in amigos])
"""
