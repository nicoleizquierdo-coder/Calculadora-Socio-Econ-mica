import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 EL CSS DEFINITIVO: PUNTO VERDE Y LETRAS NEGRAS
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

        /* 3. Ajuste milimétrico de las imágenes para que se alineen con el texto */
        div[data-testid="stVerticalBlock"] > div:has(img) {
            margin-bottom: 25px !important; 
        }
        
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Selección única con un solo clic:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Un solo clic - Selección Única)
# ==========================================
st.markdown("### 1. Edad")

col1_img, col1_rad = st.columns([1, 5])

with col1_img:
    # Colocamos las tres imágenes una debajo de la otra
    st.image("edad_20.png", width=55)
    st.image("edad_21.png", width=55)
    st.image("edad_60.png", width=55)

with col1_rad:
    # Un solo st.radio nativo: SOLUCIONA EL DOBLE CLIC y la selección múltiple
    edad = st.radio(
        "Selecciona rango de edad:",
        ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"],
        key="radio_edad",
        label_visibility="collapsed"
    )

st.write("---")

# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Un solo clic - Selección Única)
# ==========================================
st.markdown("### 2. Estado Civil")

col2_img, col2_rad = st.columns([1, 5])

with col2_img:
    st.image("estado_casado.png", width=55)
    st.image("estado_soltero.png", width=55)
    st.image("estado_divorciado.png", width=55)

with col2_rad:
    estado_civil = st.radio(
        "Selecciona tu Estado Civil:",
        ["Casado", "Soltero", "Viudo / Divorciado"],
        key="radio_civil",
        label_visibility="collapsed"
    )

st.write("---")

# ==========================================
# BOTÓN DE DESCARGA
# ==========================================
datos_a_guardar = f"=== RESUMEN ===\nEdad: {edad}\nEstado Civil: {estado_civil}"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen.txt",
    mime="text/plain"
)
