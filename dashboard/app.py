import streamlit as st
import pandas as pd
import numpy as np

st.title("⛰️ Rockfall AI Dashboard")

st.sidebar.header("Controls")
zone = st.sidebar.text_input("Zone ID", "Zone A")

risk = np.random.rand()  # placeholder risk

st.metric("Predicted Risk", f"{risk:.2f}")
st.line_chart(np.random.randn(20, 2), height=200)
