
import numpy as np
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components

step = np.arange(0,1000,1)
collatz = np.abs(step)

data_canada = px.data.gapminder().query("country == 'Canada'")
print(data_canada)
print("Test number 1, array init : ", collatz[0:10])
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
#fig.show()

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
print(df)