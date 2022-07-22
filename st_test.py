

import streamlit as st
import pandas as pd
import numpy as np

st.title("Title")
st.header("Header")
st.subheader("SubHeader")
st.markdown("# 큰글자")
st.markdown("## 중간글자")
st.markdown("### 작은글자")



now = 29
year = st.slider('년수', 1, 100)
age = now + year
st.write("{}년 후, {}세".format(year, age))
