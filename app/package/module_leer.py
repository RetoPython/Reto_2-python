import pandas as pd
import os
import glob

carpeta_boletas = os.path.abspath("Boletas")
archivos_boletas = glob.glob(os.path.join(carpeta_boletas, "*.txt"))
dataframes_boletas = []
   
    
def leer_boleta(archivo):
    # Leer el archivo .txt
    with open(archivo, "r") as f:
        lineas = f.readlines()

    # Extraer los datos de las líneas del archivo
    nombres_apellidos = lineas[0].strip().split(": ")[1]
    cargo = lineas[1].strip().split(": ")[1]
    sueldo = float(lineas[2].strip().split(": ")[1].split("S/ ")[1])
    mes = lineas[3].strip().split(": ")[1]
    dias_trabajados = int(lineas[4].strip().split(": ")[1])
 

    # Crear un DataFrame con los datos
    datos = {
        "Nombres y Apellidos": [nombres_apellidos],
        "Cargo": [cargo],
        "Sueldo": [sueldo],
        "Mes": [mes],
        "Días Trabajados": [dias_trabajados]
       
    }
    df = pd.DataFrame(datos)

    return df