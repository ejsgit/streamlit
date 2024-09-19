import streamlit as st

# Csounddevice library should be the job. Pip worked but import don't
# There is a lot of predefine library in many language, and a lot of online tools, synthetizer etc.

st.markdown("# Image page 5 🎉")
st.sidebar.markdown("# Image page 5 🎉")

st.image("app/fond-ecran.jpg", caption="Bridge")

# Standing wave model from chatGPT
# Add exponential envelopp, random inharmonicity, overtones
# y(x,t)=2Asin(kx)cos(ωt)

# Model found with chatGPT
# Sound Piano Synthetizer
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Sample rate and time
sample_rate = 44100
duration = 2  # seconds
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Frequency of the note (A4 = 440 Hz)
f0 = 440.0

# Number of overtones and their relative amplitudes
num_overtones = 10
amplitudes = [1 / (n**2) for n in range(1, num_overtones + 1)]

# Envelope function (Attack, Hold, Release)
def envelope(t, attack=0.01, hold=1.5, release=0.49, amplitude=1.0):
    env = np.zeros_like(t)
    attack_samples = int(attack * sample_rate)
    hold_samples = int(hold * sample_rate)
    release_samples = int(release * sample_rate)
    
    # Attack phase
    env[:attack_samples] = np.linspace(0, amplitude, attack_samples)
    # Hold phase
    env[attack_samples:attack_samples + hold_samples] = amplitude
    # Release phase
    env[attack_samples + hold_samples:] = np.linspace(amplitude, 0, release_samples)
    return env

# Generate the sound with overtones
y = np.zeros_like(t)
for n, amplitude in enumerate(amplitudes, 1):
    y += amplitude * (0.5 * np.sin(2 * np.pi * n * f0 * t) + 0.25 * np.sin(2.01 * np.pi * n * f0 * t))

# Apply the envelope
y *= envelope(t)

# Normalize to the range [-1, 1]
y = y / np.max(np.abs(y))

# Export as a .wav file
#write('piano_note.wav', sample_rate, np.int16(y * 32767))

# Plot the waveform
#plt.plot(t[:000], y[:1000])  # Plot a small portion for clarity
#plt.xlabel('Time [s]')
#plt.ylabel('Amplitude')
#plt.title('Piano Sound Waveform')
#plt.show()

# Display the plot in Streamlit
fig, ax = plt.subplots()
#ax.plot(t,y)
ax.plot(t[:10000], y[:10000])  # Plot a small portion for clarity

st.pyplot(fig)


# Generate a 440 Hz sine wave
#t = np.linspace(0, seconds, seconds * sample_rate, False)
#note_la = np.sin(frequency_la * t * 2 * np.pi) + 0.7*np.sin(2.00012*frequency_la * t * 2 * np.pi) + 0.4*np.sin(3.00003*frequency_la * t * 2 * np.pi) + 0.2*np.sin(4.00007*frequency_la * t * 2 * np.pi) + 0.1*np.sin(5.00007*frequency_la * t * 2 * np.pi)

#st.audio(note_la, sample_rate=sample_rate)
st.audio(y, sample_rate=sample_rate)
