import streamlit as st

st.markdown("# Map, Camera & Metric (Pandas) page 3 🎉")
st.sidebar.markdown("# Map, Camera & Metric (Pandas) page 3 🎉")

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)
st.map(df)

st.metric(label="Voltage", value="220V", delta="-3V")

cam_pict = st.camera_input("Take a Photo")
if cam_pict is None:
    st.markdown("Take a picture it will appear after that below")
else:
    st.image(cam_pict)

up_pict = st.file_uploader("Upload File")
