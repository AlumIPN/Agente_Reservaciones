"""
Módulo de variables de contexto compartidas.

Este archivo define las variables de contexto utilizadas por los agentes
del sistema multiagente durante la ejecución de conversaciones y tareas.

El contexto compartido permite:
- Mantener información persistente del usuario.
- Compartir datos entre agentes especializados.
- Incorporar información temporal del sistema.
- Facilitar la personalización de respuestas.

Estructura del contexto:
- customer_context:
    Información relacionada con el usuario.
- general_context:
    Información general de ejecución y sistema.

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

import datetime


# ============================================================================
# Variables de contexto global
# ============================================================================

"""
Diccionario principal de contexto compartido entre agentes.

Contiene información relevante del usuario y datos generales
utilizados durante el flujo conversacional.
"""

context_variables = {

    # ------------------------------------------------------------------------
    # Contexto del cliente
    # ------------------------------------------------------------------------

    "customer_context": {

        """
        Identificador único del cliente.
        """
        "CUSTOMER_ID": "",

        """
        Nombre completo del cliente.
        """
        "NAME": "",

        """
        Edad del cliente.
        """
        "AGE": "",

        """
        Correo electrónico del cliente.
        """
        "EMAIL": "",

        """
        Número telefónico del cliente.
        """
        "PHONE": ""
    },

    # ------------------------------------------------------------------------
    # Contexto general del sistema
    # ------------------------------------------------------------------------

    "general_context": {

        """
        Fecha y hora actual del sistema utilizada como referencia
        temporal durante la conversación.
        """
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}
