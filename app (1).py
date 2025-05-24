
import streamlit as st
from fpdf import FPDF

# Ruta relativa para la fuente
FUENTE = "DejaVuSans.ttf"

def crear_reporte_pdf(costo_fijo, costo_variable, precio_venta, punto_eq, max_cantidad):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', FUENTE, uni=True)
    pdf.set_font('DejaVu', '', 14)
    
    pdf.cell(0, 10, 'Reporte de Punto de Equilibrio', 0, 1, 'C')
    pdf.ln(10)
    pdf.cell(0, 10, f"Costo Fijo: ${costo_fijo}", 0, 1)
    pdf.cell(0, 10, f"Costo Variable: ${costo_variable}", 0, 1)
    pdf.cell(0, 10, f"Precio de Venta: ${precio_venta}", 0, 1)
    pdf.cell(0, 10, f"Punto de Equilibrio: {punto_eq} unidades", 0, 1)
    pdf.cell(0, 10, f"Cantidad Máxima: {max_cantidad} unidades", 0, 1)

    pdf_output = "reporte_panaderia.pdf"
    pdf.output(pdf_output)
    return pdf_output

def main():
    st.title("Calculadora Punto de Equilibrio - Panadería")
    costo_fijo = st.number_input("Costo Fijo Mensual", min_value=0)
    costo_variable = st.number_input("Costo Variable por unidad", min_value=0)
    precio_venta = st.number_input("Precio de Venta por unidad", min_value=0)

    if st.button("Calcular y generar PDF"):
        if precio_venta > costo_variable:
            punto_eq = costo_fijo / (precio_venta - costo_variable)
            max_cantidad = punto_eq * 2
            pdf_file = crear_reporte_pdf(costo_fijo, costo_variable, precio_venta, punto_eq, max_cantidad)
            with open(pdf_file, "rb") as f:
                st.download_button("Descargar reporte PDF", f, file_name=pdf_file)
        else:
            st.error("El precio de venta debe ser mayor que el costo variable.")

if __name__ == "__main__":
    main()
