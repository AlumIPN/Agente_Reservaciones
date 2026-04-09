#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Cargar variables desde .env
load_dotenv()

# Obtener la API Key
API_KEY_G = os.getenv("GOOGLE_MAPS_API_KEY")
API_KEY_A = os.getenv("AVSTACK_API_KEY")


# In[20]:


def consultar(place: str, query: str):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    busqueda = query + " " + place
    params = {
        "query": busqueda,
        "key": API_KEY_G
    }

    response = requests.get(url, params=params)
    data = response.json()

    resultados = []
    for p in data.get("results", []):
        resultados.append({
            "nombre": p.get("name"),
            "direccion": p.get("formatted_address"),
            "rating": p.get("rating")
        })
    return resultados


# In[5]:


def buscar_vuelos(dep_iata, arr_iata=None, limite=10):
    """
    Busca vuelos usando la API de aviationstack y devuelve resultados formateados.
    """
    endpoint = "https://api.aviationstack.com/v1/flights"
    params = {
        "access_key": API_KEY_A,
        "dep_iata": dep_iata,
        "limit": limite
    }
    if arr_iata:
        params["arr_iata"] = arr_iata

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()

        if "data" in data and len(data["data"]) > 0:
            df = pd.json_normalize(data["data"])
            columnas = [col for col in [
                "airline.name", "flight.iata", "departure.airport", "departure.scheduled",
                "arrival.airport", "arrival.scheduled", "flight_status"
            ] if col in df.columns]

            # Formatear resultados directamente
            resultados = []
            for _, fila in df[columnas].head(limite).iterrows():
                vuelo = (
                    f"Vuelo {fila.get('flight.iata','N/A')} de {fila.get('airline.name','N/A')}, "
                    f"sale de {fila.get('departure.airport','N/A')} a las {fila.get('departure.scheduled','N/A')}, "
                    f"llega a {fila.get('arrival.airport','N/A')} a las {fila.get('arrival.scheduled','N/A')}, "
                    f"estado: {fila.get('flight_status','N/A')}."
                )
                resultados.append(vuelo)
            return resultados
        else:
            return ["No se encontraron vuelos disponibles."]
    except requests.exceptions.RequestException as e:
        return [f"Error en la solicitud: {e}"]
    except Exception as e:
        return [f"Error procesando datos: {e}"]


# In[ ]:




