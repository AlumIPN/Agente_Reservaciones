"""
Módulo de transferencia entre agentes.

Este archivo contiene las funciones responsables de realizar
la transferencia dinámica entre agentes especializados dentro
de la arquitectura multiagente.

Responsabilidades principales:
- Redirigir solicitudes al agente adecuado.
- Facilitar la coordinación entre agentes.
- Mantener desacoplamiento entre módulos.
- Controlar el flujo conversacional.

Las funciones de este módulo son utilizadas principalmente por:
- Agente de clasificación (Triage Agent).
- Agentes especializados durante transferencias internas.

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""


# ============================================================================
# Transferencia al agente principal
# ============================================================================

def switch_main_ag():
    """
    Transfiere la conversación al agente principal.

    El agente principal es responsable de:
    - Reservaciones.
    - Consultas generales de viaje.
    - Transporte.
    - Generación de itinerarios.
    - Información turística.

    Returns
    -------
    Agent
        Instancia del agente principal.
    """

    from configs.Agents.TypesAg import main_Agent

    return main_Agent


# ============================================================================
# Transferencia al agente de cambios
# ============================================================================

def switch_change_ag():
    """
    Transfiere la conversación al agente especializado en cambios.

    El agente de cambios es responsable de:
    - Modificaciones de reservaciones.
    - Actualización de itinerarios.
    - Ajustes de fechas.
    - Cambios relacionados con transporte y actividades.

    Returns
    -------
    Agent
        Instancia del agente de cambios.
    """

    from configs.Agents.TypesAg import change_Agent

    return change_Agent


# ============================================================================
# Transferencia al agente de cancelaciones
# ============================================================================

def switch_cancel_ag():
    """
    Transfiere la conversación al agente especializado en cancelaciones.

    El agente de cancelaciones es responsable de:
    - Cancelar reservaciones.
    - Eliminar actividades del itinerario.
    - Gestionar solicitudes relacionadas con cancelaciones parciales
      o completas.

    Returns
    -------
    Agent
        Instancia del agente de cancelaciones.
    """

    from configs.Agents.TypesAg import cancel_Agent

    return cancel_Agent
