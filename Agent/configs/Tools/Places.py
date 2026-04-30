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





