"""
Módulo de definición y configuración de agentes especializados.

Este archivo centraliza la creación de los agentes utilizados dentro
de la arquitectura multiagente del sistema. Cada agente posee un rol
específico, instrucciones particulares y acceso controlado a funciones
especializadas según su responsabilidad operativa.

Agentes implementados:
- Principal Agent
- Change Agent
- Cancel Agent
- Triage Agent

Responsabilidades generales:
- Gestión de reservaciones.
- Cambios de itinerario.
- Cancelaciones.
- Clasificación y transferencia de solicitudes.

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

from swarm import Agent

from configs.Agents.prompts import *

from configs.Agents.Data.context_variables import *

from configs.Agents.Data.BDAg import *

from configs.Tools.Places import *

from configs.Tools.Clima import *

from configs.Tools.switch import *


# ============================================================================
# Agente principal
# ============================================================================

"""
Agente especializado en la atención principal de solicitudes relacionadas
con viajes, reservaciones, transporte e itinerarios.

Responsabilidades:
- Consultar información de reservaciones.
- Buscar opciones de vuelos y transporte.
- Gestionar reservaciones.
- Generar itinerarios.
- Consultar información climática.
- Transferir solicitudes a agentes especializados cuando sea necesario.
"""

main_Agent = Agent(
    name="Principal Agent",

    model="gpt-4o",

    instructions=principal_inst(context_variables),

    functions=[
        consultar,
        buscar_vuelo,
        reservar,
        itinerario,
        obtener_pronostico,
        switch_change_ag,
        switch_cancel_ag,
        consultar_bus,
        buscar_vuelo
    ]
)


# ============================================================================
# Agente de cambios
# ============================================================================

"""
Agente especializado en modificaciones de reservaciones e itinerarios.

Responsabilidades:
- Actualizar información de reservaciones.
- Consultar reservaciones mediante folio.
- Gestionar cambios relacionados con vuelos y transporte.
- Transferir solicitudes a otros agentes cuando corresponda.
"""

change_Agent = Agent(
    name="Change Agent",

    model="gpt-4o",

    instructions=change_inst(context_variables),

    functions=[
        switch_main_ag,
        switch_cancel_ag,
        actualizar,
        consultar_folio,
        consultar_bus,
        buscar_vuelo
    ]
)


# ============================================================================
# Agente de cancelaciones
# ============================================================================

"""
Agente especializado en la gestión de cancelaciones de reservaciones.

Responsabilidades:
- Procesar cancelaciones de reservaciones.
- Transferir solicitudes hacia otros agentes especializados.
"""

cancel_Agent = Agent(
    name="Cancel Agent",

    model="gpt-4o",

    instructions=Cancel_inst(context_variables),

    functions=[
        switch_main_ag,
        switch_change_ag,
        cancelar_reserva
    ]
)


# ============================================================================
# Agente de clasificación (Triage)
# ============================================================================

"""
Agente inicial encargado de clasificar las solicitudes del usuario y
redirigirlas al agente especializado correspondiente.

Responsabilidades:
- Identificar la intención principal del usuario.
- Realizar consultas básicas.
- Transferir solicitudes al agente adecuado.
- Actuar como punto de entrada principal del sistema.
"""

triage_agent = Agent(
    name="Triage Agent",

    model="gpt-4o-mini",

    instructions=triage_inst(context_variables),

    functions=[
        consultar,
        switch_main_ag,
        switch_change_ag,
        switch_cancel_ag
    ]
)
