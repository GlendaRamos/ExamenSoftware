# Import python libraries
import streamlit as st
from PIL import Image

# Insert icon of web app
icon = Image.open("Engineer_of_petroleum.jpg")
# Page Layout
st.set_page_config(page_title="Petroleum App", page_icon=icon)

# CSS cod🛢 to improve the design of the web app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Tile of app
st.title("Ingeniería de Producción :link:")

st.write("---")

st.markdown(
    """La ingeniería del petróleo, ingeniería petrolífera, ingeniería de petróleos o 
    ingeniería petrolera es la parte de la ingeniería que combina métodos científicos y 
    prácticos orientados al desarrollo de técnicas para descubrir, explotar, 
    desarrollar, transportar, procesar y tratar los hidrocarburos desde su estado 
    natural, en el yacimiento, hasta los productos finales o derivados.
 - **Python Libraries:** streamlit, pandas, numpy, plotly, PIL
 """
)

# Fill in information about the project implemented in this app
expander_bar = st.expander("About")
expander_bar.write(
    "La ingeniería en petróleo es una ciencia para el desarrollo del potencial "
    "energetico que proviene del hidrocarburo."
)

# Insert image
image = Image.open("dd.jpg")
st.image(image, width=100, use_column_width=True)

# Sidebar
st.sidebar.title(":arrow_down_small: **Producción**")
uploaded_file = st.sidebar.file_uploader("Upload your csv file here")

st.sidebar.radio("pages", options=["Home", "Data", "Basic Calculations"])
