#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os
from dotenv import load_dotenv
from collections import Counter
import requests


load_dotenv()

API_KEY_W = os.getenv("WHTER_API_KEY")


# In[23]:


def obtener_pronostico(ciudad, dias):
    """
    Consulta el pronóstico de una ciudad para N días usando WeatherAPI.
    Devuelve un objeto estructurado para consumo por agentes.
    """
    
    try:
        url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY_W}&q={ciudad}&days={dias}&aqi=no&alerts=no"
        response = requests.get(url)

        if response.status_code != 200:
            return {
                "success": False,
                "error": f"Error en la API: {response.status_code}",
                "data": None
            }

        data = response.json()

        if "forecast" not in data or "forecastday" not in data["forecast"]:
            return {
                "success": False,
                "error": "Respuesta inválida de WeatherAPI",
                "data": None
            }

        forecast_days = data["forecast"]["forecastday"]

        # Promedio de temperaturas
        temps = [day["day"]["avgtemp_c"] for day in forecast_days]
        avg_total = round(sum(temps) / len(temps), 2)

        # Condición más frecuente
        conditions = [day["day"]["condition"]["text"] for day in forecast_days]
        condition_mas_comun = Counter(conditions).most_common(1)[0][0]

        return {
            "success": True,
            "data": {
                "ciudad": ciudad,
                "temperatura_promedio_c": avg_total,
                "condicion_principal": condition_mas_comun
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "data": None
        }




# In[ ]:




