import os
import json
import requests
from collections import Counter

# 1. Configuración
TOKEN = os.environ.get("KOBO_TOKEN")
ASSET_UID = "apohavweLAvySyRaVnviaN"
URL = f"https://eu.kobotoolbox.org/api/v2/assets/{ASSET_UID}/data.json"

headers = {"Authorization": f"Token {TOKEN}"}

# 2. Consultar la API
response = requests.get(URL, headers=headers)
response.raise_for_status()
datos_crudos = response.json().get("results", [])

# 3. Procesar y agregar datos (Ejemplo: contar encuestas por comunidad)
# Asegúrate de usar el nombre de la variable (name) tal como está en Kobo
conteo_comunidades = Counter(encuesta.get("nombre_comunidad") for encuesta in datos_crudos if encuesta.get("nombre_comunidad"))

datos_agregados = {
    "total_encuestas": len(datos_crudos),
    "por_comunidad": dict(conteo_comunidades)
}

# 4. Guardar el archivo agregado (sobreescribe el anterior)
os.makedirs("datos", exist_ok=True)
with open("datos/datos.json", "w", encoding="utf-8") as f:
    json.dump(datos_agregados, f, ensure_ascii=False, indent=2)
