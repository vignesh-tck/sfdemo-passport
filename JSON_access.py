#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[64]:


### we can have a reference JSON and use that as base
import json  
with open('passport_json_2.json', 'r') as f: 
    data = json.loads(f.read()) 
# since our JSON is complex, use this methos
df1 = pd.json_normalize(data)


# In[65]:


df1.head()


# In[66]:


#populate simple fields directly like this
df1['dataPassportID']=10001


# In[67]:


#for Array fields first assign to list like below
dsAccess=df1['dsAccess'].tolist()


# In[68]:


#this will help access the entire JSON array
print(dsAccess[0])


# In[69]:


#to access first element of the JSON array
print(dsAccess[0][0])
#you will see that it is a dictionary


# In[70]:


#to modify a dictionary value, simply pass the assignment
dsAccess[0][0]["accessMethod"]="SQL"


# In[71]:


#to add a new entry use the append function
dsAccess[0].append({'accessMethod': 'JDBC', 'accessURI': 'Full API URI', 'accessConnector': 'blank'})


# In[72]:


print(dsAccess[0])


# In[73]:


#pass the entire list back to the same JSON node to update it 
df1['dsAccess']=dsAccess


# In[74]:


df1.head()


# In[60]:


#use this to create a new json document and store to the document store
df1.to_json('output_json.json',orient='records')


# In[ ]:




