import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones para ver los resultados:")

st.write("---")

# Creamos dos columnas para poner las preguntas una al lado de la otra
col_preg1, col_preg2 = st.columns(2)

with col_preg1:
    st.markdown("### 1. Edad")
    edad = st.selectbox(
        "Selecciona tu rango de edad:",
        ["de 20 a 40 años", "de 41 a 60 años", "más de 60 años"],
        key="edad_select"
    )
    
    # --- AQUÍ ASIGNAMOS TUS IMÁGENES DE EDAD ---
    if edad == "de 20 a 40 años":
        imagen_edad = "edad_20.png"
    elif edad == "de 41 a 60 años":
        imagen_edad = "edad_21.png"
    else:
        imagen_edad = "edad_60.png"
        
    # Mostramos tu imagen en la pantalla
    st.image(imagen_edad, caption=f"Rango: {edad}", use_container_width=True)

with col_preg2:
    st.markdown("### 2. Estado Civil")
    estado_civil = st.selectbox(
        "Selecciona tu Estado Civil:",
        ["Casado", "Soltero", "Viudo / Divorciado"],
        key="civil_select"
    )
    
    # --- AQUÍ ASIGNAMOS TUS IMÁGENES DE ESTADO CIVIL ---
    if estado_civil == "Casado":
        imagen_civil = "estado_casado.png"
    elif estado_civil == "Soltero":
        imagen_civil = "estado_soltero.png"
    else:
        # Asumimos que para "Viudo / Divorciado" usas la de divorciado
        imagen_civil = "estado_divorciado.png"
        
    # Mostramos tu imagen en la pantalla
    st.image(imagen_civil, caption=f"Estado: {estado_civil}", use_container_width=True)

st.write("---")

# Botón para descargar el archivo de texto
datos_a_guardar = f"=== RESUMEN DE RESPUESTAS ===\n• Rango de edad: {edad}\n• Estado civil:  {estado_civil}\n"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen_calculadora.txt",
    mime="text/plain"
)
