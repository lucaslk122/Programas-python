# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import numpy as np
import pandas as pd

lista1 = [49,46,25,23,21,8,7]
lista2 = ["Josué","Raquel","Lucas","Samuel","Miriam","Pedro","Satah"]
s = pd.Series(data=lista1,index=lista2)
print (s)
df = pd.DataFrame(np.random.randn(5,4),index='A B C D E'.split(),columns='X Y Z L'.split())
print (df)
print (df['X']) #Jeito de buscar o valor das colunas no dataframe que criei 
print (df.loc['D']) #jeito de buscar os valores da linha, para esse exemplo, a linha A
print (df.loc['A','Z']) #metodo para encontrar um valor esecifico, no caso, especifiquei a linha primeiro e depois a coluna para procurar
print (df.loc[['A','B'],['X','Y','Z','L']]) #encontrar parametros, a primeira parte define as linhas,a segunda,as colunas
print (df.iloc[0:2,0:2]) #metodo para localização pelos indicies, primeiro as linas depois as colunas
