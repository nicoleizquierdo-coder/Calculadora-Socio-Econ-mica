import streamlit as st
import os

st.set_page_config(page_title="Calculadora socio-económica", page_icon="📊", layout="centered")

# ==========================================
# 🎨 REGLAS DE DISEÑO DEFINITIVAS
# ==========================================
st.markdown("""
    <style>
        /* Desactivar el botón flotante de Deploy */
        .stDeployButton { display:none; }
        
        /* Ajustar espacios verticales para alinear la imagen/emoji con el botón */
        div[data-testid="stHorizontalBlock"] {
            align-items: center !important;
            margin-bottom: 5px !important;
        }
        
        /* Estilo personalizado para el cuadro de resultados final */
        .resultado-box {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #28a745;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Función de seguridad unificada para todo el formulario
def cargar_imagen_segura(ruta, emoji_auxiliar):
    if os.path.exists(ruta):
        try:
            st.image(ruta, width=55)
        except Exception:
            st.markdown(f"<h2 style='text-align: center; margin: 0; padding-bottom: 10px;'>{emoji_auxiliar}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center; margin: 0; padding-bottom: 10px;'>{emoji_auxiliar}</h2>", unsafe_allow_html=True)

st.title("📊 Calculadora socio-económica")
st.write("Selección única con un solo clic y cálculo de porcentaje en tiempo real:")

st.write("---")

# Diccionarios de puntuación para los cálculos internos
valores_edad = {"de 20 a 40 años": 1, "de 41 a 60 años": 2, "más de 61 años": 3}
valores_civil = {"Casado": 1, "Soltero": 2, "Viudo / Divorciado": 3}
valores_familia = {"1-2 personas": 1, "2-4 personas": 2, "5+ personas": 3}
valores_educacion = {"Superior +": 1, "Superior": 2, "1-2 nivel": 3}
valores_empleo = {"Propio": 1, "Formal": 2, "Desempleado": 3}
valores_vehiculo = {"Si": 1, "N/A": 2, "No": 3}
valores_seguro = {"Si": 1, "Si (Limitado)": 2, "No": 3}
valores_material = {"Hormigón / Ladrillo": 1, "N/A": 2, "Madera, caña, etc.": 3}
valores_tenencia = {"Propia": 1, "Rentada": 2, "Prestada": 3}
valores_enfermedad = {"No": 1, "N/A": 2, "Si": 3}
valores_seguridad = {"Si": 1, "N/A": 2, "No": 3}

# ==========================================
# PREGUNTA 1: EDAD (Peso: 1)
# ==========================================
st.markdown("### 1. Edad")
if "edad_final" not in st.session_state:
    st.session_state.edad_final = "de 20 a 40 años"

col1_img, col1_btn = st.columns([1, 6])
with col1_img:
    cargar_imagen_segura("edad_20.png", "👤")
with col1_btn:
    label_1 = "🟢 de 20 a 40 años" if st.session_state.edad_final == "de 20 a 40 años" else "⚪ de 20 a 40 años"
    if st.button(label_1, key="btn_e1", use_container_width=True):
        st.session_state.edad_final = "de 20 a 40 años"
        st.rerun()

col2_img, col2_btn = st.columns([1, 6])
with col2_img:
    cargar_imagen_segura("edad_21.png", "👥")
with col2_btn:
    label_2 = "🟢 de 41 a 60 años" if st.session_state.edad_final == "de 41 a 60 años" else "⚪ de 41 a 60 años"
    if st.button(label_2, key="btn_e2", use_container_width=True):
        st.session_state.edad_final = "de 41 a 60 años"
        st.rerun()

col3_img, col3_btn = st.columns([1, 6])
with col3_img:
    cargar_imagen_segura("edad_60.png", "👴")
with col3_btn:
    label_3 = "🟢 más de 61 años" if st.session_state.edad_final == "más de 61 años" else "⚪ más de 61 años"
    if st.button(label_3, key="btn_e3", use_container_width=True):
        st.session_state.edad_final = "más de 61 años"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 2: ESTADO CIVIL (Peso: 1)
# ==========================================
st.markdown("### 2. Estado Civil")
if "civil_final" not in st.session_state:
    st.session_state.civil_final = "Casado"

col4_img, col4_btn = st.columns([1, 6])
with col4_img:
    cargar_imagen_segura("estado_casado.png", "💍")
with col4_btn:
    label_c1 = "🟢 Casado" if st.session_state.civil_final == "Casado" else "⚪ Casado"
    if st.button(label_c1, key="btn_c1", use_container_width=True):
        st.session_state.civil_final = "Casado"
        st.rerun()

col5_img, col5_btn = st.columns([1, 6])
with col5_img:
    cargar_imagen_segura("estado_soltero.png", "🚶")
with col5_btn:
    label_c2 = "🟢 Soltero" if st.session_state.civil_final == "Soltero" else "⚪ Soltero"
    if st.button(label_c2, key="btn_c2", use_container_width=True):
        st.session_state.civil_final = "Soltero"
        st.rerun()

col6_img, col6_btn = st.columns([1, 6])
with col6_img:
    cargar_imagen_segura("estado_divorciado.png", "✂️")
with col6_btn:
    label_c3 = "🟢 Viudo / Divorciado" if st.session_state.civil_final == "Viudo / Divorciado" else "⚪ Viudo / Divorciado"
    if st.button(label_c3, key="btn_c3", use_container_width=True):
        st.session_state.civil_final = "Viudo / Divorciado"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 3: PERSONAS EN FAMILIA (Peso: 1)
# ==========================================
st.markdown("### 3. Personas en familia")
if "familia_final" not in st.session_state:
    st.session_state.familia_final = "1-2 personas"

col7_img, col7_btn = st.columns([1, 6])
with col7_img:
    cargar_imagen_segura("familia_1.jpg", "🏡")
with col7_btn:
    label_f1 = "🟢 1-2 personas" if st.session_state.familia_final == "1-2 personas" else "⚪ 1-2 personas"
    if st.button(label_f1, key="btn_f1", use_container_width=True):
        st.session_state.familia_final = "1-2 personas"
        st.rerun()

col8_img, col8_btn = st.columns([1, 6])
with col8_img:
    cargar_imagen_segura("familia_2.png", "👨‍👩‍👦")
with col8_btn:
    label_f2 = "🟢 2-4 personas" if st.session_state.familia_final == "2-4 personas" else "⚪ 2-4 personas"
    if st.button(label_f2, key="btn_f2", use_container_width=True):
        st.session_state.familia_final = "2-4 personas"
        st.rerun()

col9_img, col9_btn = st.columns([1, 6])
with col9_img:
    cargar_imagen_segura("familia_3.png", "👨‍👩‍👧‍👦")
with col9_btn:
    label_f3 = "🟢 5+ personas" if st.session_state.familia_final == "5+ personas" else "⚪ 5+ personas"
    if st.button(label_f3, key="btn_f3", use_container_width=True):
        st.session_state.familia_final = "5+ personas"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 4: NIVEL EDUCATIVO (Peso: 1)
# ==========================================
st.markdown("### 4. Nivel educativo")
if "educacion_final" not in st.session_state:
    st.session_state.educacion_final = "Superior +"

col10_img, col10_btn = st.columns([1, 6])
with col10_img:
    cargar_imagen_segura("educacion_1.png", "🎓")
with col10_btn:
    label_ed1 = "🟢 Superior +" if st.session_state.educacion_final == "Superior +" else "⚪ Superior +"
    if st.button(label_ed1, key="btn_ed1", use_container_width=True):
        st.session_state.educacion_final = "Superior +"
        st.rerun()

col11_img, col11_btn = st.columns([1, 6])
with col11_img:
    cargar_imagen_segura("educacion_2.png", "📜")
with col11_btn:
    label_ed2 = "🟢 Superior" if st.session_state.educacion_final == "Superior" else "⚪ Superior"
    if st.button(label_ed2, key="btn_ed2", use_container_width=True):
        st.session_state.educacion_final = "Superior"
        st.rerun()

col12_img, col12_btn = st.columns([1, 6])
with col12_img:
    cargar_imagen_segura("educacion_3.png", "🏫")
with col12_btn:
    label_ed3 = "🟢 1-2 nivel" if st.session_state.educacion_final == "1-2 nivel" else "⚪ 1-2 nivel"
    if st.button(label_ed3, key="btn_ed3", use_container_width=True):
        st.session_state.educacion_final = "1-2 nivel"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 5: TIPO DE EMPLEO (Peso: 1)
# ==========================================
st.markdown("### 5. Tipo de empleo")
if "empleo_final" not in st.session_state:
    st.session_state.empleo_final = "Propio"

col13_img, col13_btn = st.columns([1, 6])
with col13_img:
    cargar_imagen_segura("empleo_1.png", "💼")
with col13_btn:
    label_emp1 = "🟢 Propio" if st.session_state.empleo_final == "Propio" else "⚪ Propio"
    if st.button(label_emp1, key="btn_emp1", use_container_width=True):
        st.session_state.empleo_final = "Propio"
        st.rerun()

col14_img, col14_btn = st.columns([1, 6])
with col14_img:
    cargar_imagen_segura("empleo_2.png", "🏢")
with col14_btn:
    label_emp2 = "🟢 Formal" if st.session_state.empleo_final == "Formal" else "⚪ Formal"
    if st.button(label_emp2, key="btn_emp2", use_container_width=True):
        st.session_state.empleo_final = "Formal"
        st.rerun()

col15_img, col15_btn = st.columns([1, 6])
with col15_img:
    cargar_imagen_segura("empleo_3.png", "🛑")
with col15_btn:
    label_emp3 = "🟢 Desempleado" if st.session_state.empleo_final == "Desempleado" else "⚪ Desempleado"
    if st.button(label_emp3, key="btn_emp3", use_container_width=True):
        st.session_state.empleo_final = "Desempleado"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 6: TIENE VEHÍCULOS (Peso: 1)
# ==========================================
st.markdown("### 6. Tiene Vehículos")
if "vehiculo_final" not in st.session_state:
    st.session_state.vehiculo_final = "Si"

col16_img, col16_btn = st.columns([1, 6])
with col16_img:
    cargar_imagen_segura("vehiculo_1.png", "🚗")
with col16_btn:
    label_veh1 = "🟢 Si" if st.session_state.vehiculo_final == "Si" else "⚪ Si"
    if st.button(label_veh1, key="btn_veh1", use_container_width=True):
        st.session_state.vehiculo_final = "Si"
        st.rerun()

col17_img, col17_btn = st.columns([1, 6])
with col17_img:
    cargar_imagen_segura("vehiculo_2.png", "🔍")
with col17_btn:
    label_veh2 = "🟢 N/A" if st.session_state.vehiculo_final == "N/A" else "⚪ N/A"
    if st.button(label_veh2, key="btn_veh2", use_container_width=True):
        st.session_state.vehiculo_final = "N/A"
        st.rerun()

col18_img, col18_btn = st.columns([1, 6])
with col18_img:
    cargar_imagen_segura("vehiculo_3.png", "❌")
with col18_btn:
    label_veh3 = "🟢 No" if st.session_state.vehiculo_final == "No" else "⚪ No"
    if st.button(label_veh3, key="btn_veh3", use_container_width=True):
        st.session_state.vehiculo_final = "No"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 7: TIENE SEGURO PRIVADO (Peso: 1)
# ==========================================
st.markdown("### 7. Tiene Seguro Privado")
if "seguro_final" not in st.session_state:
    st.session_state.seguro_final = "Si"

col19_img, col19_btn = st.columns([1, 6])
with col19_img:
    cargar_imagen_segura("seguro_1.png", "🛡️")
with col19_btn:
    label_seg1 = "🟢 Si" if st.session_state.seguro_final == "Si" else "⚪ Si"
    if st.button(label_seg1, key="btn_seg1", use_container_width=True):
        st.session_state.seguro_final = "Si"
        st.rerun()

col20_img, col20_btn = st.columns([1, 6])
with col20_img:
    cargar_imagen_segura("seguro_2.png", "🩹")
with col20_btn:
    label_seg2 = "🟢 Si (Limitado)" if st.session_state.seguro_final == "Si (Limitado)" else "⚪ Si (Limitado)"
    if st.button(label_seg2, key="btn_seg2", use_container_width=True):
        st.session_state.seguro_final = "Si (Limitado)"
        st.rerun()

col21_img, col21_btn = st.columns([1, 6])
with col21_img:
    cargar_imagen_segura("seguro_3.png", "🚫")
with col21_btn:
    label_seg3 = "🟢 No" if st.session_state.seguro_final == "No" else "⚪ No"
    if st.button(label_seg3, key="btn_seg3", use_container_width=True):
        st.session_state.seguro_final = "No"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 8: MATERIALES DE LA VIVIENDA (Peso: 2)
# ==========================================
st.markdown("### 8. Materiales de la vivienda (Crítico)")
if "material_final" not in st.session_state:
    st.session_state.material_final = "Hormigón / Ladrillo"

col22_img, col22_btn = st.columns([1, 6])
with col22_img:
    cargar_imagen_segura("material_1.jpg", "🧱")
with col22_btn:
    label_mat1 = "🟢 Hormigón / Ladrillo" if st.session_state.material_final == "Hormigón / Ladrillo" else "⚪ Hormigón / Ladrillo"
    if st.button(label_mat1, key="btn_mat1", use_container_width=True):
        st.session_state.material_final = "Hormigón / Ladrillo"
        st.rerun()

col23_img, col23_btn = st.columns([1, 6])
with col23_img:
    cargar_imagen_segura("material_2.png", "⚪")
with col23_btn:
    label_mat2 = "🟢 N/A" if st.session_state.material_final == "N/A" else "⚪ N/A"
    if st.button(label_mat2, key="btn_mat2", use_container_width=True):
        st.session_state.material_final = "N/A"
        st.rerun()

col24_img, col24_btn = st.columns([1, 6])
with col24_img:
    cargar_imagen_segura("material_3.jpg", "🪵")
with col24_btn:
    label_mat3 = "🟢 Madera, caña, etc." if st.session_state.material_final == "Madera, caña, etc." else "⚪ Madera, caña, etc."
    if st.button(label_mat3, key="btn_mat3", use_container_width=True):
        st.session_state.material_final = "Madera, caña, etc."
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 9: TENENCIA VIVIENDA (Peso: 2)
# ==========================================
st.markdown("### 9. Tenencia vivienda (Crítico)")
if "tenencia_final" not in st.session_state:
    st.session_state.tenencia_final = "Propia"

col25_img, col25_btn = st.columns([1, 6])
with col25_img:
    cargar_imagen_segura("tenencia_1.png", "🔑")
with col25_btn:
    label_ten1 = "🟢 Propia" if st.session_state.tenencia_final == "Propia" else "⚪ Propia"
    if st.button(label_ten1, key="btn_ten1", use_container_width=True):
        st.session_state.tenencia_final = "Propia"
        st.rerun()

col26_img, col26_btn = st.columns([1, 6])
with col26_img:
    cargar_imagen_segura("tenencia_2.png", "💵")
with col26_btn:
    label_ten2 = "🟢 Rentada" if st.session_state.tenencia_final == "Rentada" else "⚪ Rentada"
    if st.button(label_ten2, key="btn_ten2", use_container_width=True):
        st.session_state.tenencia_final = "Rentada"
        st.rerun()

col27_img, col27_btn = st.columns([1, 6])
with col27_img:
    cargar_imagen_segura("tenencia_3.png", "🤝")
with col27_btn:
    label_ten3 = "🟢 Prestada" if st.session_state.tenencia_final == "Prestada" else "⚪ Prestada"
    if st.button(label_ten3, key="btn_ten3", use_container_width=True):
        st.session_state.tenencia_final = "Prestada"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 10: EXISTENCIA DE ENFERMEDADES (Peso: 2)
# ==========================================
st.markdown("### 10. Existencia de Enfermedades (Crítico)")
if "enfermedad_final" not in st.session_state:
    st.session_state.enfermedad_final = "No"

col28_img, col28_btn = st.columns([1, 6])
with col28_img:
    cargar_imagen_segura("enfermedad_1.png", "💚")
with col28_btn:
    label_enf1 = "🟢 No" if st.session_state.enfermedad_final == "No" else "⚪ No"
    if st.button(label_enf1, key="btn_enf1", use_container_width=True):
        st.session_state.enfermedad_final = "No"
        st.rerun()

col29_img, col29_btn = st.columns([1, 6])
with col29_img:
    cargar_imagen_segura("enfermedad_2.png", "🔷")
with col29_btn:
    label_enf2 = "🟢 N/A" if st.session_state.enfermedad_final == "N/A" else "⚪ N/A"
    if st.button(label_enf2, key="btn_enf2", use_container_width=True):
        st.session_state.enfermedad_final = "N/A"
        st.rerun()

col30_img, col30_btn = st.columns([1, 6])
with col30_img:
    cargar_imagen_segura("enfermedad_3.png", "⚠️")
with col30_btn:
    label_enf3 = "🟢 Si" if st.session_state.enfermedad_final == "Si" else "⚪ Si"
    if st.button(label_enf3, key="btn_enf3", use_container_width=True):
        st.session_state.enfermedad_final = "Si"
        st.rerun()

st.write("---")

# ==========================================
# PREGUNTA 11: SEGURIDAD SOCIAL (Peso: 2)
# ==========================================
st.markdown("### 11. Seguridad Social (Crítico)")
if "seguridad_social_final" not in st.session_state:
    st.session_state.seguridad_social_final = "Si"

col31_img, col31_btn = st.columns([1, 6])
with col31_img:
    cargar_imagen_segura("seguridad_1.png", "✅")
with col31_btn:
    label_ss1 = "🟢 Si" if st.session_state.seguridad_social_final == "Si" else "⚪ Si"
    if st.button(label_ss1, key="btn_ss1", use_container_width=True):
        st.session_state.seguridad_social_final = "Si"
        st.rerun()

col32_img, col32_btn = st.columns([1, 6])
with col32_img:
    cargar_imagen_segura("seguridad_2.png", "🔸")
with col32_btn:
    label_ss2 = "🟢 N/A" if st.session_state.seguridad_social_final == "N/A" else "⚪ N/A"
    if st.button(label_ss2, key="btn_ss2", use_container_width=True):
        st.session_state.seguridad_social_final = "N/A"
        st.rerun()

col33_img, col33_btn = st.columns([1, 6])
with col33_img:
    cargar_imagen_segura("seguridad_3.png", "❌")
with col33_btn:
    label_ss3 = "🟢 No" if st.session_state.seguridad_social_final == "No" else "⚪ No"
    if st.button(label_ss3, key="btn_ss3", use_container_width=True):
        st.session_state.seguridad_social_final = "No"
        st.rerun()

st.write("---")

# ==========================================
# 📊 CÁLCULOS MATEMÁTICOS DE PUNTUACIÓN Y REGLA DE 3
# ==========================================
# Suma Producto por pesos (1 a 7 multiplicado por 1, 8 a 11 multiplicado por 2)
puntos_obtenidos = (
    valores_edad[st.session_state.edad_final] * 1 +
    valores_civil[st.session_state.civil_final] * 1 +
    valores_familia[st.session_state.familia_final] * 1 +
    valores_educacion[st.session_state.educacion_final] * 1 +
    valores_empleo[st.session_state.empleo_final] * 1 +
    valores_vehiculo[st.session_state.vehiculo_final] * 1 +
    valores_seguro[st.session_state.seguro_final] * 1 +
    valores_material[st.session_state.material_final] * 2 +
    valores_tenencia[st.session_state.tenencia_final] * 2 +
    valores_enfermedad[st.session_state.enfermedad_final] * 2 +
    valores_seguridad[st.session_state.seguridad_social_final] * 2
)

# Regla de 3 directa sobre el máximo de 45 puntos
porcentaje_final = (puntos_obtenidos * 100.0) / 45.0

# Desplegar los resultados en pantalla en un contenedor visual estético
st.markdown("### 📈 Resultado del Análisis")
st.markdown(f"""
    <div class="resultado-box">
        <h4>Puntaje Acumulado: <b>{puntos_obtenidos} / 45 puntos</b></h4>
        <h2>Porcentaje Socio-económico: <b>{porcentaje_final:.2f}%</b></h2>
    </div>
""", unsafe_allow_html=True)

# Barra de progreso integrada de Streamlit (acepta valores de 0.0 a 1.0)
st.progress(porcentaje_final / 100.0)

st.write(" ")

# ==========================================
# BOTÓN DE DESCARGA (Incluye el porcentaje y los puntos en el reporte)
# ==========================================
datos_a_guardar = (
    f"=== RESUMEN DE RESPUESTAS ===\n"
    f"1. Edad: {st.session_state.edad_final}\n"
    f"2. Estado Civil: {st.session_state.civil_final}\n"
    f"3. Personas en familia: {st.session_state.familia_final}\n"
    f"4. Nivel educativo: {st.session_state.educacion_final}\n"
    f"5. Tipo de empleo: {st.session_state.empleo_final}\n"
    f"6. Tiene Vehículos: {st.session_state.vehiculo_final}\n"
    f"7. Tiene Seguro Privado: {st.session_state.seguro_final}\n"
    f"8. Materiales de la vivienda: {st.session_state.material_final}\n"
    f"9. Tenencia vivienda: {st.session_state.tenencia_final}\n"
    f"10. Existencia de Enfermedades: {st.session_state.enfermedad_final}\n"
    f"11. Seguridad Social: {st.session_state.seguridad_social_final}\n"
    f"-----------------------------------------\n"
    f"PUNTAJE TOTAL: {puntos_obtenidos} / 45\n"
    f"PORCENTAJE FINAL: {porcentaje_final:.2f}%\n"
    f"=========================================\n"
)

st.download_button(
    label="📥 Descargar reporte de porcentaje (.txt)",
    data=datos_a_guardar,
    file_name="reporte_socio_economico.txt",
    mime="text/plain"
)
