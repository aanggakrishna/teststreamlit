import streamlit as st
import pandas as pd

st.write("Hellow World")
"Ini tanpa write"

df = pd.read_csv("store.csv")

st.table(df)
