import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 REGLAS DE DISEÑO: PUNTO VERDE Y LETRAS NEGRAS
# ==========================================
st.markdown("""
    <style>
        /* 1. Mantener las letras siempre negras/oscuras */
        div[role="radiogroup"] label p {
            color: #31333F !important;
            font-weight: 500;
            font-size: 1.1rem !important;
            display: inline-flex;
            align-items: center;
        }

        /* 2. Color Verde únicamente para el punto circular cuando está seleccionado */
        div[role="radiogroup"] [data-checked="true"] > div:first-child {
            border-color: #28a745 !important;
        }
        div[role="radiogroup"] [data-checked="true"] > div:first-child::after {
            background-color: #28a745 !important;
        }

        /* 3. Ajustar el espacio de las filas para que la imagen quepa perfectamente */
        div[role="radiogroup"] label {
            padding: 10px 0px !important;
            min-height: 65px !important;
            display: flex !important;
            align-items: center !important;
        }
        
        /* Ocultar barra superior de Streamlit */
        .stDeployButton { display:none; }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Selección única garantizada con un solo clic:")

st.write("---")

# ==========================================
# PREGUNTA 1: EDAD (Imágenes inyectadas junto al texto)
# ==========================================
st.markdown("### 1. Edad")

# Creamos las opciones mezclando el HTML de tu imagen con el texto
opciones_edad = [
    f'<img src="app/static/edad_20.png" width="45" style="margin-right:15px; vertical-align:middle; border-radius:4px;"> de 20 a 40 años',
    f'<img src="app/static/edad_21.png" width="45" style="margin-right:15px; vertical-align:middle; border-radius:4px;"> de 41 a 60 años',
    f'<img src="app/static/edad_60.png" width="45" style="margin-right:15px; vertical-align:middle; border-radius:4px;"> más de 60 años'
]

# Un solo st.radio controla todo -> Imposible seleccionar varias
seleccion_edad_raw = st.radio(
    "Edad",
    opciones_edad,
    key="radio_edad",
    label_visibility="collapsed"
)

# Limpiamos el HTML para guardar solo el texto limpio en tu archivo final
if "20 a 40" in seleccion_edad_raw:
    edad_final = "de 20 a 40 años"
elif "41 a 60" in seleccion_edad_raw:
    edad_final = "de 41 a 60 años"
else:
    edad_final = "más de 60 años"


st.write("---")


# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Imágenes inyectadas junto al texto)
# ==========================================
st.markdown("### 2. Estado Civil")

opciones_civil = [
    f'<img src="app/static/estado_casado.png" width="45" style="margin-right:15px; vertical-align:middle; border-radius:4px;"> Casado',
    f'<img src="app/static/estado_soltero.png" width="45" style="margin-right:15px; vertical-align:middle; border-radius:4px;"> Soltero',
    f'<img src="app/static/estado_divorciado.png" width="45" style="margin-right:15px; vertical-align:middle; border-radius:4px;"> Viudo / Divorciado'
]

seleccion_civil_raw = st.radio(
    "Estado Civil",
    opciones_civil,
    key="radio_civil",
    label_visibility="collapsed"
)

if "Casado" in seleccion_civil_raw:
    civil_final = "Casado"
elif "Soltero" in seleccion_civil_raw:
    civil_final = "Soltero"
else:
    civil_final = "Viudo / Divorciado"


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
