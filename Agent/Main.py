
"""
Módulo principal de ejecución de la interfaz conversacional multiagente.

Este script inicializa la aplicación basada en Gradio y gestiona la
interacción entre el usuario y la arquitectura multiagente utilizando
la librería Swarm.

Funcionalidades principales:
- Inicialización del cliente Swarm.
- Gestión del historial conversacional.
- Transferencia dinámica entre agentes especializados.
- Interfaz gráfica para interacción en tiempo real.
- Finalización controlada de sesión.

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

from configs.AI import *

from swarm import Swarm
from configs.Agents.Data.BDAg import cargar_contexto
from configs.Agents.TypesAg import triage_agent
import gradio as gr


# ============================================================================
# Inicialización del cliente principal
# ============================================================================

"""
Cliente principal encargado de ejecutar el flujo multiagente.
"""
client = Swarm()


# ============================================================================
# Función principal de interacción
# ============================================================================

def responder(mensaje, historial, agente_actual):
    """
    Procesa la interacción del usuario dentro de la interfaz conversacional.

    Esta función administra el flujo principal de conversación entre el
    usuario y los agentes especializados. Su responsabilidad incluye:

    - Registrar mensajes en el historial conversacional.
    - Ejecutar el agente actualmente activo.
    - Gestionar posibles transferencias entre agentes.
    - Actualizar la conversación con la respuesta generada.
    - Finalizar la sesión cuando el usuario lo solicite.

    Parameters
    ----------
    mensaje : str
        Mensaje ingresado por el usuario.

    historial : list
        Historial completo de la conversación en formato:
        [{"role": "user|assistant", "content": "..."}]

    agente_actual : Agent
        Agente actualmente encargado de procesar la solicitud.

    Returns
    -------
    tuple
        Retorna:
        - Historial actualizado para el chatbot.
        - Estado actualizado de la conversación.
        - Agente activo actualizado.
    """

    # ------------------------------------------------------------------------
    # Validación de cierre de sesión
    # ------------------------------------------------------------------------

    if mensaje.strip().lower() in ["exit", "terminar"]:
        historial.append({
            "role": "assistant",
            "content": "Sesión finalizada. ¡Hasta pronto!"
        })

        # Cierre de la interfaz gráfica
        demo.close()

        # Reinicio del agente principal para futuras ejecuciones
        return historial, historial, triage_agent

    # ------------------------------------------------------------------------
    # Registro del mensaje del usuario
    # ------------------------------------------------------------------------

    historial.append({
        "role": "user",
        "content": mensaje
    })

    # ------------------------------------------------------------------------
    # Ejecución del agente activo
    # ------------------------------------------------------------------------

    respuesta = client.run(
        agent=agente_actual,
        messages=historial
    )

    # ------------------------------------------------------------------------
    # Actualización dinámica del agente
    # ------------------------------------------------------------------------

    agente_actual = respuesta.agent

    # ------------------------------------------------------------------------
    # Obtención de la respuesta generada
    # ------------------------------------------------------------------------

    contenido = respuesta.messages[-1]["content"]

    historial.append({
        "role": "assistant",
        "content": contenido
    })

    # ------------------------------------------------------------------------
    # Retorno de estados actualizados
    # ------------------------------------------------------------------------

    return historial, historial, agente_actual


# ============================================================================
# Construcción de la interfaz gráfica
# ============================================================================

with gr.Blocks() as demo:
    """
    Interfaz principal de usuario construida con Gradio.

    Componentes:
    - Chatbot para visualización conversacional.
    - Campo de entrada de texto.
    - Botón de envío.
    - Estados persistentes de historial y agente activo.
    """

    gr.Markdown("## Chat con historial")

    # ------------------------------------------------------------------------
    # Componentes visuales
    # ------------------------------------------------------------------------

    chatbot = gr.Chatbot()

    entrada = gr.Textbox(
        label="Escribe tu mensaje"
    )

    enviar = gr.Button("Enviar")

    # ------------------------------------------------------------------------
    # Estados persistentes de sesión
    # ------------------------------------------------------------------------

    """
    Estado del historial conversacional.
    """
    estado = gr.State([])

    """
    Estado del agente actualmente activo.
    """
    agente = gr.State(triage_agent)

    # ------------------------------------------------------------------------
    # Asociación de eventos
    # ------------------------------------------------------------------------

    enviar.click(
        responder,
        inputs=[entrada, estado, agente],
        outputs=[chatbot, estado, agente]
    )


# ============================================================================
# Ejecución de la aplicación
# ============================================================================

"""
Inicialización de la interfaz gráfica en entorno interactivo.
"""
demo.launch(inline=True)
