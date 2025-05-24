import streamlit as st

# Título de la app
st.title("Descarga tu PDF")

# Ruta o archivo PDF (puedes cambiar el nombre si es otro)
pdf_file = "documento.pdf"

# Abrir el PDF en modo binario
with open(pdf_file, "rb") as file:
    pdf_bytes = file.read()

# Botón para descargar el PDF
st.download_button(
    label="Descargar PDF",
    data=pdf_bytes,
    file_name="documento_descargado.pdf",
    mime="application/pdf"
)

st.write("Haz clic en el botón para descargar el PDF.")
