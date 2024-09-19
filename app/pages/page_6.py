import streamlit as st
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.markdown("# Graph Plot (Plotly) 6 🎉")
st.sidebar.markdown("# Graph Plot (Plotly) 6 🎉")

st.subheader("Plotly Line Chart")

time = np.arange(0, 100, 0.1)
amplitude = np.sin(time) + 0.5*np.sin(time*3.72345) + 0.83*np.sin(time*0.05)

n_init = st.number_input(
    label="n_init",
    min_value=1,
    value=837799
)

n=1
step = np.arange(0,1000,1)
collatz = np.abs(step)
#fig = px.line(x=time, y=amplitude)

if st.button("Collatz Start"):
    collatz = np.abs(step)
    collatz[0] = n_init
    n=1
    while n < 1000:
        if (collatz[n-1] % 2 == 0): # even
            collatz[n] = collatz[n-1] // 2
        else:
            collatz[n] = 3 * collatz[n-1] + 1
        n=n+1

    fig = px.bar(x=step, y=collatz)

fig.update_xaxes(rangeslider_visible=True, range=[0, 60])
                 
fig.show()

#clickedPoint = preserveZoomPlotlyChart(fig, event='click')

