# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

def consulta_cep(cep):
    import requests
    url = 'https://viacep.com.br/ws/%s/json/'%cep
    response = requests.get(url)
    print (response.content)
    type('response.content')
    
if  __name__ == '__main__' :
    consulta_cep('08280180')   
    
