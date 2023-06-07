import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#from fpdf import FPDF

archivo_pdf = "consolidado.pdf"

def enviar_correo(destinatario, archivo_adjunto):
    # Configura los detalles del servidor SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "Reto2Python@gmail.com"
    smtp_password = "wghfdcqcwymepmhr"
    
    # Crea el objeto MIMEMultipart
    mensaje = MIMEMultipart()
    mensaje["From"] = smtp_username
    mensaje["To"] = destinatario
    mensaje["Subject"] = "Consolidado de boletas de pago"
  
    with open(archivo_adjunto, "rb") as f:
        adjunto = MIMEBase("application", "octet-stream")
        adjunto.set_payload(f.read())
        encoders.encode_base64(adjunto)
        adjunto.add_header("Content-Disposition", f"attachment; filename={archivo_pdf}")
        mensaje.attach(adjunto)
  
  # Enviar el correo electrónico
    with smtplib.SMTP(smtp_server, smtp_port) as servidor_smtp:
          servidor_smtp.starttls()
          servidor_smtp.login(smtp_username, smtp_password)
          servidor_smtp.send_message(mensaje)
  
    print("Correo electrónico enviado con éxito.")
    return 'true'