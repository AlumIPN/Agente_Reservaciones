"""
Módulo de configuración de variables de entorno.

Este archivo se encarga de cargar y centralizar las credenciales y
variables sensibles utilizadas por la aplicación, utilizando un archivo
`.env` como fuente principal de configuración.

Variables cargadas:
- GOOGLE_MAPS_API_KEY
- OPENAI_API_KEY

El objetivo de este módulo es:
- Separar credenciales del código fuente.
- Facilitar la configuración entre entornos.
- Mejorar la seguridad y mantenibilidad del proyecto.

Autor: Brandon Giron
Proyecto: Sistema Multiagente para Gestión de Reservaciones
"""

import os
# from configs.Agents.Data import BD1

from dotenv import load_dotenv


# ============================================================================
# Carga de variables de entorno
# ============================================================================

"""
Carga las variables definidas en el archivo `.env`
al entorno de ejecución actual.
"""
load_dotenv()


# ============================================================================
# Variables de configuración externas
# ============================================================================

"""
Clave de acceso para servicios de Google Maps API.
"""
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

"""
Clave de acceso para servicios de OpenAI API.
"""
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
