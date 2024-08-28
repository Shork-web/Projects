import streamlit as st
from PIL import Image

# Create columns to place the image and text side by side
col1, col2 = st.columns([1, 3])

# Load the image
image = Image.open("C:/Users/Suisei/me.jpg")

# Display the image in the first column, adjusting the width
with col1:
    st.image(image, caption="This is me", width=150)  # Adjust the width to make the image smaller

# Display the text in the second column
with col2:
    st.markdown("""
    ### About Me
    Hi, I'm **Iverson G. Merto**, a passionate 4th-year IT student. 
    With three years of experience in IT, my journey began in the beautiful province of Southern Leyte, where I discovered my love for computers.

    When I'm not coding or exploring new tech trends, you can find me:
    - Diving into captivating **manhwa** stories.
    - Enjoying the thrill of **motorcycle rides**.
    - Immersing myself in the world of **video games**.
    """)
    
# Portfolio Section with icons or visuals
st.header("Portfolio")
st.markdown("Here's a glimpse of some of the exciting projects I've worked on:")

# KeyXtractor
st.subheader("🚀 Project 1: KeyXtractor - AI-powered Keyword Extraction")
st.markdown("""
**Description:** This collaborative project aims to develop an AI tool that identifies and ranks keywords or sentences based on their significance. 
It's a powerful tool for content analysis and information retrieval.
""")

# Circle Detector
st.subheader("🔍 Project 2: Circle Detector - Applied AI Trial Run")
st.markdown("""
**Description:** This project involves creating an AI tool that uses cameras to detect and count objects with circular shapes. 
It's an excellent example of computer vision in action, demonstrating the potential of AI in real-world applications.
""")

# Contact Section with social media links
st.header("Get in Touch")
st.markdown("""
Feel free to reach out via:
- 📧 **Email:** [test@gmail.com](mailto:test@gmail.com)
- 🌐 **Facebook:** [Connect with me on Facebook](https://www.facebook.com/profile.php?id=61561851882675&mibextid=ZbWKwL)
""")
