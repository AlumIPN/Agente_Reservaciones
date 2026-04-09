#!/usr/bin/env python
# coding: utf-8

# In[6]:


from configs.AI import *


# In[7]:


from configs.Agents.TypesAg import *


# In[8]:


from swarm.repl import run_demo_loop


# In[9]:


from datetime import datetime


# In[10]:


if __name__ == "__main__":
    run_demo_loop(triage_agent, debug=False, stream=True)


# In[ ]:




