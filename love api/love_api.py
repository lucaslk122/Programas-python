# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 11:54:48 2020

@author: Lucas
"""

import requests
HEADERS = {
"x-rapidapi-host": "love-calculator.p.rapidapi.com",
"x-rapidapi-key": "c5d8276104msh528edf745fda7c2p1b667ejsn8eb51714dcf6"
}
url ='https://love-calculator.p.rapidapi.com/getPercentage?fname='+input("Digite seu nome: ")+"&sname="+input("Digite o nome da pessoa que voce gosta: ")
req = requests.request("GET",url,headers=HEADERS)
resultado = req.json()
print("Seu nome: ",resultado["fname"])
print("A pessoa que voce gosta: ",resultado["sname"])
print("Porcentagem de sucesso: ",resultado["percentage"])
print("Resultado: ",resultado["result"])
