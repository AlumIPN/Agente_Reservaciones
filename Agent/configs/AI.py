import os
#from configs.Agents.Data import BD1

from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Obtener la API Key
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
