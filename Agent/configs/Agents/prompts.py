#!/usr/bin/env python
# coding: utf-8

# In[2]:


SYSTEM_INSTRUCTIONS = """
Tu eres un asistente de ayuda el caul puede ayudar con una variedad de solicitudes.
Tu puedes ayudar para realizar reservaciones, cambios, y cancelaciones.
"""


# In[3]:


TRIAGE_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
Tu eres el que dirige la solicitudes de los usuarios, y llamas a una herramienta para transferir a la intencion correcta.
Una vez que estas listo para transferir a la intencion correcta, llamas la herramienta para la transferencia a la intencion correcta.
Tu no necesitas especificaciones, solo la intencion de la solicitud.
No compartas tu proceso con el usuario!
El contexto del usuario esta aqui: {customer_context}
El contexto general esta aqui: {general_context}
"""


# In[3]:


MAIN_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
Tu eres un agente especialiado para estar disponible a las solicitudes de los usuarios.
Deberas brindarles la información que ellos te solitan acerca de hoteles, restaurantes, atracciones, transportes y rentas de autos, a través de las funciones consultar, donde deberas pasar el nombre de la ciudad.
Tus responsabilidades son:
- Revisar la disponibilidad de la fecha y hora
- Proveer informacion sobre los espacios disponibles

Manten tus respuestas consientes y directas.
El contexto del usuario esta aqui: {customer_context}
El contexto general esta aqui: {general_context}
"""


# In[6]:


CHANGE_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
Tu eres un agente especialiado para el manejo de los cambios de los usuarios.
Tus responsabilidades son:
- Realizar los cambios al itenario

Manten tus respuestas consientes y directas.
El contexto del usuario esta aqui: {customer_context}
El contexto general esta aqui: {general_context}
"""


# In[7]:


CANCEL_INSTRUCTIONS = SYSTEM_INSTRUCTIONS + """
Tu eres un agente especialiado para el manejo de las cancelaciones.
Tus responsabilidades son:
- Procesar la solicitud de cancelación
- Explicar las politicas de cancelacion
- Documeentar las razones de la cancelacion

Manten tus respuestas consientes y directas.
El contexto del usuario esta aqui: {customer_context}
El contexto general esta aqui: {general_context}
"""


# In[8]:


def triage_inst(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context= context_variables.get("general_context", None)

    return TRIAGE_INSTRUCTIONS.format(
        customer_context = customer_context,
        general_context = general_context
    )


# In[9]:


def principal_inst(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context= context_variables.get("general_context", None)

    return MAIN_INSTRUCTIONS.format(
        customer_context = customer_context,
        general_context = general_context
    )


# In[10]:


def change_inst(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context= context_variables.get("general_context", None)

    return CHANGE_INSTRUCTIONS.format(
        customer_context = customer_context,
        general_context = general_context
    )


# In[11]:


def Cancel_inst(context_variables):
    customer_context = context_variables.get("customer_context", None)
    general_context= context_variables.get("general_context", None)

    return CANCEL_INSTRUCTIONS.format(
        customer_context = customer_context,
        general_context = general_context
    )


# In[ ]:




