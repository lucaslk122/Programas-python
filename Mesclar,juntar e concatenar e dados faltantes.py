# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:14:09 2020

@author: Lucas
"""
import numpy as np
import pandas as pd
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])
df4 = pd.concat([df1,df2,df3]) #Concatenação basicamente cola DataFrames. Tenha em mente que as dimensões devem corresponder 
#ao longo do eixo que você está concatenando. Você pode usar ** pd.concat ** e passar uma lista de DataFrames para 
#concatenar juntos:
print (df4)
esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
direita = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})    
df5 = pd.merge(esquerda,direita,how='inner',on='key') #A função ** mesclar ** permite que você mescle os quadros de dados 
#juntos usando uma lógica semelhante à mesclagem de tabelas SQL juntas.une dataframes dado que eles compartilhem algo em comum
print (df5)
esquerda1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
direita1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})
df6 = pd.merge(esquerda1,direita1, on = ['key1','key2'])#outro exemplo de como mesclar dadtaframes com alguuns dados em comum
print (df6)
esquerda2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

direita2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
df6 = esquerda2.join(direita2) #Juntar é um método conveniente para combinar as colunas de dois DataFrames 
#indexados potencialmente diferentes em um único resultado DataFrame.
print (df6)
df7 = df6.fillna(value=20) # substitui valores não encontrados como "NaN por aquele valor que especifiquei
print (df7)