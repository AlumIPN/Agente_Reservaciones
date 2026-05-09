"""
Módulo de consulta meteorológica.

Este archivo proporciona funcionalidades para consultar pronósticos
climáticos utilizando la API externa de WeatherAPI.

Responsabilidades principales:
- Consultar información meteorológica por ciudad.
- Calcular temperaturas promedio.
- Identificar condiciones climáticas predominantes.
- Estructurar respuestas para consumo por agentes.

La información obtenida es utilizada por los agentes del sistema para:
- Proporcionar contexto climático al usuario.

API utilizada:
- WeatherAPI

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

import os
from collections import Counter

import requests
from dotenv import load_dotenv


# ============================================================================
# Carga de variables de entorno
# ============================================================================

"""
Carga las variables de configuración definidas en el archivo `.env`.
"""
load_dotenv()


# ============================================================================
# Credenciales externas
# ============================================================================

"""
Clave de acceso para WeatherAPI.
"""
API_KEY_W = os.getenv("WHTER_API_KEY")


# ============================================================================
# Consulta de pronóstico climático
# ============================================================================

def obtener_pronostico(ciudad, dias):
    """
    Consulta el pronóstico climático de una ciudad utilizando WeatherAPI.

    La función obtiene información meteorológica para una cantidad
    determinada de días y genera un resumen estructurado que incluye:

    - Temperatura promedio.
    - Condición climática predominante.
    - Estado general de la consulta.

    Parameters
    ----------
    ciudad : str
        Nombre de la ciudad a consultar.

    dias : int
        Número de días de pronóstico requeridos.

    Returns
    -------
    dict
        Diccionario estructurado con el resultado de la consulta.

        Estructura:
        {
            "success": bool,
            "data": {
                "ciudad": str,
                "temperatura_promedio_c": float,
                "condicion_principal": str
            },
            "error": str | None
        }
    """

    try:

        # --------------------------------------------------------------------
        # Construcción de la URL de consulta
        # --------------------------------------------------------------------

        url = (
            f"http://api.weatherapi.com/v1/forecast.json"
            f"?key={API_KEY_W}"
            f"&q={ciudad}"
            f"&days={dias}"
            f"&aqi=no"
            f"&alerts=no"
        )

        # --------------------------------------------------------------------
        # Solicitud HTTP a la API
        # --------------------------------------------------------------------

        response = requests.get(url)

        # --------------------------------------------------------------------
        # Validación de respuesta HTTP
        # --------------------------------------------------------------------

        if response.status_code != 200:

            return {
                "success": False,
                "error": f"Error en la API: {response.status_code}",
                "data": None
            }

        # --------------------------------------------------------------------
        # Conversión de respuesta JSON
        # --------------------------------------------------------------------

        data = response.json()

        # --------------------------------------------------------------------
        # Validación de estructura esperada
        # --------------------------------------------------------------------

        if (
            "forecast" not in data or
            "forecastday" not in data["forecast"]
        ):

            return {
                "success": False,
                "error": "Respuesta inválida de WeatherAPI",
                "data": None
            }

        # --------------------------------------------------------------------
        # Obtención de días de pronóstico
        # --------------------------------------------------------------------

        forecast_days = data["forecast"]["forecastday"]

        # --------------------------------------------------------------------
        # Cálculo de temperatura promedio
        # --------------------------------------------------------------------

        temps = [
            day["day"]["avgtemp_c"]
            for day in forecast_days
        ]

        avg_total = round(sum(temps) / len(temps), 2)

        # --------------------------------------------------------------------
        # Determinación de condición climática predominante
        # --------------------------------------------------------------------

        conditions = [
            day["day"]["condition"]["text"]
            for day in forecast_days
        ]

        condition_mas_comun = (
            Counter(conditions)
            .most_common(1)[0][0]
        )

        # --------------------------------------------------------------------
        # Respuesta estructurada exitosa
        # --------------------------------------------------------------------

        return {
            "success": True,
            "data": {
                "ciudad": ciudad,
                "temperatura_promedio_c": avg_total,
                "condicion_principal": condition_mas_comun
            }
        }

    # ------------------------------------------------------------------------
    # Manejo general de excepciones
    # ------------------------------------------------------------------------

    except Exception as e:

        return {
            "success": False,
            "error": str(e),
            "data": None
        }



