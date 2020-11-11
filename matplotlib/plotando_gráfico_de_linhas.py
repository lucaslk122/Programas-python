# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

import matplotlib.pyplot as plt
x = [1,2,3,5,5]
y = [2,3,7,1,0]
plt.title("Meu primeiro gráfico com python") # titulo
#eixos
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.bar(x,y) # plota o gráfico
plt.show() # exibe i gráfico plotado