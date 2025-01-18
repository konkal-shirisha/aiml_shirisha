#!/usr/bin/env python
# coding: utf-8

# In[24]:


a = [1,2,3,4,5]
average = sum (a)/len (a)
print(average)


# In[69]:


def calculate_mean(values):
    if len(values) == 0:
        return None
    else:
        return int(values)/len(values)


# In[71]:


values = [1,2,3,4,5]
mean_value = calculate_mean(values)
print(mean_value)


# In[73]:


from collections import Counter

def find_mode(data):
    counter = Counter(data)
    mode = counter.most_common(1)[0][0]
    return mode

data = [1, 2, 2, 3, 3, 3, 4]
mode = find_mode(data)
print("Mode:", mode)


# In[136]:


def mode_value(L):
    s = set(L)
    d={}
    
    for x in s:
        d[x]= L.count(x)
        
    m = max(d.values())

    
    for k in d.keys():
        if d[k] == m:
            return k


# In[138]:


L = ["M","M","F","M","F","M"]
mode_value(L)


# In[140]:


L1 = [1,2,1,1,2,1]
mode_value(L1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




