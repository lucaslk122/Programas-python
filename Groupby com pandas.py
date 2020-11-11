# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:53:36 2020

@author: Lucas
"""

import pandas as pd
data = {'Empresa':['Google','Google','Vita','Vita','Fei','Fei'], 
        'Nomes':['Lucas','Samuel','Sarah','Pedro','Raquel','Roberto'],
        'Vendas':[200,300,400,500,150,800]} #dicionario
df = pd.DataFrame(data)
print (df)
group = df.groupby('Empresa') #metodo para agrupar tdos os elementos da coluna especficada
print (group.sum()) #Soma de todos os elementos que possuem a mesma string ,no caso que usei, foi para Empresa
print (group.describe())
print (group.sum().loc['Fei']) #total de vendas da empresa Fei
print (group.sum().loc['Vita'])
print (group.sum().loc['Google'])