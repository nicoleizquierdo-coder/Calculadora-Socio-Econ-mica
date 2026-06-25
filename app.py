import streamlit as st

# Configuración del título de la página web
st.title("Formulario de Datos Personales")
st.write("Por favor, responde a las siguientes preguntas:")

# 1. Pregunta de Edad
edad = st.selectbox(
    "1. Selecciona tu rango de edad:",
    ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"]
)

# 2. Pregunta de Estado Civil
estado_civil = st.selectbox(
    "2. Selecciona tu Estado Civil:",
    ["Casado", "Soltero", "Viudo / Divorciado"]
)

st.write("---")

# Botón para descargar las respuestas
datos_a_guardar = f"=== INFORMACIÓN ===\nEdad: {edad}\nEstado Civil: {estado_civil}\n"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="mis_respuestas.txt",
    mime="text/plain"
)
