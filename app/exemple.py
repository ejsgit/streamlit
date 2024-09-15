print("Hello, version 2 with Streamlit and test func")

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Visualisation superposition de deux sinus de fréquences f1 et f2")
st.subheader("Auteur : Rico")
st.write("Voici une petit démo de ce qu'on peut faire avec les outils streamlit")

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

f1 = st.number_input(
    label="Fréquence f1",
    min_value=0,
    value=1
)

f2 = st.number_input(
    label="Fréquence f2",
    min_value = 0,
    value=20
)

r = st.slider(
    'f1/f2 amplitude ratio', 
    min_value=1,
    value=1)   # 👈 this is a widget

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

x = np.linspace(0, 2 * np.pi, 400)  # Generate 100 points between 0 and 2π
y = np.sin(f1*x) + (1/(r)) * np.sin(f2*x)  # Create a simple plot
fig, ax = plt.subplots()
ax.plot(x,y)
#ax.plot([1, 2, 3], [4, 5, 6])
#plt.plot(x, y)
#plt.show()

# Display the plot in Streamlit
st.pyplot(fig)

# Optionally add some Streamlit interactivity or text
st.write("This is a simple plot rendered with Streamlit!")

st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", autoplay=True)

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds

frequency_la = 440  # Our played note will be 440 Hz

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)

# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)
st.audio(note_la, sample_rate=sample_rate)

