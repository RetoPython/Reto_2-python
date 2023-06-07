import os
import glob
from package.module_leer import leer_boleta
from package.module_pdf import generar_pdf_consolidado
from package.module_correo import enviar_correo

carpeta_boletas = os.path.abspath("Boletas")
archivos_boletas = glob.glob(os.path.join(carpeta_boletas, "*.txt"))
dataframes_boletas = []

print (archivos_boletas)
for archivo in archivos_boletas:
    df_boleta = leer_boleta(archivo)
    dataframes_boletas.append(df_boleta)

generar_pdf_consolidado(dataframes_boletas)
destinatario = "xxxxxxxxx@gmail.com"
archivo_pdf = "consolidado.pdf"
enviar_correo(destinatario, archivo_pdf)
