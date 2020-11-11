# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
import matplotlib.pyplot as plt
 
x = [366,405,436,492,546,579]
y = [0.24,0.36,0.62,0.93,1.15,1.48]
plt.xlim(300,600)
plt.ylim(0.2,1.6)
plt.plot(x,y, color='k' , marker = 'o' )
plt.xlabel("Frequencia de onda [nm]")
plt.ylabel("Potencial de corte [V]")
plt.grid()
plt.show()