import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 PERSONALIZACIÓN CSS (Color Verde y Alineación)
# ==========================================
st.markdown("""
    <style>
        /* 1. Forzar color verde a las casillas seleccionadas */
        div[data-testid="stCheckbox"] input[type="checkbox"]:checked + div {
            background-color: #28a745 !important;
            border-color: #28a745 !important;
        }
        
        /* 2. Mantener el texto de las opciones siempre negro */
        div[data-testid="stCheckbox"] label p {
            color: #31333F !important;
            font-weight: 500;
            font-size: 1.1rem !important;
        }

        /* 3. Centrar verticalmente la imagen con la casilla de texto */
        div[data-testid="stHorizontalBlock"] {
            align-items: center !important;
            margin-bottom: -10px !important;
        }
        
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones (Un solo clic - Selección única):")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Imagen y Letra amarradas por fila)
# ==========================================
st.markdown("### 1. Edad")

if "edad_final" not in st.session_state:
    st.session_state.edad_final = "de 20 a 40 años"

# Fila 1: Opción 1
f1_c1, f1_c2 = st.columns([1, 10])
with f1_c1:
    st.image("edad_20.png", width=50)
with f1_c2:
    # Se marca sola si está activa en la memoria
    if st.checkbox("de 20 a 40 años", value=(st.session_state.edad_final == "de 20 a 40 años"), key="chk_e1"):
        st.session_state.edad_final = "de 20 a 40 años"

# Fila 2: Opción 2
f2_c1, f2_c2 = st.columns([1, 10])
with f2_c1:
    st.image("edad_21.png", width=50)
with f2_c2:
    if st.checkbox("de 41 a 60 años", value=(st.session_state.edad_final == "de 41 a 60 años"), key="chk_e2"):
        st.session_state.edad_final = "de 41 a 60 años"

# Fila 3: Opción 3
f3_c1, f3_c2 = st.columns([1, 10])
with f3_c1:
    st.image("edad_60.png", width=50)
with f3_c2:
    if st.checkbox("más de 60 años", value=(st.session_state.edad_final == "más de 60 años"), key="chk_e3"):
        st.session_state.edad_final = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Imagen y Letra amarradas por fila)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_final" not in st.session_state:
    st.session_state.civil_final = "Casado"

# Fila 1: Opción 1
f4_c1, f4_c2 = st.columns([1, 10])
with f4_c1:
    st.image("estado_casado.png", width=50)
with f4_c2:
    if st.checkbox("Casado", value=(st.session_state.civil_final == "Casado"), key="chk_c1"):
        st.session_state.civil_final = "Casado"

# Fila 2: Opción 2
f5_c1, f5_c2 = st.columns([1, 10])
with f5_c1:
    st.image("estado_soltero.png", width=50)
with f5_c2:
    if st.checkbox("Soltero", value=(st.session_state.civil_final == "Soltero"), key="chk_c2"):
        st.session_state.civil_final = "Soltero"

# Fila 3: Opción 3
f6_c1, f6_c2 = st.columns([1, 10])
with f6_c1:
    st.image("estado_divorciado.png", width=50)
with f6_c2:
    if st.checkbox("Viudo / Divorciado", value=(st.session_state.civil_final == "Viudo / Divorciado"), key="chk_c3"):
        st.session_state.civil_final = "Viudo / Divorciado"


st.write("---")


# ==========================================
# BOTÓN DE DESCARGA
# ==========================================
datos_a_guardar = f"=== RESUMEN ===\nEdad: {st.session_state.edad_final}\nEstado Civil: {st.session_state.civil_final}"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen.txt",
    mime="text/plain"
)
