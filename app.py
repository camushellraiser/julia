import streamlit as st

st.set_page_config(
    page_title="Formación en Repostería – Análisis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================
# ESTILO EDITORIAL
# =====================
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #000000;
    color: #f5f5f5;
}

body {
    font-family: 'Source Serif 4', serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #ffffff;
}

.section {
    max-width: 1100px;
    margin: auto;
    padding: 5rem 2rem;
    border-top: 1px solid #1a1a1a;
}

.hero {
    padding-top: 6rem;
    padding-bottom: 6rem;
}

.hero h1 {
    font-size: 4rem;
    margin-bottom: 2rem;
}

.hero p {
    font-size: 1.25rem;
    line-height: 1.9;
    color: #d0d0d0;
    max-width: 900px;
}

p {
    font-size: 1.05rem;
    line-height: 1.9;
    color: #cfcfcf;
}

.label {
    color: #cfa77a;
    letter-spacing: 0.15em;
    font-size: 0.75rem;
    margin-bottom: 1rem;
}

.compare {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    margin-top: 3rem;
}

.card {
    background: #0b0b0b;
    border: 1px solid #1c1c1c;
    border-radius: 24px;
    padding: 2.5rem;
}

.card h3 {
    margin-bottom: 1.5rem;
}

.quote {
    font-style: italic;
    font-size: 1.3rem;
    color: #e0e0e0;
    max-width: 900px;
}

.footer {
    text-align: center;
    color: #777;
    font-size: 0.85rem;
    padding-bottom: 4rem;
}
</style>

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Source+Serif+4:wght@300;400;600&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# =====================
# PORTADA
# =====================
st.markdown("""
<div class="section hero">
  <div class="label">INFORME COMPARATIVO</div>
  <h1>Pensado para ti, Julia</h1>
  <p>
  Esto no es una recomendación ni una comparación rápida.
  Es un análisis completo, hecho con tiempo y criterio,
  para que puedas ver con claridad qué ofrece realmente cada camino
  en el momento profesional en el que estás.
  </p>
</div>
""", unsafe_allow_html=True)

# =====================
# CONTEXTO
# =====================
st.markdown("""
<div class="section">
  <h2>Desde dónde parte este análisis</h2>
  <p>
  No estás empezando desde cero. Ya tienes técnica, intuición y experiencia.
  Por eso aquí no importa “aprender repostería”, sino decidir
  <strong>dónde vale la pena profundizar, exigirte y crecer</strong>.
  </p>
</div>
""", unsafe_allow_html=True)

# =====================
# COMPARACIÓN VIVENCIAL
# =====================
st.markdown("""
<div class="section">
  <h2>Cómo se vive estudiar en cada opción</h2>

  <div class="compare">
    <div class="card">
      <h3>GQB</h3>
      <p>
      Formación estructurada, exigente y técnica.
      Ritmo constante, trabajo individual y enfoque profesional.
      Cada clase se siente como un paso más hacia cocina real.
      </p>
    </div>

    <div class="card">
      <h3>CGI</h3>
      <p>
      Formación más flexible y cómoda.
      Ambiente creativo, ritmo más relajado y enfoque amplio.
      Ideal para disfrutar el proceso sin tanta presión técnica.
      </p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# =====================
# VARIABLES CLAVE
# =====================
st.markdown("""
<div class="section">
  <h2>Comparación clara de variables</h2>
  <p>
  Ambas opciones son válidas, pero responden a intenciones distintas.
  Aquí está lo que realmente cambia:
  </p>

  <div class="compare">
    <div class="card">
      <h3>GQB</h3>
      <p>
      • 7 meses intensivos<br>
      • Práctica individual<br>
      • Grupos muy reducidos<br>
      • Alta pastelería europea<br>
      • Exigencia constante<br>
      • Proyección profesional formal
      </p>
    </div>

    <div class="card">
      <h3>CGI</h3>
      <p>
      • Formato diplomado<br>
      • Práctica compartida<br>
      • Grupos más amplios<br>
      • Enfoque creativo<br>
      • Menor presión técnica<br>
      • Orientación a emprendimiento
      </p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# =====================
# CIERRE
# =====================
st.markdown("""
<div class="section">
  <h2>Lectura final</h2>
  <p class="quote">
  No hay una decisión correcta universal.
  Solo importa que el camino que elijas
  esté alineado con lo que quieres construir ahora.
  </p>
</div>

<div class="footer">
Documento elaborado con tiempo, análisis y respeto por tu oficio.
</div>
""", unsafe_allow_html=True)
