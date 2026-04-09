#!/usr/bin/env python
# coding: utf-8

# In[2]:


from swarm import Agent


# In[3]:


from configs.Agents.prompts import *


# In[4]:


from configs.Agents.Data.context_variables import *


# In[5]:


from configs.Agents.Data.BDAg import *


# In[ ]:


from configs.Tools.Places import *


# In[ ]:


from configs.Tools.Clima import *


# In[6]:


from configs.Tools.switch import *


# In[7]:


main_Agent = Agent(
    name = "Principal Agent",
    instructions= principal_inst(context_variables),
    functions= [
        consultar,
        buscar_vuelos,
        reservar,
        itinerario,
        obtener_pronostico,
        switch_change_ag,
        switch_cancel_ag
        #consultar_hoteles,
        #consultar_atracciones,
        #consultar_autos,
        #consultar_transportes
     
    ]
    
)


# In[8]:


change_Agent = Agent(
    name = "Change Agent",
    instructions= change_inst(context_variables),
    functions= [
        switch_main_ag,
        switch_cancel_ag,
        actualizar
 
    ]
    
)


# In[9]:


cancel_Agent = Agent(
    name = "Cancel Agent",
    instructions= Cancel_inst(context_variables),
    functions= [
        switch_main_ag,
        switch_change_ag,
        cancelar_reserva
 
    ]
    
)


# In[10]:


triage_agent = Agent(
    name = "Main Agent",
    instructions= triage_inst(context_variables),
    functions= [
        consultar,
        switch_main_ag,
        switch_change_ag,
        switch_cancel_ag
    ]
    
)


# In[ ]:





# In[ ]:




