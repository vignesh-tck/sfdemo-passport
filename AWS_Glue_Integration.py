#!/usr/bin/env python
# coding: utf-8

# In[104]:


import boto3

client = boto3.client('glue')


# In[110]:


#define object
    glue = boto3.client(
    service_name='glue',
    aws_access_key_id='access key', #give access key from your account
    aws_secret_access_key='secret key' #give secret key from your account
    )


# In[112]:


#pass on table name and get all metadata about the table
response1 = glue.get_table(
    DatabaseName="claimsrepo",
    Name="claim1_json" 
)


# In[119]:


#pretty print to see the dictionary 
import pprint


# In[121]:


pp = pprint.PrettyPrinter(indent=4)


# In[123]:


#print the response to see how Glue response looks like
pp.pprint(response1)


# In[128]:


#list columns in the glue table
print(response1[ 'Table']['StorageDescriptor']['Columns'])


# In[115]:


#start Crawler to catalog new tables
response = glue.start_crawler(
    Name='Claims_Repo'
)
#if no new tables are there, nothing will be udpated. This needs to be scheduled on run time or once a day depending on what we need


# In[ ]:




