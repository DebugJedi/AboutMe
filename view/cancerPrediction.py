import streamlit as st

com1, com2, com3 = st.columns([1,2,1], gap= 'small', vertical_alignment='center')

url = 'https://coldemail-5zdtzmmqe7nns6pgcekxuw.streamlit.app/'
with com1:
    st.markdown("")  
with com2:
    # st.markdown("[link](%s):material/link:"% url)   
    st.image("Assets/BreastCancer.jpg")
with com3:
    st.markdown("")

url = "https://cancerprediction-j4wt7j.streamlit.app/"

# com1, com2, com3 = st.columns([0.5,2,0.5], gap= 'small', vertical_alignment='center')
# with com1:
#     st.markdown("")  
# with com2:
#     # st.markdown("[link](%s):material/link:"% url)   
st.write("# [Cancer Prediction App](%s)🔗"% url)




intro = """
Breast cancer is one of the leading causes of cancer-related deaths among women globally. Detecting whether a breast mass is malignant (cancerous) or benign (non-cancerous) at an early stage is crucial for improving patient outcomes. Traditional diagnostic methods, such as mammograms and biopsies, while effective, often result in unnecessary procedures and emotional distress due to false positives and other diagnostic limitations. To address these challenges, machine learning models, particularly neural networks, have shown immense potential in aiding more accurate and timely predictions in medical diagnostics.

The **Cancer Prediction App** leverages the power of *deep learning* to assist in diagnosing breast masses based on patient data. By utilizing a neural network model trained on breast mass characteristics, this app predicts whether a mass is malignant or benign with high accuracy, providing valuable insights to both clinicians and patients. The app aims to streamline the diagnostic process, reduce unnecessary biopsies, and ultimately improve early detection rates.

Built using **PyTorch**, a popular deep learning framework, and integrated with an interactive Streamlit interface, this app enables users to upload breast mass data and receive real-time predictions. Whether you're a medical practitioner looking for diagnostic assistance or a researcher exploring machine learning in healthcare, this app is designed to make the process easy, efficient, and reliable.

"""

Features = """
### Core Features
- **Neural Network Model** for Prediction The app is powered by a robust neural network model developed using PyTorch. This model was trained on a comprehensive dataset of breast mass characteristics, including features such as mass size, shape, density, and more. The neural network analyzes these inputs to classify the mass as either malignant or benign, providing highly accurate predictions.

- **Real-Time Predictions** Currently the application make prediction based on the manual inputs which can be selected using the slider on the left. Model make predicition by loading the pre-trained neural network model. 

Interactive Visualization To further aid understanding, the app includes interactive data visualizations using Plotly. Users can explore key metrics like feature distributions and compare them with predicted outcomes, making the results more interpretable. The app provides visual insights into how different characteristics influence the model's predictions.
"""

conclusion = """
The App represents the intersection of machine learning and healthcare, providing an innovative and user-friendly solution for breast mass diagnosis. By leveraging a neural network trained on real-world data, the app aims to improve diagnostic accuracy and aid in early detection, ultimately helping to save lives. With its easy-to-use interface, real-time predictions, and powerful visualizations, the app offers a modern tool that can benefit both healthcare professionals and researchers alike. Whether used in clinical settings or for academic research, this app demonstrates the potential of artificial intelligence in transforming breast cancer diagnostics.
"""

st.markdown(intro)

st.divider()

st.markdown(Features)

st.divider()

st.markdown(conclusion)