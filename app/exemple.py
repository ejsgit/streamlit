print("Hello, version 1 with Streamlit")

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

x = np.linspace(0, 2 * np.pi, 100)  # Generate 100 points between 0 and 2π
y = np.sin(x)# Create a simple plot
fig, ax = plt.subplots()
ax.plot(x,y)
#ax.plot([1, 2, 3], [4, 5, 6])
#plt.plot(x, y)
#plt.show()

# Display the plot in Streamlit
st.pyplot(fig)

# Optionally add some Streamlit interactivity or text
st.write("This is a simple plot rendered with Streamlit!")