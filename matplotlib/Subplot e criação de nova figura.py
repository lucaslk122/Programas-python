#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[13]:


x = np.linspace(0, 5,11) #Return evenly spaced numbers over a specified interval.


# In[14]:


y = x**2


# In[15]:


plt.plot (x,y)
plt.xlabel ("Eixo X")
plt.ylabel ("Eixo y")
plt.title ("Isso é apenas um treino")


# In[19]:


plt.subplot(1,2,1) #Subplot cria um grafico de x linhas por y colunas, o terceiro parametro significa em qual gráfico vai trabalhar,nesse caso, o primeiro
plt.plot (x,y,'r--')
plt.xlabel("eixo x")
plt.ylabel('eixo y')
plt.title('gráfico 1')
plt.subplot(1,2,2) #agora estou manipulando o segundo gráfico
plt.plot (y,x,'g*-')
plt.xlabel("eixo x")
plt.ylabel('eixo y')
plt.title('gráfico 2')


# In[45]:


fig = plt.figure() #método para criar uma figura
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.3,0.3]) # parametro do tipo (distancia do eixo x,distanca do eixo y,largura,altura)
axes1.plot(x,y,'r--')
axes1.set_xlabel("eixo x")
axes1.set_ylabel('eixo y')
axes1.set_title('gráfico 1')
axes2.plot(y,x,'g*-')
axes2.set_xlabel("eixo x")
axes2.set_ylabel('eixo y')
axes2.set_title('gráfico 2')
plt.grid()


# In[ ]:




