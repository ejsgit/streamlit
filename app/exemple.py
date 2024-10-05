print("Hello, version 2 with Streamlit and test func")

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components

slider_html = """

<style>
input[type="range"] {
  writing-mode: vertical-lr;
}
</style>

<input type="range" id="volume" name="volume" min="0" max="100" />
<label for="volume">H2</label>

<script>
    const slider = document.getElementById("volume");
    slider.oninput = function() {
        const value = parseInt(slider.value);
        window.parent.postMessage({ value: value }, "*");
</script>
"""

components.html(slider_html, height=400)

# Capture the slider value
#value = st.session_state.get("slider_value", 50)
#st.write(f"Selected value: {value}")
if st.session_state.get("slider_value") is None:
    st.session_state.slider_value = 50  # Set initial value

# Capture the value sent from the slider
slider_value = st.session_state.slider_value
st.write(f"Selected value: {slider_value}")

value1 = st.slider("Select a value:", min_value=0, max_value=100, value=50, format="%d")
st.write(f"Selected value: {value1}")

st.title("Visualisation superposition de deux sinus de fréquences f1 et f2")

st.subheader("Auteur : RicoBrico")
st.write("Voici une petit démo de ce qu'on peut faire avec les outils streamlit")

st.markdown("# Graph Plot, audio, cursors (Numpy, Matplot) main page 🎈")
st.sidebar.markdown("# Graph Plot, audio, cursors (Numpy, Matplot) main page 🎈")

f1 = st.number_input(
    label="Fréquence f1",
    min_value=0,
    value=1
)
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
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

h1 = st.slider(
    'h1/f amplitude ratio', 
    min_value=0,
    value=50)   # 👈 this is a widget

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

x = np.linspace(0, 2 * np.pi, 400)  # Generate 100 points between 0 and 2π
y = np.sin(f1*x) + (1/(r)) * np.sin(f2*x)  # Create a simple plot

#ax.plot([1, 2, 3], [4, 5, 6])
#plt.plot(x, y)
#plt.show()

# Display the plot in Streamlit
fig, ax = plt.subplots()
ax.plot(x,y)
st.pyplot(fig)

# Optionally add some Streamlit interactivity or text
st.write("This is a simple plot rendered with Streamlit!")

st.audio("https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg", autoplay=False)

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds

frequency_la = 440  # Our played note will be 440 Hz

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)

# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi) + 0.7*np.sin(2.00012*frequency_la * t * 2 * np.pi) + 0.4*np.sin(3.00003*frequency_la * t * 2 * np.pi) + 0.2*np.sin(4.00007*frequency_la * t * 2 * np.pi) + 0.1*np.sin(5.00007*frequency_la * t * 2 * np.pi)
st.audio(note_la, sample_rate=sample_rate)

