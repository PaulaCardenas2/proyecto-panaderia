
import streamlit as st
from fpdf import FPDF
import io

def crear_reporte_pdf(costo_fijo, costo_variable, precio_venta, punto_eq, max_cantidad):
    pdf = FPDF()
    pdf.add_page()

    # Agregar fuente con uni=True para evitar error UnicodeEncodeError
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)

    pdf.cell(0, 10, f"Costo fijo: ${costo_fijo}", ln=True)
    pdf.cell(0, 10, f"Costo variable: ${costo_variable}", ln=True)
    pdf.cell(0, 10, f"Precio venta: ${precio_venta}", ln=True)
    pdf.cell(0, 10, f"Punto de equilibrio: {punto_eq}", ln=True)
    pdf.cell(0, 10, f"Cantidad máxima: {max_cantidad}", ln=True)

    # Guardar PDF en memoria, no en disco
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

# Parámetros de ejemplo
costo_fijo = 500000
costo_variable = 1000
precio_venta = 2000
punto_eq = 500
max_cantidad = 1000

pdf_bytes = crear_reporte_pdf(costo_fijo, costo_variable, precio_venta, punto_eq, max_cantidad)

st.title("Proyecto Panadería")
st.write("Aquí puedes descargar el reporte PDF")

st.download_button(
    label="Descargar reporte PDF",
    data=pdf_bytes,
    file_name="reporte_panaderia.pdf",
    mime="application/pdf"
)