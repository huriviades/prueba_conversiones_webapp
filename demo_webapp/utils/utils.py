import requests
from .formulas import celsius_a_fahrenheit, fahrenheit_a_celsius

API_URL = "http://172.40.0.20:80/api/conversiones/temperatura"

def obtener_conversiones():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener conversiones: {e}")
        return []

def crear_conversion(temperatura, tipo):
    temperatura = float(temperatura)
    if tipo == "F":
        resultado = celsius_a_fahrenheit(temperatura)
        tipo_completo = "Celsius a Fahrenheit"
    elif tipo == "C":
        resultado = fahrenheit_a_celsius(temperatura)
        tipo_completo = "Fahrenheit a Celsius"
    else:
        print("Tipo de conversión no válido")
        return False

    nueva_conversion = {
        "resultado": resultado,
        "tipo": tipo_completo
    }

    try:
        response = requests.post(API_URL, json=nueva_conversion)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error al crear la conversión: {e}")
        return False