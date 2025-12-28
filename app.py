import streamlit as st

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------
st.set_page_config(
    page_title="Informe Ejecutivo – Repostería",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# ESTILO EDITORIAL NEGRO
# -------------------------------------------------
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
    max-width: 1150px;
    margin: auto;
    padding: 5rem 2rem;
    border-top: 1px solid #1a1a1a;
}

.hero {
    padding-top: 6rem;
    padding-bottom: 6rem;
}

.hero h1 {
    font-size: 4.2rem;
    margin-bottom: 2rem;
}

.hero p {
    font-size: 1.25rem;
    line-height: 1.9;
    color: #d0d0d0;
    max-width: 900px;
}

p, li {
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
    border-radius: 28px;
    padding: 2.8rem;
}

.card h3 {
    margin-bottom: 1.6rem;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 3rem;
}

.table th, .table td {
    border-bottom: 1px solid #1f1f1f;
    padding: 1.2rem;
    vertical-align: top;
}

.table th {
    color: #cfa77a;
    font-size: 0.85rem;
    letter-spacing: 0.08em;
    text-align: left;
}

.quote {
    font-style: italic;
    font-size: 1.35rem;
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

# -------------------------------------------------
# PORTADA
# -------------------------------------------------
st.markdown("""
<div class="section hero">
  <div class="label">INFORME EJECUTIVO COMPARATIVO</div>
  <h1>Pensado para ti, Julia</h1>
  <p>
  Este documento no es una recomendación rápida ni una opinión.
  Es un análisis completo, construido con tiempo y criterio,
  para que puedas evaluar con calma qué opción encaja mejor
  con tu nivel, tu experiencia y el momento profesional en el que estás.
  </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# PERFIL
# -------------------------------------------------
st.markdown("""
<div class="section">
  <h2>Perfil considerado</h2>
  <p>
  Este análisis parte de un perfil con experiencia real en repostería.
  Alguien que ya domina bases, entiende procesos y busca algo más que repetir recetas:
  busca estructura, profundidad o un entorno alineado con su manera de trabajar.
  </p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# FILOSOFÍA
# -------------------------------------------------
st.markdown("""
<div class="section">
  <h2>Filosofía de cada escuela</h2>

  <div class="compare">
    <div class="card">
      <h3>GQB</h3>
      <p>
      Formación profesional con enfoque europeo.
      Prioriza técnica, estructura y exigencia constante.
      La práctica es individual y el ritmo es sostenido.
      </p>
    </div>

    <div class="card">
      <h3>CGI</h3>
      <p>
      Formación tipo diplomado.
      Ambiente más flexible y creativo,
      con énfasis en disfrutar el proceso y explorar variedad.
      </p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# PROGRAMA
# -------------------------------------------------
st.markdown("""
<div class="section">
  <h2>Contenido y programa académico</h2>

  <div class="compare">
    <div class="card">
      <h3>GQB – Pastelería internacional</h3>
      <p>
      Masas quebradas, hojaldre, masas batidas,
      cremas clásicas, mousses, entremets,
      chocolate profesional, bombonería,
      azúcar artístico, glaseados,
      heladería y técnicas vanguardistas.
      </p>
    </div>

    <div class="card">
      <h3>CGI – Diplomado</h3>
      <p>
      Galletería, tartas, cupcakes,
      panadería básica, brownies,
      pastelería europea por niveles,
      chocolatería, fondant,
      confitería mexicana y heladería.
      </p>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TABLA VARIABLES
# -------------------------------------------------
st.markdown("""
<div class="section">
  <h2>Comparación completa de variables</h2>

  <table class="table">
    <tr>
      <th>Variable</th>
      <th>GQB</th>
      <th>CGI</th>
    </tr>
    <tr>
      <td>Duración</td>
      <td>7 meses intensivos</td>
      <td>Diplomado de corta duración</td>
    </tr>
    <tr>
      <td>Horarios</td>
      <td>Lunes y miércoles · 18:30–22:00</td>
      <td>Miércoles y jueves · 16:00–20:00</td>
    </tr>
    <tr>
      <td>Distancia</td>
      <td>≈ 26 minutos desde casa</td>
      <td>≈ 26 minutos desde casa</td>
    </tr>
    <tr>
      <td>Tipo de práctica</td>
      <td>Individual, estación propia</td>
      <td>Práctica compartida</td>
    </tr>
    <tr>
      <td>Grupos</td>
      <td>Máximo 10 alumnos</td>
      <td>8–15 alumnos</td>
    </tr>
    <tr>
      <td>Equipo y uniforme</td>
      <td>Filipina, mandil, gorro, cuchillos, termómetro</td>
      <td>Incluye utensilios y uniforme</td>
    </tr>
    <tr>
      <td>Pagos</td>
      <td>Inscripción + mensualidades</td>
      <td>Pago único aproximado</td>
    </tr>
    <tr>
      <td>Certificación</td>
      <td>Constancia profesional avalada por WACS</td>
      <td>Constancia de diplomado</td>
    </tr>
  </table>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# CIERRE
# -------------------------------------------------
st.markdown("""
<div class="section">
  <h2>Lectura final</h2>
  <p class="quote">
  No se trata de cuál es mejor.
  Se trata de cuál se alinea más con la repostera que eres hoy
  y con la que quieres seguir construyendo.
  </p>
</div>

<div class="footer">
Documento elaborado con análisis, detalle y respeto por tu oficio.
</div>
""", unsafe_allow_html=True)
