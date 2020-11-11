#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[3]:


tips = sns.load_dataset('tips')


# In[5]:


tips.info()


# In[16]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['v','x']) #lineariza uma regressão linear


# In[17]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex') #separa em dois gráficos diferentes


# In[ ]:




