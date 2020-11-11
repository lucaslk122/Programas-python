#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd


# In[3]:


tips = sns.load_dataset('tips')


# In[24]:


tips.info()
tips.head()


# In[25]:


tips[tips['sex']=='Female'].shape


# In[8]:


tips['total_bill'].mean()


# In[10]:


barplot e countplot
Esses plots parecidos permitem que você obtenha dados agregados de um recurso categórico. ** barplot ** é 
um gráfico geral que permite que você agregue os dados 
categóricos baseados em alguma função, por padrão, a média:


# In[12]:


sns.barplot(x = 'sex',y = 'total_bill' , data = tips, estimator=np.std) #estimator está calculando o desvio padrão


# In[13]:


sns.countplot(x='sex',data=tips)


# In[28]:


sns.boxplot(x='day',y='total_bill',data=tips)


# In[30]:


sns.boxplot(x='day',y='total_bill',data=tips, hue='sex') #huename of variables in data or vector data, optional
#Grouping variable that will produce points with different colors. Can be either categorical or numeric, 
#although color mapping will behave differently in latter case.


# In[37]:


sns.violinplot(x='day',y='tip',data=tips, hue='sex', split=True, palette='Set1')
#A violin plot plays a similar role as a box and whisker plot. 
#It shows the distribution of quantitative data across several levels of one (or more) categorical variables 
#such that those distributions can be compared. Unlike a box plot, in which all of the plot components correspond 
#to actual datapoints, the violin plot features a kernel density estimation of the underlying distribution.


# In[40]:


#stripplot e swarmplot
#O stripplot irá desenhar um scatterplot onde uma variável é categórica. Um stripplot pode ser desenhado por conta própria,
#mas também é um bom complemento para uma boxplot ou violinplot nos casos em que você deseja mostrar todas as 
#observações juntamente com alguma representação da distribuição subjacente.

#O swarmplot é semelhante ao stripplot (), mas os pontos são ajustados (somente ao longo do eixo categórico) para 
#que eles não se sobreponham. Isso dá uma melhor representação da distribuição de valores, embora não se ajuste 
#também a um grande número de observações (tanto em termos de capacidade de mostrar todos os pontos quanto em 
#termos da computação necessária para organizá-los).


# In[53]:


sns.stripplot(x='day',y='total_bill',data=tips)


# In[57]:


sns.swarmplot(x="day", y="total_bill",hue='sex',data=tips, palette="Set1", split=True)


# In[ ]:




