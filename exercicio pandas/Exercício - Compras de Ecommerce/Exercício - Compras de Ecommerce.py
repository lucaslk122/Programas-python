#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[32]:


ecom = pd.read_csv('Ecommerce Purchases.csv')


# In[6]:


ecom


# In[7]:


ecom.info()


# In[8]:


ecom['Purchase Price'].mean()


# In[9]:


ecom['Purchase Price'].max()


# In[10]:


ecom['Purchase Price'].min()


# In[14]:


ecom[ecom['Language']=='en'].count()


# In[33]:


ecom[ecom['Job']=='Lawyer'].shape


# In[19]:


ecom['AM or PM'].value_counts()


# In[34]:


ecom['Job'].value_counts().head(5)


# In[51]:


ecom[ecom['Lot'] == '90 WT'][['Purchase Price','Email']]


# In[52]:


ecom[ecom['Credit Card'] == 4926535242672853] #quem é o dono do cartão de crédito com  o numer mencionado


# In[56]:


ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price']>95)].shape #quantas pessoas tem o cartão american express e fez uma compra maior que 95


# In[59]:


sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25') #quantas pessoas em o cartão de crédito que vence em 2025


# In[63]:


print (ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)) # 5 amils mais usados


# In[ ]:




