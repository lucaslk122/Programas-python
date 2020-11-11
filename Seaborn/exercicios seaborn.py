#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


sns.set_style('whitegrid')


# In[5]:


titanic = sns.load_dataset('titanic')


# In[6]:


titanic.head()


# In[9]:


titanic.info()


# In[12]:


sns.jointplot(x='fare',y='age',data=titanic)


# In[13]:


sns.distplot(titanic['fare'],bins=30,kde=False,color='red')


# In[14]:


sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')


# In[15]:


sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')


# In[16]:


sns.countplot(x='sex',data=titanic)


# In[17]:


sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')


# In[18]:


g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




