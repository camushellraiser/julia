import streamlit as st

st.set_page_config(page_title="Pensado para ti, Julia", page_icon="✨")

with open("pensado-para-julia.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=3000, scrolling=True)
