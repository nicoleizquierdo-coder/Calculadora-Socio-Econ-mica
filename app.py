import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 PERSONALIZACIÓN CSS (Punto Verde, Letras Negras)
# ==========================================
st.markdown("""
    <style>
        /* 1. Mantenemos el color de las letras siempre negro/oscuro */
        div[role="radiogroup"] label p {
            color: #31333F !important;
            font-weight: 500;
            font-size: 1.1rem !important;
        }

        /* 2. Color Verde solo para el punto circular cuando está seleccionado */
        div[role="radiogroup"] [data-checked="true"] > div:first-child {
            border-color: #28a745 !important;
        }
        div[role="radiogroup"] [data-checked="true"] > div:first-child::after {
            background-color: #28a745 !important;
        }

        /* 3. Ajuste de alineación para que las imágenes coincidan con el radio */
        div[data-testid="stVerticalBlock"] > div:has(img) {
            margin-bottom: 23px !important; /* Espacio entre imágenes */
        }
        
        /* Ocultar barra de botones superior */
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Selección única. Las imágenes están vinculadas a cada respuesta:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD
# ==========================================
st.markdown("### 1. Edad")

col_img1, col_rad1 = st.columns([1, 4])

with col_img1:
    # Mostramos las 3 imágenes en fila vertical
    st.image("edad_20.png", width=60)
    st.image("edad_21.png", width=60)
    st.image("edad_60.png", width=60)

with col_rad1:
    # Un solo st.radio garantiza Selección Única y un solo clic
    edad = st.radio(
        "Selecciona edad:",
        ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"],
        key="radio_edad",
        label_visibility="collapsed"
    )

st.write("---")

# ==========================================
# PREGUNTA 2: ESTADO CIVIL
# ==========================================
st.markdown("### 2. Estado Civil")

col_img2, col_rad2 = st.columns([1, 4])

with col_img2:
    st.image("estado_casado.png", width=60)
    st.image("estado_soltero.png", width=60)
    st.image("estado_divorciado.png", width=60)

with col_rad2:
    estado_civil = st.radio(
        "Selecciona estado civil:",
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
