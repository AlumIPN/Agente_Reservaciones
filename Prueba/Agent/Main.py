#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Agent.configs.AI import *


# In[3]:


from Agent.configs.Agents.TypesAg import *


# In[4]:


from swarm.repl import run_demo_loop


# In[5]:


from datetime import datetime


# In[6]:


if __name__ == "__main__":
    run_demo_loop(triage_agent, debug=False, stream=True)


# In[ ]:




