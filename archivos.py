
import csv
import json
import os
from datetime import datetime

ARCHIVO_HISTORIAL = "historial.csv"
ARCHIVO_RESUMEN = "resumen.json"
PREFIJO_RESULTADO = "resultado_"


def cargar_csv(ruta):
    """Lee un CSV con csv.reader. Retorna (encabezados, filas)."""
    filas = []
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)
        encabezados = next(lector)
        for fila in lector:
            if fila:
                filas.append(fila)
    return encabezados, filas


def guardar_csv(ruta, encabezados, filas):
    """Escribe encabezados y filas en un CSV."""
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezados)
        escritor.writerows(filas)


def guardar_json(ruta, datos):
    """Guarda un diccionario o lista en un archivo JSON."""
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)


def cargar_json(ruta):
    """Lee un archivo JSON y retorna su contenido."""
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


# ---------- Resultados guardados ----------

def nombre_seguro(texto):
    """Deja solo letras, números y guion bajo para usar como nombre de archivo."""
    limpio = ""
    for c in texto.strip().lower():
        if c.isalnum() or c == "_":
            limpio += c
        elif c == " ":
            limpio += "_"
    return limpio


def guardar_resultado(nombre, encabezados, filas):
    """Guarda filas en resultado_<nombre>.csv. Retorna la ruta o None si el nombre es vacío."""
    nombre = nombre_seguro(nombre)
    if nombre == "":
        return None
    ruta = PREFIJO_RESULTADO + nombre + ".csv"
    guardar_csv(ruta, encabezados, filas)
    return ruta



