import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 DISEÑO Y COLORES (Personalización a Verde)
# ==========================================
st.markdown("""
    <style>
        /* Cambia el color del círculo seleccionado a Verde */
        div[data-testid="stMarkdownContainer"] p {
            margin-bottom: 0px;
        }
        /* Color verde para el botón de radio seleccionado */
        stWidgetForm div[role="radiogroup"] input[type="radio"]:checked + div {
            background-color: #28a745 !important;
            border-color: #28a745 !important;
        }
        input[type="radio"]:checked + div::after {
            background-color: #28a745 !important;
        }
        /* Forzar los componentes globales de Streamlit a usar acento verde */
        :root {
            --primary-color: #28a745 !important;
        }
        .st-emotion-cache-16idsys p {
            font-size: 16px !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones (Selección única):")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Un solo clic - Selección Única - Verde)
# ==========================================
st.markdown("### 1. Edad")

# Creamos la estructura visual hacia abajo
f1_col1, f1_col2 = st.columns([1, 5])
with f1_col1:
    st.image("edad_20.png", width=65)
    st.write("") # Espacio estético
    st.image("edad_21.png", width=65)
    st.write("")
    st.image("edad_60.png", width=65)

with f1_col2:
    # st.radio garantiza por defecto que SOLO se pueda elegir una respuesta a la vez
    edad = st.radio(
        "Selecciona tu rango de edad:",
        ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"],
        key="radio_edad",
        label_visibility="collapsed" # Oculta el título repetido para dejar solo las opciones
    )

st.write("---")

# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Un solo clic - Selección Única - Verde)
# ==========================================
st.markdown("### 2. Estado Civil")

f2_col1, f2_col2 = st.columns([1, 5])
with f2_col1:
    st.image("estado_casado.png", width=65)
    st.write("")
    st.image("estado_soltero.png", width=65)
    st.write("")
    st.image("estado_divorciado.png", width=65)

with f2_col2:
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
datos_a_guardar = f"=== RESUMEN DE RESPUESTAS ===\n• Rango de edad: {edad}\n• Estado civil:  {estado_civil}\n"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen_calculadora.txt",
    mime="text/plain"
)
