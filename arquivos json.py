# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
# criando arquivos Json

import json
clientes = '''
            {
             "Pessoas":[
               {"Nome": "Lucas",
               "Endereço":"Rua jeronumo de barros",
               "Número": "179",
               "Idade": "25",
                "bairro": "Cidade Lider",
                "Cidade": "São Paulo"},
             {
               "Nome": "Pedro",
               "Endereço":"Rua jeronumo de barros",
               "Número": "179",
               "Idade": "9",
                "bairro": "Cidade Lider",
                "Cidade": "São Paulo"},
             {
               "Nome": "Sarah",
               "Endereço":"Rua jeronumo de barros",
               "Número": "179",
               "Idade": "7",
                "bairro": "Cidade Lider",
                "Cidade": "São Paulo"},
             {
               "Nome": "Shinji Ikari",
               "Endereço":"Neo Tokyo 3",
               "Número": "001020",
               "Idade": "14",
                "bairro": "Alguma bairro devastado",
                "Cidade": "Tokyo"}]}'''


data = json.loads(clientes)
for pessoa in data['Pessoas']:
    print(pessoa['Nome'], pessoa['Idade'])
    

    
#novo_teste = json.dumps(data)
#print(novo_teste)
