import streamlit as st

# -----------------------
# CONFIGURACIÓN GENERAL
# -----------------------
st.set_page_config(
    page_title="Informe Ejecutivo – Formación en Repostería",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------
# ESTILOS OSCUROS PREMIUM
# -----------------------
st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #000000;
    color: #f2f2f2;
    font-family: 'Inter', sans-serif;
}

h1, h2, h3 {
    font-family: 'IBM Plex Serif', serif;
    color: #ffffff;
}

section {
    padding-top: 3rem;
    padding-bottom: 3rem;
    border-top: 1px solid #1a1a1a;
}

.block {
    background-color: #0e0e0e;
    border: 1px solid #1c1c1c;
    border-radius: 18px;
    padding: 2rem;
    margin-bottom: 2rem;
}

.label {
    color: #cfa77a;
    letter-spacing: 0.08em;
    font-size: 0.8rem;
    margin-bottom: 0.5rem;
}

.small {
    color: #b0b0b0;
    font-size: 0.95rem;
    line-height: 1.7;
}

.table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1.5rem;
}

.table th, .table td {
    border-bottom: 1px solid #1f1f1f;
    padding: 1rem;
    vertical-align: top;
}

.table th {
    color: #cfa77a;
    text-align: left;
    font-size: 0.85rem;
    letter-spacing: 0.06em;
}

.table td {
    color: #d8d8d8;
    font-size: 0.95rem;
}

.footer {
    margin-top: 5rem;
    color: #888;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# HERO
# -----------------------
st.markdown("<section>", unsafe_allow_html=True)
st.markdown("## Pensado para ti, Julia")
st.markdown("""
Este informe no es una recomendación rápida ni una opinión ligera.  
Es un **análisis completo**, construido con tiempo, criterio y respeto por el oficio,  
para que puedas ver **todas las variables reales** involucradas en esta decisión.
""")
st.markdown("</section>", unsafe_allow_html=True)

# -----------------------
# CONTEXTO
# -----------------------
st.markdown("<section>", unsafe_allow_html=True)
st.markdown("### Contexto de partida")
st.markdown("""
No estás empezando desde cero.  
Tienes técnica, experiencia y sensibilidad.  
Eso cambia completamente la pregunta:

> no se trata de *dónde aprender repostería*,  
> sino de **dónde vale la pena profundizar, exigirte y crecer**.
""")
st.markdown("</section>", unsafe_allow_html=True)

# -----------------------
# VARIABLES
# -----------------------
st.markdown("<section>", unsafe_allow_html=True)
st.markdown("### Variables consideradas")
st.markdown("""
Este análisis contempla únicamente factores que impactan tu experiencia real:

- nivel técnico del programa  
- profundidad y estructura académica  
- horarios y carga semanal  
- distancia y logística  
- forma de trabajo en clase  
- ambiente y exigencia  
- proyección profesional  

Trámites y papeleo quedaron fuera porque no definen la calidad formativa.
""")
st.markdown("</section>", unsafe_allow_html=True)

# -----------------------
# COMPARACIÓN TABLA
# -----------------------
st.markdown("<section>", unsafe_allow_html=True)
st.markdown("### Comparación estructurada")

st.markdown("""
<table class="table">
<tr>
<th>Variable</th>
<th>GQB – Carrera profesional</th>
<th>CGI – Diplomado</th>
</tr>

<tr>
<td>Duración</td>
<td>7 meses (modalidad intensiva)</td>
<td>Formato corto tipo diplomado</td>
</tr>

<tr>
<td>Carga semanal</td>
<td>7 h / semana, alta concentración</td>
<td>8 h / semana, ritmo más relajado</td>
</tr>

<tr>
<td>Horarios</td>
<td>Lunes y miércoles · 18:30–22:00</td>
<td>Miércoles y jueves · 16:00–20:00</td>
</tr>

<tr>
<td>Distancia</td>
<td>Aprox. 26 minutos</td>
<td>Aprox. 26 minutos</td>
</tr>

<tr>
<td>Tipo de práctica</td>
<td>Individual, estación propia</td>
<td>Compartida</td>
</tr>

<tr>
<td>Grupos</td>
<td>Máx. 10 alumnos</td>
<td>8–15 alumnos</td>
</tr>

<tr>
<td>Profundidad técnica</td>
<td>
Alta pastelería europea:  
chocolate profesional, azúcar, entremets, glaseados espejo
</td>
<td>
Programa amplio y creativo,  
menor profundidad técnica
</td>
</tr>

<tr>
<td>Exigencia</td>
<td>Alta, enfoque profesional</td>
<td>Media, enfoque flexible</td>
</tr>

<tr>
<td>Proyección</td>
<td>Pastelería formal, restaurantes, cocina profesional</td>
<td>Emprendimiento, eventos, desarrollo personal</td>
</tr>

<tr>
<td>Retorno para perfil con experiencia</td>
<td>Alto: reto y crecimiento real</td>
<td>Moderado: consolidación</td>
</tr>
</table>
""", unsafe_allow_html=True)

st.markdown("</section>", unsafe_allow_html=True)

# -----------------------
# LECTURA FINAL
# -----------------------
st.markdown("<section>", unsafe_allow_html=True)
st.markdown("### Lectura final")
st.markdown("""
No hay una opción “correcta” universal.  
Hay opciones que **encajan mejor según el momento y el objetivo**.

Una apuesta por estructura, profundidad y exigencia.  
La otra por comodidad, creatividad y disfrute.

Lo importante es que la decisión esté tomada con **información completa**,  
no con intuiciones incompletas.
""")
st.markdown("</section>", unsafe_allow_html=True)

# -----------------------
# CIERRE
# -----------------------
st.markdown("<section>", unsafe_allow_html=True)
st.markdown("""
> Lo único que importa para mí  
> es que elijas el camino que te haga sentir  
> retada cuando lo necesitas  
> y tranquila con el proceso.
""")
st.markdown("</section>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Documento elaborado con análisis, criterio técnico y respeto por el oficio.</div>", unsafe_allow_html=True)
