import json
clientes = '''
            {
             "Pessoas":[
               {"Nome": "Lucas",
               "Endereço":"Rua jeronumo de barros",
               "Número": "179",
                "bairro": "Cidade Lider",
                "Cidade": "São Paulo"},
             {
               "Nome": "Pedro",
               "Endereço":"Rua jeronumo de barros",
               "Número": "179",
                "bairro": "Cidade Lider",
                "Cidade": "São Paulo"},
             {
               "Nome": "Sarah",
               "Endereço":"Rua jeronumo de barros",
               "Número": "179",
                "bairro": "Cidade Lider",
                "Cidade": "São Paulo"},
             {
               "Nome": "Shinji Ikari",
               "Endereço":"Neo Tokyo 3",
               "Número": "001020",
                "bairro": "Alguma bairro devastado",
                "Cidade": "Tokyo"}
               ]}'''

data = json.loads(clientes)
for pessoa in data['Pessoas']:
    print(pessoa['Nome'])

