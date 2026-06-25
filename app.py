import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 REGLAS DE COLOR VERDE CORPORATIVO
# ==========================================
st.markdown("""
    <style>
        /* Forzar los componentes globales de Streamlit a usar acento verde */
        :root {
            --primary-color: #28a745 !important;
        }
        /* Color verde para el botón de radio seleccionado */
        input[type="radio"]:checked + div div {
            border-color: #28a745 !important;
            background-color: #28a745 !important;
        }
        /* Eliminar márgenes internos molestos para juntar los elementos */
        .stDeployButton { display:none; }
        div[data-testid="stHorizontalBlock"] {
            align-items: center !important;
            margin-bottom: -10px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones (Un solo clic):")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Imagen y Letra perfectamente juntos)
# ==========================================
st.markdown("### 1. Edad")

# Creamos un grupo de radio oculto para gestionar la selección única detrás de escena
if "edad_seleccionada" not in st.session_state:
    st.session_state.edad_seleccionada = "de 20 a 40 años"

# Fila Opción 1
col_img1, col_txt1 = st.columns([1, 8])
with col_img1:
    st.image("edad_20.png", width=55)
with col_txt1:
    if st.radio(" ", ["de 20 a 40 años"], key="r_edad1", label_visibility="collapsed", index=0 if st.session_state.edad_seleccionada == "de 20 a 40 años" else None):
        st.session_state.edad_seleccionada = "de 20 a 40 años"

# Fila Opción 2
col_img2, col_txt2 = st.columns([1, 8])
with col_img2:
    st.image("edad_21.png", width=55)
with col_txt2:
    if st.radio(" ", ["de 41 a 60 años"], key="r_edad2", label_visibility="collapsed", index=0 if st.session_state.edad_seleccionada == "de 41 a 60 años" else None):
        st.session_state.edad_seleccionada = "de 41 a 60 años"

# Fila Opción 3
col_img3, col_txt3 = st.columns([1, 8])
with col_img3:
    st.image("edad_60.png", width=55)
with col_txt3:
    if st.radio(" ", ["más de 60 años"], key="r_edad3", label_visibility="collapsed", index=0 if st.session_state.edad_seleccionada == "más de 60 años" else None):
        st.session_state.edad_seleccionada = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Imagen y Letra perfectamente juntos)
# ==========================================
st.markdown("### 2. Estado Civil")

if "civil_seleccionado" not in st.session_state:
    st.session_state.civil_seleccionado = "Casado"

# Fila Opción 1
col_img4, col_txt4 = st.columns([1, 8])
with col_img4:
    st.image("estado_casado.png", width=55)
with col_txt4:
    if st.radio(" ", ["Casado"], key="r_civil1", label_visibility="collapsed", index=0 if st.session_state.civil_seleccionado == "Casado" else None):
        st.session_state.civil_seleccionado = "Casado"

# Fila Opción 2
col_img5, col_txt5 = st.columns([1, 8])
with col_img5:
    st.image("estado_soltero.png", width=55)
with col_txt5:
    if st.radio(" ", ["Soltero"], key="r_civil2
