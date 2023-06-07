from fpdf import FPDF

def generar_pdf_consolidado(dataframes):
    pdf = FPDF()
    
    campos_ordenados = ['Nombres y Apellidos', 'Cargo', 'Sueldo', 'Mes', 'Días Trabajados']

    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Genera el contenido del PDF
    for empleado in dataframes:
        for campo in campos_ordenados:
           
            pdf.cell(0, 10, f"{campo}: {empleado[campo]}", ln=True)

        pdf.ln()
    
    # Guarda el archivo PDF
    pdf.output("consolidado.pdf")
    return 'true'
    