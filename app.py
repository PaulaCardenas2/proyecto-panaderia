
import streamlit as st

st.title("Análisis de Viabilidad Económica - Panadería Artesanal")

st.header("Introducción")
st.write("""
Este proyecto analiza la viabilidad económica de una panadería artesanal,
calculando el punto de equilibrio y evaluando la producción diaria actual.
Se usan conceptos matemáticos como funciones lineales, proporcionalidad,
regla de tres y porcentajes.
""")

st.header("Datos del problema")

costo_fijo = 500000
costo_variable = 1000
precio_venta = 2000
panadero_a = 20  # panes por hora
panadero_b = panadero_a * 1.5  # 1.5 veces más rápido
horas_jornada = 8

st.write(f"Costo fijo mensual: ${costo_fijo:,}")
st.write(f"Costo variable por pan: ${costo_variable:,}")
st.write(f"Precio de venta por pan: ${precio_venta:,}")
st.write(f"Producción Panadero A: {panadero_a} panes/hora")
st.write(f"Producción Panadero B: {int(panadero_b)} panes/hora")
st.write(f"Jornada laboral diaria: {horas_jornada} horas")

produccion_hora = panadero_a + panadero_b
produccion_dia = produccion_hora * horas_jornada

punto_equilibrio = costo_fijo / (precio_venta - costo_variable)

cumplimiento = (produccion_dia / punto_equilibrio) * 100

horas_necesarias = punto_equilibrio / produccion_hora

st.header("Resultados")

st.write(f"Producción total diaria: {int(produccion_dia)} panes")
st.write(f"Punto de equilibrio (panes a vender): {int(punto_equilibrio)} panes")
st.write(f"Porcentaje de la meta cubierta con jornada actual: {cumplimiento:.2f}%")
st.write(f"Horas necesarias para cubrir el punto de equilibrio: {horas_necesarias:.2f} horas")

st.header("Conclusión")
if cumplimiento >= 100:
    st.write("La producción actual es suficiente para alcanzar el punto de equilibrio.")
else:
    st.write("La producción actual NO es suficiente para alcanzar el punto de equilibrio,")
    st.write(f"se necesitan {horas_necesarias:.2f} horas de trabajo para lograrlo.")
