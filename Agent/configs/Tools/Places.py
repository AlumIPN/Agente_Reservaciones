"""
Módulo de consulta de lugares y servicios turísticos.

Este archivo proporciona funcionalidades para realizar búsquedas
de lugares utilizando la API de Google Places.

Responsabilidades principales:
- Consultar lugares turísticos y establecimientos.
- Obtener información básica de ubicaciones.
- Proporcionar resultados estructurados para los agentes.
- Facilitar recomendaciones de viaje e itinerarios.

La información obtenida puede incluir:
- Nombre del lugar.
- Dirección.
- Calificación promedio.

API utilizada:
- Google Places API

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

import os

import pandas as pd
import requests
from dotenv import load_dotenv


# ============================================================================
# Carga de variables de entorno
# ============================================================================

"""
Carga las variables definidas en el archivo `.env`.
"""
load_dotenv()


# ============================================================================
# Credenciales externas
# ============================================================================

"""
Clave de acceso para Google Places API.
"""
API_KEY_G = os.getenv("GOOGLE_MAPS_API_KEY")


# ============================================================================
# Consulta de lugares
# ============================================================================

def consultar(place: str, query: str):
    """
    Realiza una búsqueda de lugares utilizando Google Places API.

    La función combina un término de búsqueda con una ubicación
    específica para obtener resultados relacionados con:
    - Restaurantes
    - Hoteles
    - Atracciones
    - Servicios turísticos
    - Otros establecimientos

    Parameters
    ----------
    place : str
        Ciudad, ubicación o destino de búsqueda.

    query : str
        Tipo de lugar o término de búsqueda.

    Returns
    -------
    list
        Lista de resultados estructurados.

        Cada elemento contiene:
        {
            "nombre": str,
            "direccion": str,
            "rating": float
        }
    """

    # ------------------------------------------------------------------------
    # Endpoint de Google Places API
    # ------------------------------------------------------------------------

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

    # ------------------------------------------------------------------------
    # Construcción de la consulta
    # ------------------------------------------------------------------------

    busqueda = query + " " + place

    params = {
        "query": busqueda,
        "key": API_KEY_G
    }

    # ------------------------------------------------------------------------
    # Solicitud HTTP
    # ------------------------------------------------------------------------

    response = requests.get(url, params=params)

    # ------------------------------------------------------------------------
    # Conversión de respuesta JSON
    # ------------------------------------------------------------------------

    data = response.json()

    # ------------------------------------------------------------------------
    # Procesamiento de resultados
    # ------------------------------------------------------------------------

    resultados = []

    for p in data.get("results", []):

        resultados.append({
            "nombre": p.get("name"),
            "direccion": p.get("formatted_address"),
            "rating": p.get("rating")
        })

    # ------------------------------------------------------------------------
    # Retorno de resultados estructurados
    # ------------------------------------------------------------------------

    return resultados

