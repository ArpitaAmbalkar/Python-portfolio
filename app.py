import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def image_to_base64(image):
    buffer = BytesIO()
    image.save(buffer, format="WEBP")
    img_str = base64.b64encode(buffer.getvalue()).decode()
    return img_str

st.set_page_config(page_title="Arpita's Portfolio", page_icon=":sparkles:")

# ---- CSS for Circular Image ----
st.markdown("""
    <style>
    .circular-img {
        margin_top= 3 cm;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Profile Section with Columns ----
image = Image.open("my_image.webp")
col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(f'<img src="data:image/webp;base64,{image_to_base64(image)}" class="circular-img">', unsafe_allow_html=True)

with col2:
    st.title("Hi, I'm Arpita!")
    st.subheader("Python Developer | C++ Enthusiast | Problem Solver")
    st.write("""
    Welcome to my portfolio!  
    Here you can find my projects, resume, and contact info.
    """)

# ---- Skills ----
st.header("Skills")
st.write("- Python\n- C++\n- SQL\n- Data Structures\n- Git")

# ---- Projects ----
st.header("Projects")
st.write("1. Personal Expense Tracker - A CLI app to track and visualize your expenses.")
st.write("2. Resume Analyzer - Python-based tool to check resume quality.")
st.write("3. Early Depression Detection - ML model to detect signs of early depression using text input.")
st.write("4. Object Detection App - TensorFlow-based app to detect human activities like sitting or eating.")
st.write("5. Face Detection using Python - Detects and highlights faces in real-time using OpenCV.")
st.write("6. Farm Website - A responsive website for farmers and buyers. [Visit Website](https://sureshambalkar.netlify.app/location)")

# ---- Resume ----
st.header("Resume")
with open("Arpita_Resume.pdf", "rb") as file:
    st.download_button("Download Resume", file, file_name="Arpita_Resume.pdf")

# ---- Contact ----
st.header("Contact")
st.write("[GitHub](https://github.com/ArpitaAmbalkar)")
st.write("[LinkedIn](https://www.linkedin.com/in/arpita-ambalkar-47775b252?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
st.write("Email: arpitaambalkar26@gmail.com")

