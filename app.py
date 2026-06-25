import streamlit as st



st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")



# ==========================================

# 🎨 REGLAS DE COLOR: BOTÓN SELECCIONADO EN VERDE

# ==========================================

st.markdown("""

    <style>

        /* Desactivar el botón flotante de Deploy */

        .stDeployButton { display:none; }

        

        /* Ajustar espacios verticales */

        div[data-testid="stHorizontalBlock"] {

            align-items: center !important;

            margin-bottom: 5px !important;

        }

    </style>

""", unsafe_allow_html=True)



st.title("📊 Calculadora socio-económica")

st.write("Selección única con un solo clic (Las imágenes y respuestas están juntas):")



st.write("---")



# ==========================================

# PREGUNTA 1: EDAD (Selección Única - Un solo clic)

# ==========================================

st.markdown("### 1. Edad")



if "edad_final" not in st.session_state:

    st.session_state.edad_final = "de 20 a 40 años"



# Opción 1: 20 a 40 años

col1_img, col1_btn = st.columns([1, 6])

with col1_img:

    st.image("edad_20.png", width=55)

with col1_btn:

    # Si está seleccionado, le ponemos un indicador visual limpio al texto del botón

    label_1 = "🟢 de 20 a 40 años" if st.session_state.edad_final == "de 20 a 40 años" else "⚪ de 20 a 40 años"

    if st.button(label_1, key="btn_e1", use_container_width=True):

        st.session_state.edad_final = "de 20 a 40 años"



# Opción 2: 41 a 60 años

col2_img, col2_btn = st.columns([1, 6])

with col2_img:

    st.image("edad_21.png", width=55)

with col2_btn:

    label_2 = "🟢 de 41 a 60 años" if st.session_state.edad_final == "de 41 a 60 años" else "⚪ de 41 a 60 años"

    if st.button(label_2, key="btn_e2", use_container_width=True):

        st.session_state.edad_final = "de 41 a 60 años"



# Opción 3: más de 60 años

col3_img, col3_btn = st.columns([1, 6])

with col3_img:

    st.image("edad_60.png", width=55)

with col3_btn:

    label_3 = "🟢 más de 60 años" if st.session_state.edad_final == "más de 60 años" else "⚪ más de 60 años"

    if st.button(label_3, key="btn_e3", use_container_width=True):

        st.session_state.edad_final = "más de 60 años"





st.write("---")





# ==========================================

# PREGUNTA 2: ESTADO CIVIL (Selección Única - Un solo clic)

# ==========================================

st.markdown("### 2. Estado Civil")



if "civil_final" not in st.session_state:

    st.session_state.civil_final = "Casado"



# Opción 1: Casado

col4_img, col4_btn = st.columns([1, 6])

with col4_img:

    st.image("estado_casado.png", width=55)

with col4_btn:

    label_c1 = "🟢 Casado" if st.session_state.civil_final == "Casado" else "⚪ Casado"

    if st.button(label_c1, key="btn_c1", use_container_width=True):

        st.session_state.civil_final = "Casado"



# Opción 2: Soltero

col5_img, col5_btn = st.columns([1, 6])

with col5_img:

    st.image("estado_soltero.png", width=55)

with col5_btn:

    label_c2 = "🟢 Soltero" if st.session_state.civil_final == "Soltero" else "⚪ Soltero"

    if st.button(label_c2, key="btn_c2", use_container_width=True):

        st.session_state.civil_final = "Soltero"



# Opción 3: Viudo / Divorciado

col6_img, col6_btn = st.columns([1, 6])

with col6_img:

    st.image("estado_divorciado.png", width=55)

with col6_btn:

    label_c3 = "🟢 Viudo / Divorciado" if st.session_state.civil_final == "Viudo / Divorciado" else "⚪ Viudo / Divorciado"

    if st.button(label_c3, key="btn_c3", use_container_width=True):

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

