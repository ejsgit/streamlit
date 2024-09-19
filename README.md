# Streamlit

Publish quickly WEB apps concerning data review and alalysis, dashboard and instruments UI
(Localhost, online through streamlit website and link, remotly on a VPS via docker depo and/or gitHub repo)

Multi pages app, navigation
Map capabilities, zoom etc.
Play audio files, generate sound
Plot graph with zoom (plotly)
Load files, upload file
Take photo
Add cursors, buttons, images, select field, leftsid
Titles, markdown (translate to html)
Latex
State machine

If necessary try with "sudo"

Clone repo
git clone https://github.com/ejsgit/streamlit.git

Create venv, active and install requirement.txt
python -m venv .venv etc.
.venv/ /activate or source / /activate

do : pip install -r requirements.txt (maybo cut this file in several ones)
LIB installed : streamlit, numpy, matplotlib.pyplot, plotly, graphviz, pandas, StringIO, 
scipy.io.wavfile

streamlit run ./app/exemple.py
or 
streamlit run .\app\exemple.py