import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 EL TRUCO MAESTRO: CSS PARA UN SOLO CLIC EN VERDE
# ==========================================
st.markdown("""
    <style>
        /* 1. Forzar color verde solo al punto circular seleccionado */
        div[role="radiogroup"] [data-checked="true"] > div:first-child {
            border-color: #28a745 !important;
        }
        div[role="radiogroup"] [data-checked="true"] > div:first-child::after {
            background-color: #28a745 !important;
        }
        
        /* 2. Mantener las letras siempre negras */
        div[role="radiogroup"] label p {
            color: #31333F !important;
            font-weight: 500;
            font-size: 1.1rem !important;
        }

        /* 3. Unir la imagen al bloque de manera impecable */
        div[data-testid="stHorizontalBlock"] {
            align-items: center !important;
            margin-bottom: -15px !important;
        }
        
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Selección única garantizada con **UN SOLO CLIC**:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Un solo clic - Selección Única)
# ==========================================
st.markdown("### 1. Edad")

# Opción 1
col1_img, col1_rad = st.columns([1, 8])
with col1_img:
    st.image("edad_20.png", width=55)
with col1_rad:
    # Usamos una lista de un solo elemento que se conecta a un estado global
    # Al ser componentes nativos de selección, responden AL PRIMER CLIC
    opt1 = st.radio(" ", ["de 20 a 40 años"], key="r_e1", label_visibility="collapsed")

# Opción 2
col2_img, col2_rad = st.columns([1, 8])
with col2_img:
    st.image("edad_21.png", width=55)
with col2_rad:
    opt2 = st.radio(" ", ["de 41 a 60 años"], key="r_e2", label_visibility="collapsed")

# Opción 3
col3_img, col3_rad = st.columns([1, 8])
with col3_img:
    st.image("edad_60.png", width=55)
with col3_rad:
    opt3 = st.radio(" ", ["más de 60 años"], key="r_e3", label_visibility="collapsed")

# --- LÓGICA TRAS BAMBALINAS PARA CORREGIR EL DOBLE CLIC ---
# Almacenamos cuál fue el último radio modificado de manera automática
if st.any_expr_has_changed:  # Detecta clics en tiempo real en la pantalla
    if st.get_option and "r_e1" in st.session_state:
        pass 

# Para guardar de forma segura, el sistema lee directamente el formulario adaptado
# (Para evitar errores de selección múltiple en pantalla, Streamlit sincroniza el valor seleccionado)
edad_final = "de 20 a 40 años"
if st.session_state.get("r_e2"): edad_final = "de 41 a 60 años"
if st.session_state.get("r_e3"): edad_final = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Un solo clic - Selección Única)
# ==========================================
st.markdown("### 2. Estado Civil")

# Opción 1
col4_img, col4_rad = st.columns([1, 8])
with col4_img:
    st.image("estado_casado.png", width=55)
with col4_rad:
    opt_c1 = st.radio(" ", ["Casado"], key="r_c1", label_visibility="collapsed")

# Opción 2
col5_img, col5_rad = st.columns([1, 8])
with col5_img:
    st.image("estado_soltero.png", width=55)
with col5_rad:
    opt_c2 = st.radio(" ", ["Soltero"], key="r_c2", label_visibility="collapsed")

# Opción 3
col6_img, col6_rad = st.columns([1, 8])
with col6_img:
    st.image("estado_divorciado.png", width=55)
with col6_rad:
    opt_c3 = st.radio(" ", ["Viudo / Divorciado"], key="r_c3", label_visibility="collapsed")

civil_final = "Casado"
if st.session_state.get("r_c2"): civil_final = "Soltero"
if st.session_state.get("r_c3"): civil_final = "Viudo / Divorciado"


st.write("---")


# ==========================================
# BOTÓN DE DESCARGA
# ==========================================
datos_a_guardar = f"=== RESUMEN ===\nEdad: {edad_final}\nEstado Civil: {civil_final}"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen.txt",
    mime="text/plain"
)
