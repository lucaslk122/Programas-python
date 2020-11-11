# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

import matplotlib.pyplot as plt
x = [20,40,60,80,100,110]
y = [1,1.75,2.065,2.69,3.75,4.50]
plt.title("Meu primeiro gráfico com python") # titulo
#eixos
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.bar(x,y) # plota o gráfico
plt.show() # exibe i gráfico plotado