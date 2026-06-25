import streamlit as st

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊")

st.title("📊 Calculadora socio-económica")
st.write("Por favor, selecciona tus opciones para ver los resultados e imágenes en tiempo real.")

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
    
    # Asignar imagen según la edad (puedes cambiar las URLs por tus enlaces)
    if edad == "de 20 a 40 años":
        url_edad = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300"
    elif edad == "de 41 a 60 años":
        url_edad = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300"
    else:
        url_edad = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=300"
        
    st.image(url_edad, caption=f"Rango: {edad}", use_container_width=True)

with col_preg2:
    st.markdown("### 2. Estado Civil")
    estado_civil = st.selectbox(
        "Selecciona tu Estado Civil:",
        ["Casado", "Soltero", "Viudo / Divorciado"],
        key="civil_select"
    )
    
    # Asignar imagen según el estado civil (puedes cambiar las URLs por tus enlaces)
    if estado_civil == "Casado":
        url_civil = "https://images.unsplash.com/photo-1515934751635-c81c6bc9a2d8?w=300"
    elif estado_civil == "Soltero":
        url_civil = "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=300"
    else:
        url_civil = "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=300"
        
    st.image(url_civil, caption=f"Estado: {estado_civil}", use_container_width=True)

st.write("---")

# Botón para descargar el resumen en un archivo de texto
datos_a_guardar = f"=== RESUMEN DE RESPUESTAS ===\n• Rango de edad: {edad}\n• Estado civil:  {estado_civil}\n"

st.download_button(
    label="📥 Descargar respuestas en mi PC",
    data=datos_a_guardar,
    file_name="resumen_calculadora.txt",
    mime="text/plain"
)
