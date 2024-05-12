import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Welcome")

with open("README.md", "r", encoding="utf-8") as readme_file:
    readme_text = readme_file.read()

st.markdown(readme_text, unsafe_allow_html=True)


#👋_Welcome.py