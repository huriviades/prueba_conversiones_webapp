import requests

API_URL = "http://172.40.0.20:80/api/conversiones/temperatura"

def obtener_conversiones():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener conversiones: {e}")
        return []

def crear_conversion(resultado, tipo):
    nueva_conversion = {
        "resultado": resultado,
        "tipo": tipo
    }
    try:
        response = requests.post(API_URL, json=nueva_conversion)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error al crear la conversión: {e}")
        return False
