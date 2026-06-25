import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Opciones con imágenes al lado)
# ==========================================
st.markdown("### 1. Edad")

# Usamos columnas pequeñas para alinear la imagen al lado de la selección
col_img1, col_opt1 = st.columns([1, 3])

with col_opt1:
    edad = st.radio(
        "Selecciona tu rango de edad:",
        ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"],
        key="edad_radio"
    )

# Asignamos la imagen correspondiente según la selección para mostrarla al lado
if edad == "de 20 a 40 años":
    imagen_edad = "edad_20.png"
elif edad == "de 41 a 60 años":
    imagen_edad = "edad_21.png"
else:
    imagen_edad = "edad_60.png"

with col_img1:
    # Mostramos la imagen pequeña alineada a la izquierda
    st.image(imagen_edad, width=100)


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Opciones con imágenes al lado)
# ==========================================
st.markdown("### 2. Estado Civil")

col_img2, col_opt2 = st.columns([1, 3])

with col_opt2:
    estado_civil = st.radio(
        "Selecciona tu Estado Civil:",
        ["Casado", "Soltero", "Viudo / Divorciado"],
        key="civil_radio"
    )

if estado_civil == "Casado":
    imagen_civil = "estado_casado.png"
elif estado_civil == "Soltero":
    imagen_civil = "estado_soltero.png"
else:
    imagen_civil = "estado_divorciado.png"

with col_img2:
    # Mostramos la imagen pequeña alineada a la izquierda
    st.image(imagen_civil, width=100)


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
