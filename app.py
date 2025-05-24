pdf_file = crear_reporte_pdf(costo_fijo, costo_variable, precio_venta, punto_eq, max_cantidad)

with open(pdf_file, "rb") as file:
    st.download_button(
        label="Descargar reporte PDF",
        data=file,
        file_name=pdf_file,
        mime="application/pdf"
    )
