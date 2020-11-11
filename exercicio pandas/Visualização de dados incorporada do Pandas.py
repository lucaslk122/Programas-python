#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[66]:


df1 = pd.read_csv("df1",index_col=0)


# In[128]:


df2 = pd.read_csv("df2")


# In[59]:


df1['A'].hist() #metodo para visualizar o histograma de uma coluna


# In[60]:


df2.plot.area()


# In[61]:


df2.plot.bar(stacked=True)


# In[62]:


df1['A'].plot.hist(bins=50)


# In[94]:


df1.plot.scatter(x='A', y="B",s=df1['C']*10)
plt.ylabel("Teste")
plt.xlabel("Outro teste")
plt.title("Teste em massa")


# In[98]:


df2.plot.box()


# In[99]:


df = pd.DataFrame(np.random.rand(1000,2),columns=['A','B'])


# In[102]:


df.head()


# In[119]:


df['A'].std() + df['B'].std()


# In[121]:


df.plot.hexbin(x='A',y='B', gridsize=20)


# In[131]:


df2.plot.kde()


# In[ ]:




