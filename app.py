import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Un solo clic, texto limpio)
# ==========================================
st.markdown("### 1. Edad")

if "edad_elegida" not in st.session_state:
    st.session_state.edad_elegida = "de 20 a 40 años"

# Opción 1: 20-40
f1_col1, f1_col2 = st.columns([1, 5])
with f1_col1:
    st.image("edad_20.png", width=65)
with f1_col2:
    st.write("")
    # El checkbox se marca automáticamente si es la opción activa
    if st.checkbox("de 20 a 40 años", value=(st.session_state.edad_elegida == "de 20 a 40 años"), key="chk_edad1"):
        st.session_state.edad_elegida = "de 20 a 40 años"

# Opción 2: 41-60
f2_col1, f2_col2 = st.columns([1, 5])
with f2_col1:
    st.image("edad_21.png", width=65)
with f2_col2:
    st.write("")
    if st.checkbox("de 41 a 60 años", value=(st.session_state.edad_elegida == "de 41 a 60 años"), key="chk_edad2"):
        st.session_state.edad_elegida = "de 41 a 60 años"

# Opción 3: >60
f3_col1, f3_col2 = st.columns([1, 5])
with f3_col1:
    st.image("edad_60.png", width=65)
with f3_col2:
    st.write("")
    if st.checkbox("más de 60 años", value=(st.session_state.edad_elegida == "más de 60 años"), key="chk_edad3"):
        st.session_state.edad_elegida = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Un solo clic, texto limpio)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_elegido" not in st.session_state:
    st.session_state.civil_elegido = "Casado"

# Opción 1: Casado
f4_col1, f4_col2 = st.columns([1, 5])
with f4_col1:
    st.image("estado_casado.png", width=65)
with f4_col2:
    st.write("")
    if st.checkbox("Casado", value=(st.session_state.civil_elegido == "Casado"), key="chk_civil1"):
        st.session_state.civil_elegido = "Casado"

# Opción 2: Soltero
f5_col1, f5_col2 = st.columns([1, 5])
with f5_col1:
    st.image("estado_soltero.png", width=65)
with f5_col2:
    st.write("")
    if st.checkbox("Soltero", value=(st.session_state.civil_elegido == "Soltero"), key="chk_civil2"):
        st.session_state.civil_elegido = "Soltero"

# Opción 3: Viudo / Divorciado
f6_col1, f6_col2 = st.columns([1, 5])
with f6_col1:
    st.image("estado_divorciado.png", width=65)
with f6_col2:
    st.write("")
    if st.checkbox("Viudo / Divorciado", value=(st.session_state.civil_elegido == "Viudo / Divorciado"), key="chk_civil3"):
        st.session_state.civil_elegido = "Viudo / Divorciado"


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
