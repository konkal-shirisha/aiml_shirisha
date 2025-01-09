#!/usr/bin/env python
# coding: utf-8

# In[31]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter + 1
        sum += x
    mean = sum/counter
    return mean


# In[33]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[35]:


product(10,20,30)


# In[37]:


mean_value(10,20,30)


# In[ ]:




