import streamlit as st
from forms.contact import contact_form

# st.title("About me")
@st.dialog("Contact Me")
def show_contact_form():
    # st.text_input("First Name")
    contact_form()
# Hero Section



col1, col2 = st.columns(2, gap= 'small', vertical_alignment='center')

with col1:
    st.image("./Assets/profilePic.png", width= 250)

with col2:
    st.title("DebugJedi", anchor= False)
    st.write(":red[A.K.A Priyank]")
    st.write(
        "Business Analyst with 5+ years of experience."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# Experience & Qualification
st.write("\n")
st.subheader("Experience", anchor= False)
st.write(
    """
    - 5+ years of experience of extracting actionable insights from data
    - Strong proficiency in Python and other analytical tools
    - Deep understanding of statistical principles and their applications
    - Demonstrated track record of delivering high-quality data-driven results
"""
)

# Skills
st.write("\n")
st.subheader("Hard skills", anchor= False)
st.write(
    """
    - Programming: Python (Sckit-learn, Pandas, NumPy, SciPy, TensorFlow, Keras, Statsmodels, NLTK), SQL
    - Data visulization: PowerBi, Tableau
    - Modeling: Linear Regression, Logistic Regression, Decision Trees, XGBoost
    - Databases: MySQL, SQLServer
"""
)