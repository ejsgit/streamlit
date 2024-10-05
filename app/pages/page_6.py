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
    label="ADD OVERFLW PROTECTION : n_init",
    min_value=1,
    value=137,# 837799
    max_value=837799
)

n=1
step = np.arange(0,1000,1)
collatz = np.abs(step, dtype=np.int64)
#collatz = np.abs(step)
#collatz = np.arange(0,1000,1)

#fig = px.line(x=time, y=amplitude)

def collatzRun():
    global n_init
    #collatz=np.zeros_like(step)
    #collatz = 0*np.abs(step) # improve this reset 
    collatz[:]=0
    if n_init > 837799:
        n_init = 837799
    collatz[0] = n_init
    n=1
    fourOneLoop = 0
    colMax=0
    while (n < 1000) and (fourOneLoop < 1):
        if (collatz[n-1] > colMax):
            colMax=collatz[n-1]
        if (collatz[n-1] % 2 == 0): # even
            collatz[n] = collatz[n-1] // 2
        else:
            collatz[n] = 3 * collatz[n-1] + 1
            #collatz[n] = 7 * collatz[n-1] + 1
        if (collatz[n] == 1):
            fourOneLoop=fourOneLoop+1
        print(collatz[n])
        n=n+1
    collaTitle="Collatz run for N initial = " + str(collatz[0]) + " , Max Value = " + str(colMax)
    fig = px.bar(y=collatz[0:n], x=step[0:n], text_auto='.0f',title=collaTitle)
    fig.update_traces(textangle=270)
    #fig.update_xaxes(rangeslider_visible=True, range=[0, n])
    #fig.update_traces(textposition='outside')
   
    #fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    #fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    #fig.show()

    st.plotly_chart(fig)
    print("n, fourOneLoop", n, fourOneLoop)
    #st.write("n=",n)

#if st.button("Collatz Start"):
#    collatzRun()
collatzRun()
#clickedPoint = preserveZoomPlotlyChart(fig, event='click')

