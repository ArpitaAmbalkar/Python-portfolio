import streamlit as st

st.set_page_config(page_title="Arpita's Portfolio", page_icon=":sparkles:")

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
st.write("3. Early Depression Detection - ML model to detect signs of early depression using text input.")
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
