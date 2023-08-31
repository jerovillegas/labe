import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.header("LabE")

company_description = """Misión: Dinamizar el trabajo académico sobre 
productividad y competitividad con pertinencia económica y de política pública 
que aporten a las discusiones coyunturales y estructurales en el país.
"""
st.write(company_description)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Publicaciones recientes")

with col2:
    st.subheader("Noticias")


