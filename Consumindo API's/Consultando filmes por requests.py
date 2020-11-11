# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import requests
import json
requisição = requests.get('http://www.omdbapi.com/?apikey=617c4dc1&&t='
                        +input("Digite o nome do filme: "))
dicionario = json.loads(requisição.text)
print ('Titulo: ', dicionario['Title'])
print ('Ano: ', dicionario['Year'])
print ('Gebnero: ', dicionario['Genre'])
print ('Diretor: ', dicionario['Director'])
print ('Nota: ', dicionario['imdbRating'])




