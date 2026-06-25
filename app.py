import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 REGLAS DE COLOR: TEXTO NEGRO Y CASILLA VERDE
# ==========================================
st.markdown("""
    <style>
        /* Desactivar el botón flotante de Deploy */
        .stDeployButton { display:none; }
        
        /* Forzar color verde SOLO a las casillas marcadas */
        div[data-testid="stCheckbox"] input[type="checkbox"]:checked + div {
            background-color: #28a745 !important;
            border-color: #28a745 !important;
        }
        
        /* Mantener las letras de las respuestas siempre negras/oscuras */
        div[data-testid="stCheckbox"] label p {
            color: #31333F !important;
            font-weight: 500;
            font-size: 1.1rem !important;
        }
        
        /* Alinear perfectamente la imagen al centro vertical de la respuesta */
        div[data-testid="stHorizontalBlock"] {
            align-items: center !important;
            margin-bottom: -10px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Selección única con **UN SOLO CLIC**:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Un solo clic - Selección Única)
# ==========================================
st.markdown("### 1. Edad")

if "edad_final" not in st.session_state:
    st.session_state.edad_final = "de 20 a 40 años"

# Opción 1: 20 a 40 años
col1_img, col1_chk = st.columns([1, 6])
with col1_img:
    st.image("edad_20.png", width=55)
with col1_chk:
    if st.checkbox("de 20 a 40 años", value=(st.session_state.edad_final == "de 20 a 40 años"), key="chk_e1"):
        st.session_state.edad_final = "de 20 a 40 años"

# Opción 2: 41 a 60 años
col2_img, col2_chk = st.columns([1, 6])
with col2_img:
    st.image("edad_21.png", width=55)
with col2_chk:
    if st.checkbox("de 41 a 60 años", value=(st.session_state.edad_final == "de 41 a 60 años"), key="chk_e2"):
        st.session_state.edad_final = "de 41 a 60 años"

# Opción 3: más de 60 años
col3_img, col3_chk = st.columns([1, 6])
with col3_img:
    st.image("edad_60.png", width=55)
with col3_chk:
    if st.checkbox("más de 60 años", value=(st.session_state.edad_final == "más de 60 años"), key="chk_e3"):
        st.session_state.edad_final = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Un solo clic - Selección Única)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_final" not in st.session_state:
    st.session_state.civil_final = "Casado"

# Opción 1: Casado
col4_img, col4_chk = st.columns([1, 6])
with col4_img:
    st.image("estado_casado.png", width=55)
with col4_chk:
    if st.checkbox("Casado", value=(st.session_state.civil_final == "Casado"), key="chk_c1"):
        st.session_state.civil_final = "Casado"

# Opción 2: Soltero
col5_img, col5_chk = st.columns([1, 6])
with col5_img:
    st.image("estado_soltero.png", width=55)
with col5_chk:
    if st.checkbox("Soltero", value=(st.session_state.civil_final == "Soltero"), key="chk_c2"):
        st.session_state.civil_final = "Soltero"

# Opción 3: Viudo / Divorciado
col6_img, col6_chk = st.columns([1, 6])
with col6_img:
    st.image("estado_divorciado.png", width=55)
with col6_chk:
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
