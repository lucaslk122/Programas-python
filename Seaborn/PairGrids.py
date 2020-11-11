#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# In[10]:


iris.head()


# In[11]:


iris['species'].value_counts()


# In[12]:


g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[16]:


g = sns.FacetGrid(tips, col="time",  row="smoker")
g = g.map(plt.hist, 'total_bill')


# In[ ]:




