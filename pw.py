import streamlit as st
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key="AIzaSyDbGOYOVsyr2NNyB6HRA9T_0f1hkTHWkWw")
model = genai.GenerativeModel('gemini-1.5-flash')

# Set the page configuration
st.set_page_config(
    page_title="Chanchal Alam's Portfolio",
    page_icon=":tada:",
    layout="centered",
)

# Hero Section
col1, col2 = st.columns(2)

with col1:
    st.title("Chanchal Alam")
    st.markdown("**Actively working in the Data Science Field**")
    st.write("Lovely Professional University, Jalandhar, Punjab, IN")
    st.write("I'm an aspiring Data Scientist and have been active on Kaggle for a year now. I'm a Kaggle Notebook Expert, ranking in the top 500 globally. With a strong foundation in programming languages like Python, Java, and R, I excel in machine learning models using TensorFlow and PyTorch. My expertise in NLP, Deep Learning, and Large Language Models enables me to derive meaningful insights from unstructured data. Additionally, I'm proficient in Computer Vision with OpenCV and Mediapipe, and I've successfully handled Big Data using PySpark.")
    st.write("[Email](mailto:chanchalalam24@gmail.com) | [LinkedIn](https://linkedin.com/in/chanchalalam786) | [GitHub](https://github.com/chanchalalam) | [Kaggle](https://www.kaggle.com/chanchal24)")

with col2:
    st.image("images/cv.jpg")

persona = """
You are Chanchal AI bot. You help people answer questions about yourself (i.e., Chanchal).
Answer as if you are responding. Don't answer in the second or third person.
If you don't know the answer, simply say "That's a secret".
Here is more info about Chanchal:
Hi, I'm an aspiring Data Scientist and have been active on Kaggle for a year now. I'm a Kaggle Notebook Expert, ranking in the top 500 globally.
With a strong foundation in programming languages like Python, Java, and R, I excel in machine learning models using TensorFlow and PyTorch. 
My expertise in NLP, Deep Learning, and Large Language Models enables me to derive meaningful insights from unstructured data.
Additionally, I'm proficient in Computer Vision with OpenCV and Mediapipe, and I've successfully handled Big Data using PySpark.
My proficiency in Database Management with MySQL and Data Analysis and Visualization with MS Excel and Tableau allows me to extract valuable insights from complex datasets. 
I've also leveraged RapidMiner and Informatica tools to streamline data workflows and drive business decisions. Currently, 
I'm working on MLOps, where I'm applying my skills to streamline the machine learning lifecycle, from model development to deployment and monitoring. 
I'm excited to explore the latest advancements in MLOps and contribute to the development of more efficient and effective AI solutions.
I thrive on leveraging these skills to drive meaningful impact and advance the field of data science and AI. With a passion for collaboration and innovation, 
I'm always looking for new opportunities to apply my expertise and make a difference. 

Chanchal's Email: chanchalalam24@gmail.com 
Chanchal's LinkedIn: https://www.linkedin.com/in/chanchalalam786/
Chanchal's GitHub: https://github.com/chanchalalam
Chanchal's Kaggle: https://www.kaggle.com/chanchal24
Chanchal's Leetcode: https://leetcode.com/u/chanchalalam24/
"""
st.title("Chanchal's AI Bot")
question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=True):
    with st.spinner("Thinking..."):
        prompt = "Here is the question that the user asked: " + question
        response = model.generate_content(persona + prompt)
        st.write(response.text)

st.write("")  # Add some spacing

# Skills Section
st.header("Skills")

skills = {
    "Python": 90,
    "Java": 85,
    "Machine Learning": 90,
    "NLP": 80,
    "Deep Learning": 90,
    "Computer Vision": 80,
    "Artificial Intelligence": 80,
}

for skill, proficiency in skills.items():
    st.slider(skill, 0, 100, proficiency)

# Education Section
st.header("Education")
st.subheader("Lovely Professional University, Phaghwara")
st.write("**B.Tech CSE with Specialization in Data Science (Artificial Intelligence & Machine Learning)**")

# Projects Section
st.header("Projects")
projects = [
    {
        "title": "Adavanced-Resume-Tracking-System",
        "date": "June 2024 - June 2024",
        "link": "https://github.com/chanchalalam/Adavanced-Resume-Tracking-System.git",
        "description": "This project aims to optimize the recruitment process. It integrates an advanced Applicant Tracking System with Google Gemini Pro, streamlining resume parsing, keyword matching, and candidate evaluation for an efficient end-to-end solution in talent acquisition."
    },
    {
        "title": "Math With Gesture",
        "date": "Jan 2024 - Jan 2024",
        "link": "https://github.com/chanchalalam/Math-With-Gesture.git",
        "description": "In this project, I created a system that can solve mathematical problems using hand gestures and computer vision techniques. By leveraging OpenCV and MediaPipe libraries, I developed a program that allows users to draw mathematical expressions on a surface, captures the gestures using a camera, and provides the solution with a step-by-step explanation."
    },
    {
        "title": "YouTube-Video-to-Detailed-Notes-Converter",
        "date": "Dec 2023 - Dec 2023",
        "link": "https://github.com/chanchalalam/YouTube-Video-to-Detailed-Notes-Converter.git",
        "description": "The YouTube Video to Detailed Notes Converter is an application that leverages the power of Generative AI, specifically the Gemini Pro model, to automatically generate detailed notes from YouTube video transcripts. This tool streamlines the process of extracting key insights from lengthy video content, making it an invaluable resource for students, researchers, and anyone seeking to efficiently consume video-based information."
    },
    {
        "title": "Multiple Disease Detection",
        "date": "Sep 2023 - June 2023",
        "link": "https://github.com/chanchalalam/Multiple-Disease-Detection.git",
        "description": "This project involves predicting multiple diseases such as Diabetes, Heart disease, Kidney disease, Breast cancer, Liver disease, Malaria, and Pneumonia using machine learning and deep learning algorithms. It includes a web application for predicting multiple diseases using these algorithms."
    }
]

for project in projects:
    st.subheader(project["title"])
    st.write(f"**{project['date']}**")
    st.write(project["description"])
    if "link" in project:
        st.write(f"[View Project]({project['link']})")
    if "links" in project:
        for link in project["links"]:
            st.write(f"[View Project]({link})")
    

# Social Media Links
st.header("Social Media")
st.write("""
- [LinkedIn](https://www.linkedin.com/in/chanchalalam786/)
- [GitHub](https://github.com/chanchalalam)
- [Kaggle](https://www.kaggle.com/chanchal24)
- [Leetcode](https://leetcode.com/u/chanchalalam24/)
""")
