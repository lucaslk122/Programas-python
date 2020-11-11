#!/usr/bin/env python
# coding: utf-8

# In[33]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# In[34]:


fig = plt.figure()
axes1 = fig.add_axes([0,0,1,1])
plt.plot(x,y)


# In[ ]:





# In[40]:


fig2 = plt.figure()
axes1 = fig2.add_axes([0,0,1,1])
axes2 = fig2.add_axes([0.2,0.5,0.2,0.2])
axes1.plot(x,y,'r')
axes2.plot(x,y,'r')


# In[ ]:





# In[56]:


fig3 = plt.figure()
axes3 = fig3.add_axes([0,0,1,1])
axes4 = fig3.add_axes([0.2,0.5, .4, .4])
axes3.plot(x,z)
axes3.set_xlabel("eixo x")
axes3.set_ylabel('eixo z')
axes3.set_xlim([0,100])
axes3.set_ylim([0,10000])
axes4.plot(x,y)
axes4.set_xlabel("eixo x")
axes4.set_ylabel('eixo y')
axes4.set_title("zoom")
axes4.set_xlim([20,22])
axes4.set_ylim([30,50])


# In[59]:


plt.subplot(1,2,1)
plt.plot(x,y,'b--',lw=3)
plt.xlim(0,100)
plt.ylim(0,200)
plt.subplot(1,2,2)
plt.plot(x,z,'r',lw=3)
plt.xlim(0,100)
plt.ylim(0,10000)


# In[60]:


fig,ax = plt.subplots(1,2) #outro jeito de fazer o gráfico acima, de um jeito mais rápido
ax[0].plot(x,y,'b--',lw=3)
ax[0].set_xlim(0,100)
ax[0].set_ylim(0,200)
ax[1].plot(x,z,'r',lw=3)
ax[1].set_xlim(0,100)
ax[1].set_ylim(0,10000)


# In[68]:


fig,ax = plt.subplots(1,2,figsize=(13,2)) #outro jeito de fazer o gráfico acima, de um jeito mais rápido
ax[0].plot(x,y,'b',lw=5)
ax[0].set_xlim(0,100)
ax[0].set_ylim(0,200)
ax[1].plot(x,z,'r--',lw=3)
ax[1].set_xlim(0,100)
ax[1].set_ylim(0,10000)


# In[ ]:




