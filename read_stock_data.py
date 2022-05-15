#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[9]:


data = pd.read_csv("data/data/AAPL.csv")


# In[10]:


data.tail()


# In[11]:


type(data)


# In[12]:


data.plot()


# In[13]:


data.dtypes


# In[16]:


type(data[['Adj. Close']])


# In[17]:


data['Adj. Close'].plot()


# In[ ]:




