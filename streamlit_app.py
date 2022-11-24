import pandas as pd
import streamlit as st

st.write("""
# Test
## test test
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  #df = pd.read_excel(uploaded_file)
  #df = pd.DataFrame()
  st.write(df)
  st.write("""Success""")
