import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 PERSONALIZACIÓN CSS (Punto Verde, Letras Negras y Alineación Total)
# ==========================================
st.markdown("""
    <style>
        /* 1. Asegurar que las letras permanezcan negras/oscuras */
        div[role="radiogroup"] label p {
            color: #31333F !important;
            font-weight: 500;
            font-size: 1.1rem !important;
        }

        /* 2. Color Verde únicamente para el punto circular seleccionado */
        div[role="radiogroup"] [data-checked="true"] > div:first-child {
            border-color: #28a745 !important;
        }
        div[role="radiogroup"] [data-checked="true"] > div:first-child::after {
            background-color: #28a745 !important;
        }

        /* 3. Forzar a que la imagen y el botón se alineen perfectamente al centro de la fila */
        div[data-testid="stHorizontalBlock"] {
            align-items: center !important;
            margin-bottom: 5px !important;
            gap: 10px !important; /* Une la imagen al texto */
        }
        
        /* Ocultar barra superior de Streamlit */
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones (Un solo clic):")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Imagen y Letra amarradas por fila)
# ==========================================
st.markdown("### 1. Edad")

# Controlamos el estado de selección única
if "edad_seleccionada" not in st.session_state:
    st.session_state.edad_seleccionada = "de 20 a 40 años"

# Fila 1: Opción 1
col_img1, col_txt1 = st.columns([1, 10])
with col_img1:
    st.image("edad_20.png", width=50)
with col_txt1:
    if st.radio(" ", ["de 20 a 40 años"], key="r_edad_1", label_visibility="collapsed", index=0 if st.session_state.edad_seleccionada == "de 20 a 40 años" else None):
        st.session_state.edad_seleccionada = "de 20 a 40 años"

# Fila 2: Opción 2
col_img2, col_txt2 = st.columns([1, 10])
with col_img2:
    st.image("edad_21.png", width=50)
with col_txt2:
    if st.radio(" ", ["de 41 a 60 años"], key="r_edad_2", label_visibility="collapsed", index=0 if st.session_state.edad_seleccionada == "de 41 a 60 años" else None):
        st.session_state.edad_seleccionada = "de 41 a 60 años"

# Fila 3: Opción 3
col_img3, col_txt3 = st.columns([1, 10])
with col_img3:
    st.image("edad_60.png", width=50)
with col_txt3:
    if st.radio(" ", ["más de 60 años"], key="r_edad_3", label_visibility="collapsed", index=0 if st.session_state.edad_seleccionada == "más de 60 años" else None):
        st.session_state.edad_seleccionada = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Imagen y Letra amarradas por fila)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_seleccionado" not in st.session_state:
    st.session_state.civil_seleccionado = "Casado"

# Fila 1: Opción 1
col_img4, col_txt4 = st.columns([1, 10])
with col_img4:
    st.image("estado_casado.png", width=50)
with col_txt4:
    if st.radio(" ", ["Casado"], key="r_civil_1", label_visibility="collapsed", index=0 if st.session_state.civil_seleccionado == "Casado" else None):
        st.session_state.civil_seleccionado = "Casado"

# Fila 2: Opción 2
col_img5, col_txt5 = st.columns([1, 10])
with col_img5:
    st.image("estado_soltero.png", width=50)
with col_txt5:
    if st.radio(" ", ["Soltero"], key="r_civil_2", label_visibility="collapsed", index=0 if st.session_state.civil_seleccionado == "Soltero" else None):
        st.session_state.civil_seleccionado = "Soltero"

# Fila 3: Opción 3
col_img6, col_txt6 = st.columns([1, 10])
with col_img6:
    st.image("estado_divorciado.png", width=50)
with col_txt6:
    if st.radio(" ", ["Viudo / Divorciado"], key="r_civil_3", label_visibility="collapsed", index=0 if st.session_state.civil_seleccionado == "Viudo / Divorciado" else None):
        st.session_state.civil_seleccionado = "Viudo / Divorciado"


st.write("---")


# ==========================================
# BOTÓN DE DESCARGA
# ==========================================
datos_a_guardar = f"=== RESUMEN ===\nEdad: {st.session_state.edad_seleccionada}\nEstado Civil: {st.session_state.civil_seleccionado}"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen.txt",
    mime="text/plain"
)
