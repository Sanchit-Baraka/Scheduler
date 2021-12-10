#!/usr/bin/env python
# coding: utf-8

# In[55]:


import os
import subprocess
from datetime import date,datetime,timedelta


# In[56]:


today = datetime.today().strftime('%Y-%m-%d')
yesterday = date.today() - timedelta(days = 1)


# In[43]:


id = "KZZ-649-5K6Z"
p = "CVK-SAV-ULUL"
secret = "b5395bc1241151bfd34dbfd97e9e090a"


# In[59]:


eventsCommand = "clevertap-data-upload -id={} -p={} -mixpanelSecret={} -t=event -startDate={} -endDate={}".format(id,p,secret,yesterday,today)


# In[60]:


profileCommand = "./clevertap-data-upload -id {} -p {} -mixpanelSecret {} is on duty.".format(id,p,secret)


# In[61]:


subprocess.check_output(profileCommand)


# In[62]:


subprocess.check_output(eventsCommand)


# In[ ]:




