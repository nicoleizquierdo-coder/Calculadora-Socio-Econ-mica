import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, responde a las siguientes preguntas en orden descendente:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Hacia abajo con su imagen)
# ==========================================
st.markdown("### 1. Edad")

# st.radio muestra las 3 opciones al mismo tiempo en pantalla
edad = st.radio(
    "Selecciona tu rango de edad:",
    ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"],
    key="edad_radio"
)

# Se asigna la imagen correspondiente a la opción seleccionada
if edad == "de 20 a 40 años":
    imagen_edad = "edad_20.png"
elif edad == "de 41 a 60 años":
    imagen_edad = "edad_21.png"
else:
    imagen_edad = "edad_60.png"

# Muestra la imagen de la edad seleccionada justo debajo
st.image(imagen_edad, caption=f"Rango seleccionado: {edad}", width=350)


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Hacia abajo con su imagen)
# ==========================================
st.markdown("### 2. Estado Civil")

# También usamos st.radio para ver las opciones al mismo tiempo
estado_civil = st.radio(
    "Selecciona tu Estado Civil:",
    ["Casado", "Soltero", "Viudo / Divorciado"],
    key="civil_radio"
)

# Se asigna la imagen correspondiente al estado civil
if estado_civil == "Casado":
    imagen_civil = "estado_casado.png"
elif estado_civil == "Soltero":
    imagen_civil = "estado_soltero.png"
else:
    imagen_civil = "estado_divorciado.png"

# Muestra la imagen del estado civil justo debajo
st.image(imagen_civil, caption=f"Estado seleccionado: {estado_civil}", width=350)


st.write("---")


# ==========================================
# BOTÓN DE DESCARGA
# ==========================================
datos_a_guardar = f"=== RESUMEN DE RESPUESTAS ===\n• Rango de edad: {edad}\n• Estado civil:  {estado_civil}\n"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen_calculadora.txt",
    mime="text/plain"
)
