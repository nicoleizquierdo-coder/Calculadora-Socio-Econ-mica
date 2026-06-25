import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones haciendo clic en el botón correspondiente:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Opciones fijas hacia abajo, imágenes más pequeñas)
# ==========================================
st.markdown("### 1. Edad")

if "edad_elegida" not in st.session_state:
    st.session_state.edad_elegida = "de 20 a 40 años"

# Opción 1: 20-40
f1_col1, f1_col2 = st.columns([1, 5])
with f1_col1:
    # IMAGEN MÁS PEQUEÑA (width reducido a 65)
    st.image("edad_20.png", width=65)
with f1_col2:
    st.write("") # Espacio para centrar verticalmente
    if st.button("Seleccionar: de 20 a 40 años", key="btn_edad1", use_container_width=True):
        st.session_state.edad_elegida = "de 20 a 40 años"

# Opción 2: 41-60
f2_col1, f2_col2 = st.columns([1, 5])
with f2_col1:
    # IMAGEN MÁS PEQUEÑA
    st.image("edad_21.png", width=65)
with f2_col2:
    st.write("")
    if st.button("Seleccionar: de 41 a 60 años", key="btn_edad2", use_container_width=True):
        st.session_state.edad_elegida = "de 41 a 60 años"

# Opción 3: >60
f3_col1, f3_col2 = st.columns([1, 5])
with f3_col1:
    # IMAGEN MÁS PEQUEÑA
    st.image("edad_60.png", width=65)
with f3_col2:
    st.write("")
    if st.button("Seleccionar: más de 60 años", key="btn_edad3", use_container_width=True):
        st.session_state.edad_elegida = "más de 60 años"

st.info(f"Selección actual de Edad: **{st.session_state.edad_elegida}**")


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Opciones fijas hacia abajo, imágenes más pequeñas)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_elegido" not in st.session_state:
    st.session_state.civil_elegido = "Casado"

# Opción 1: Casado
f4_col1, f4_col2 = st.columns([1, 5])
with f4_col1:
    # IMAGEN MÁS PEQUEÑA
    st.image("estado_casado.png", width=65)
with f4_col2:
    st.write("")
    if st.button("Seleccionar: Casado", key="btn_civil1", use_container_width=True):
        st.session_state.civil_elegido = "Casado"

# Opción 2: Soltero
f5_col1, f5_col2 = st.columns([1, 5])
with f5_col1:
    # IMAGEN MÁS PEQUEÑA
    st.image("estado_soltero.png", width=65)
with f5_col2:
    st.write("")
    if st.button("Seleccionar: Soltero", key="btn_civil2", use_container_width=True):
        st.session_state.civil_elegido = "Soltero"

# Opción 3: Viudo / Divorciado
f6_col1, f6_col2 = st.columns([1, 5])
with f6_col1:
    # IMAGEN MÁS PEQUEÑA
    st.image("estado_divorciado.png", width=65)
with f6_col2:
    st.write("")
    if st.button("Seleccionar: Viudo / Divorciado", key="btn_civil3", use_container_width=True):
        st.session_state.civil_elegido = "Viudo / Divorciado"

st.info(f"Selección actual de Estado Civil: **{st.session_state.civil_elegido}**")


st.write("---")


# ==========================================
# BOTÓN DE DESCARGA
# ==========================================
datos_a_guardar = f"=== RESUMEN DE RESPUESTAS ===\n• Rango de edad: {st.session_state.edad_elegida}\n• Estado civil:  {st.session_state.civil_elegido}\n"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen_calculadora.txt",
    mime="text/plain"
)
