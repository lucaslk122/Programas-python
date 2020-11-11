#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


f = sns.load_dataset('flights')
tips = sns.load_dataset('tips')


# In[33]:


f.head()


# In[21]:


sum(f['passengers'])


# In[28]:


tips.head()


# In[26]:


tips.corr() #Compute pairwise correlation of columns, excluding NA/null values.


# In[30]:


f['year'].max()


# In[36]:


sns.heatmap(tips.corr(),annot=True) #annot mostra os valores que estõa dentro de cada quadrado


# In[54]:


v = f.pivot_table(values='passengers',index='month',columns='year')
#(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', 
#observed=False) 
#Create a spreadsheet-style pivot table as a DataFrame.

#The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and 
#columns of the result DataFrame.


# In[55]:


sns.heatmap(voos)


# In[61]:


sns.heatmap(v,cmap='magma',linecolor='gray',linewidths=1)


# In[ ]:




