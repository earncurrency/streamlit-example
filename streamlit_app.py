import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
import mitosheet

st.write("""
# Test
## test test
""")

mitosheet.sheet()

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.write(df)
#   #AgGrid(df)
