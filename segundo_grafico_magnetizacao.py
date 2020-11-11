# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:26:10 2019

@author: Lucas
"""

import matplotlib.pyplot as plt
x3 = [0.16,0.34,0.45,0.60,0.75,0.80] #corrente com entre ferro 60hz
y = [0.112,0.225,0.338,0.450,0.564,0.620] # sem enre ferro 60hz
x = [0.016,0.028,0.033,0.043,0.060,0.072] # corrente sem entre ferro 60hz
y2 = [0.135,0.270,0.406,0.541,0.676,0.744] #sem entre ferro 50hz
x1 = [0.012,0.021,0.027,0.033,0.040,0.044] #corrente sem entre ferro 50 hz
x2 = [0.105,0.205,0.303,0.396,0.490,0.546] #corrente com entre ferro 50hz
plt.grid('true')
plt.title("Fluxo magnetico em função da corrente") # titulo
#eixos
plt.xlabel("Corrente [A rms]")
plt.ylabel("Fluxo Φ (10^-3)Wb")
plt.plot(x,y,  label= "sem entre ferro[60Hz]", color="red")
plt.plot(x3,y, label= "com entre ferro[60Hz]", color="k")
plt.plot(x1,y2, label= "sem entre ferro[50Hz]", color="m")
plt.plot(x2,y2, label= "com entre ferro[50Hz]", color="g")
plt.legend()
plt.show() # exibe o gráfico plotado 