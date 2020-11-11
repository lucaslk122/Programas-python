# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

import matplotlib.pyplot as plt
y1 = [10,21.3,28.2,37.5,46,9,50]
x = [20,40,60,80,100,110]
x1 = [20,40,60,80,100,110]
y = [1,1.75,2.065,2.69,3.75,4.50]
plt.title("Fluxo magnetico em função da tensão") # titulo
#eixos
plt.xlabel("Tensão [V]")
plt.ylabel("Fluxo Φ (10^-7)Wb")
plt.plot(x , y, label= "sem entreferro", color="red", maker='*')
plt.plot(x1 , y1, color="b", label= "com entreferro")
plt.legend()
plt.show() # exibe i gráfico plotado 