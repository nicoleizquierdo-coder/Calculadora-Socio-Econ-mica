import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="wide")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones haciendo clic en el botón correspondiente:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Las 3 opciones visibles a la vez con su foto)
# ==========================================
st.markdown("### 1. Edad")

# Inicializamos la variable en el estado de Streamlit si no existe
if "edad_elegida" not in st.session_state:
    st.session_state.edad_elegida = "de 20 a 40 años" # Opción por defecto

# Creamos 3 columnas para mostrar las 3 opciones juntas de izquierda a derecha
col1, col2, col3 = st.columns(3)

with col1:
    st.image("edad_20.png", width=120)
    if st.button("Seleccionar: de 20 a 40 años", key="btn_edad1"):
        st.session_state.edad_elegida = "de 20 a 40 años"

with col2:
    st.image("edad_21.png", width=120)
    if st.button("Seleccionar: de 41 a 60 años", key="btn_edad2"):
        st.session_state.edad_elegida = "de 41 a 60 años"

with col3:
    st.image("edad_60.png", width=120)
    if st.button("Seleccionar: más de 60 años", key="btn_edad3"):
        st.session_state.edad_elegida = "más de 60 años"

# Mostramos cuál está seleccionada actualmente
st.info(f"Selección actual de Edad: **{st.session_state.edad_elegida}**")


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Las 3 opciones visibles a la vez con su foto)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_elegido" not in st.session_state:
    st.session_state.civil_elegido = "Casado" # Opción por defecto

col4, col5, col6 = st.columns(3)

with col4:
    st.image("estado_casado.png", width=120)
    if st.button("Seleccionar: Casado", key="btn_civil1"):
        st.session_state.civil_elegido = "Casado"

with col5:
    st.image("estado_soltero.png", width=120)
    if st.button("Seleccionar: Soltero", key="btn_civil2"):
        st.session_state.civil_elegido = "Soltero"

with col6:
    st.image("estado_divorciado.png", width=120)
    if st.button("Seleccionar: Viudo / Divorciado", key="btn_civil3"):
        st.session_state.civil_elegido = "Viudo / Divorciado"

# Mostramos cuál está seleccionada actualmente
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
