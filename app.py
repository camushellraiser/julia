import streamlit as st

# -------------------------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------------------------
st.set_page_config(
    page_title="Para Julia — Decisión de formación en repostería",
    layout="wide",
)

# -------------------------------------------------
# ESTILOS (FONDO NEGRO + TIPOGRAFÍA ELEGANTE)
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    background-color: #000000;
    color: #f2f2f2;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

.section {
    margin-top: 3rem;
    margin-bottom: 3rem;
}

.card {
    background: #0e0e0e;
    padding: 2rem;
    border-radius: 18px;
    box-shadow: 0 20px 40px rgba(0,0,0,.5);
    height: 100%;
}

.muted {
    color: #b3b3b3;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# PORTADA
# -------------------------------------------------
st.markdown("""
<div class="section">
<h1>Julia, hice esto pensando en ti</h1>
<p class="muted">
No para decirte qué elegir, sino para que puedas ver con calma, 
con criterio profesional y con todo el contexto, 
qué opción encaja mejor con el momento en el que estás como repostera.
</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1542826438-6f87c33cfd9e",
    use_container_width=True
)

# -------------------------------------------------
# CONTEXTO GENERAL
# -------------------------------------------------
st.markdown("""
<div class="section">
<h2>🎯 Punto de partida</h2>
<p>
Tú ya sabes de repostería. Tienes técnica, sensibilidad y experiencia.
Esto no va de “aprender desde cero”, sino de <strong>qué tipo de crecimiento quieres ahora</strong>:
más estructura, más exigencia, más proyección… o un formato más flexible y creativo.
</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# COMPARACIÓN GENERAL
# -------------------------------------------------
st.markdown("## ⚖️ Comparación clara de enfoque")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>GQB</h3>
    <ul>
        <li>Formación profesional estructurada</li>
        <li>Pastelería europea clásica y moderna</li>
        <li>Ritmo exigente y constante</li>
        <li>Trabajo individual en mesa propia</li>
        <li>Grupos muy reducidos</li>
        <li>Enfoque técnico y de alto nivel</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>CGI</h3>
    <ul>
        <li>Formato diplomado</li>
        <li>Mayor variedad de productos</li>
        <li>Ritmo más flexible</li>
        <li>Trabajo más compartido</li>
        <li>Enfoque creativo y emprendedor</li>
        <li>Menor presión técnica</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# PROGRAMA ACADÉMICO
# -------------------------------------------------
st.markdown("## 📚 Contenido y programa académico")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🎂 GQB — Pastelería internacional</h3>
    <p>
    Masas quebradas y sablé, hojaldrado clásico y avanzado, masas batidas,
    cremas clásicas (inglesa, mousseline, bavarois), mousses,
    entremets, chocolate profesional, bombonería,
    azúcar artístico, glaseados espejo, heladería
    y técnicas vanguardistas.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🍰 CGI — Diplomado en repostería</h3>
    <p>
    Galletería, tartas, cupcakes, brownies,
    panadería básica, pastelería europea por niveles,
    chocolatería, fondant,
    confitería mexicana, heladería
    y nociones de emprendimiento.
    </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# DURACIÓN Y HORARIOS
# -------------------------------------------------
st.markdown("## ⏱️ Duración y horarios")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>GQB</h3>
    <p>
    Modalidad intensiva<br>
    Duración aproximada: 7 meses<br>
    Lunes y miércoles<br>
    6:30 pm – 10:00 pm
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>CGI</h3>
    <p>
    Inicio: 22 de enero<br>
    Miércoles y jueves<br>
    4:00 pm – 8:00 pm<br>
    Posibles ajustes según grupo
    </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# DISTANCIA
# -------------------------------------------------
st.markdown("## 📍 Distancia y trayecto")

st.markdown("""
Ambas opciones implican prácticamente el mismo trayecto:
entre **25 y 30 minutos en automóvil**.
Aquí el punto no es la distancia,
sino cómo se siente llegar cansada a una clase exigente
versus una clase más flexible.
""")

st.image(
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    caption="Trayectos urbanos similares en ambos casos",
    use_container_width=True
)

# -------------------------------------------------
# COSTOS
# -------------------------------------------------
st.markdown("## 💰 Inversión aproximada")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>GQB</h3>
    <p>
    Inscripción + mensualidades<br>
    Uniforme y equipo personal<br>
    Inversión más alta, pero más estructurada
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>CGI</h3>
    <p>
    $25,000 MXN<br>
    Inscripción, uniforme y seguro adicionales<br>
    Incluye insumos y préstamo de utensilios
    </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# CERTIFICACIÓN
# -------------------------------------------------
st.markdown("## 🎓 Certificación y proyección")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>GQB</h3>
    <p>
    Carrera profesional en pastelería<br>
    Reconocimiento académico formal<br>
    Proyección más clara a cocina profesional
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>CGI</h3>
    <p>
    Constancia de diplomado<br>
    Enfoque práctico<br>
    Ideal para consolidar emprendimiento
    </p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# CIERRE
# -------------------------------------------------
st.markdown("""
<div class="section">
<h2>🖤 Para cerrar</h2>
<p>
No hay una opción correcta o incorrecta.
Solo dos caminos distintos.
Lo importante es que elijas el que
<strong>te haga sentir retada, cómoda y emocionada</strong>
al mismo tiempo.
</p>
<p class="muted">
Esto no es una decisión impuesta.
Es una invitación a que elijas lo que mejor hable de ti hoy.
</p>
</div>
""", unsafe_allow_html=True)
