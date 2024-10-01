import streamlit as st

com1, com2 = st.columns([3,1], gap= 'small', vertical_alignment='center')


with com1:
    st.header("Email Hiring Manager")    
    
with com2:
    st.image("Assets/old_computer.jpg")


introduction = """

### Introduction to the Automated Job Application Email Generator
The app was created to help job seekers simplify the process of applying for jobs. Typically,\n writing personalized emails for each job application can be time-consuming and repetitive. This app removes that burden by allowing users to upload their resume or CV along with the job posting they are interested in, and in return, it generates a custom email that highlights their qualifications and interest in the job.

By leveraging advanced AI models and natural language processing (NLP), this app ensures that your email is polished, professional, and aligned with the job description. Whether you are applying to multiple roles or a single position, this tool helps you stand out with ease and confidence.
"""
how = """
## How It Works
### **1. Upload Your Resume or CV:**

- The app allows users to upload their resume or CV in pdf format. The app uses this document to extract key details such as your skills, qualifications, and professional experience.

### **2. Provide a Job Posting Link:**

- Users input a link to the job posting they want to apply to. The app will analyze the job description, extract critical information like job requirements, responsibilities, and preferred skills, and use this information to customize the email.

### **3. Email Generation:**

- Using the data extracted from your resume and the job posting, the app generates a well-written and professional email addressed to the hiring manager. The email emphasizes your qualifications and makes a compelling case for why you are a good fit for the role.
"""

keyfeatures = """
## Key Features
- **AI-Powered Resume and Job Posting Analysis:** The app is powered by the ***Llama-3.1-70b model*** , integrated through the ***ChatGroq API***, which uses advanced natural language processing to analyze both the job description and the resume for tailored content generation.

- **Streamlined Email Writing:** By combining the user’s resume information with the job posting details, the app automates the process of crafting a personalized email that highlights relevant experience and skills based on the job requirements.
"""

whats_behind = """
## Technologies Behind the App
- **ChatGroq and Llama-3.1-70b:** The app uses ***ChatGroq*** with the ***Llama-3.1-70b*** model to handle the complex language tasks involved in understanding resumes and job descriptions, ensuring the email is professionally crafted.

- **Document Loaders:** The app leverages ***PyPDFLoader*** and ***WebBaseLoader*** from ***LangChain Community*** to load resumes and job postings from PDFs and web-based content. This ensures accurate data extraction and analysis.

- **PromptTemplate & JsonOutputParser:** The app uses customizable prompts and outputs parsed in structured formats, ensuring flexibility in email generation and a clear review process for the user.

This app is ideal for job seekers looking to simplify their application process and ensure that every email they send is professional, relevant, and tailored to the job at hand. Try it today to accelerate your job search!

"""


st.markdown(introduction)


st.divider()

com1, com2 = st.columns([3,1], gap= 'small', vertical_alignment='center')


with com1:
    st.markdown(how)
    
with com2:
    st.image("Assets/HIW.jpg")


st.divider()

com1, com2 = st.columns([3,1], gap= 'small', vertical_alignment='center')


with com1:
    st.markdown(keyfeatures)
    
with com2:
    st.image("Assets/key.jpg")


st.divider()

st.markdown(whats_behind)

st.divider()
