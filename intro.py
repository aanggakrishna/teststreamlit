import streamlit as st
import pandas as pd

st.write("Hellow World")
"Ini tanpa write"

url='https://drive.google.com/file/d/1BtDpRNj8ha4onbtlSUXMnGsWrt3idqT3/view?usp=sharing'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id
df = pd.read_csv(dwn_url)


st.table(df)
