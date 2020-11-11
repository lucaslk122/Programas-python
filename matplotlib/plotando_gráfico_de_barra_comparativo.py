# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

import matplotlib.pyplot as plt

x = [30,50,70,90,100,110,120,130]
y = [0.182,0.247,0.322,0.404,0.456,0.523,0.626,0.773]
plt.plot(x,y,color='b',marker='x')
plt.title("transformador em vazio de Fe")
plt.xlabel("Tensão no primario[V]")
plt.ylabel("Corrente no primario[A]")
plt.grid()
plt.show()