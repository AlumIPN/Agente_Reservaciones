#!/usr/bin/env python
# coding: utf-8

# In[1]:


from configs.AI import *


# In[4]:


from swarm import Swarm
from configs.Agents.Data.BDAg import cargar_contexto
from configs.Agents.TypesAg import triage_agent  # agente inicial
import gradio as gr

# Inicializa el cliente
client = Swarm()

def responder(mensaje, historial, agente_actual):
    # Si el usuario pide terminar, se cierra la sesión
    if mensaje.strip().lower() in ["exit", "terminar"]:
        historial.append({"role": "assistant", "content": "Sesión finalizada. ¡Hasta pronto!"})
        demo.close()  # cierra la interfaz
        return historial, historial, triage_agent  # reinicia agente a triage por si se relanza

    # historial: lista de mensajes [{role, content}, ...]
    historial.append({"role": "user", "content": mensaje})

    # Ejecuta con el agente actual
    respuesta = client.run(agent=agente_actual, messages=historial)

    # Actualiza el agente si hubo transferencia
    agente_actual = respuesta.agent
    #(f"Agente activo: {agente_actual}")

    # Extrae el último mensaje del asistente
    contenido = respuesta.messages[-1]["content"]
    historial.append({"role": "assistant", "content": contenido})

    return historial, historial, agente_actual

with gr.Blocks() as demo:
    gr.Markdown("## Chat con historial")

    chatbot = gr.Chatbot()
    entrada = gr.Textbox(label="Escribe tu mensaje")
    enviar = gr.Button("Enviar")

    # Cada sesión inicia con historial vacío y agente triage
    estado = gr.State([])            
    agente = gr.State(triage_agent)  

    enviar.click(
        responder,
        inputs=[entrada, estado, agente],
        outputs=[chatbot, estado, agente]
    )

demo.launch(inline=True)


# In[ ]:




