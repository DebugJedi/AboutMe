import streamlit as st

com1, com2, com3 = st.columns([1,2,1], gap= 'small', vertical_alignment='center')


with com1:
    st.markdown("")  
with com2:
    # st.markdown("[link](%s):material/link:"% url)   
    st.image("Assets/ComputerVision.jpg")
with com3:
    st.markdown("")

url = 'https://computervision-w7a5mhbcfnbui4.streamlit.app/'

# com1, com2, com3 = st.columns([0.5,2,0.5], gap= 'small', vertical_alignment='center')
# with com1:
#     st.markdown("")  
# with com2:
#     # st.markdown("[link](%s):material/link:"% url)   
st.write("# [Object Detection](%s)🔗"% url)




intro = """
I have developed a real-time object detection app using the YOLO 11 model, deployed on Streamlit. This project demonstrates how easily computer vision models can be trained and applied for practical uses, such as self-driving cars and surveillance. YOLO (You Only Look Once) is a state-of-the-art model designed for fast and accurate object detection. Version 11 of YOLO, as detailed in the Ultralytics documentation, offers enhanced performance and flexibility, making it ideal for real-time applications where speed and precision are critical. The app showcases the power of this model, enabling users to interact with live object detection capabilities.
With the current deployment the model is trained to detect some common hand gesture like, OK, ThumbsUp, ThumbsDown, FingersCross, and PeaceOut.
"""

# Features = """
# ### Core Features
# - **Neural Network Model** for Prediction The app is powered by a robust neural network model developed using PyTorch. This model was trained on a comprehensive dataset of breast mass characteristics, including features such as mass size, shape, density, and more. The neural network analyzes these inputs to classify the mass as either malignant or benign, providing highly accurate predictions.

# - **Real-Time Predictions** Currently the application make prediction based on the manual inputs which can be selected using the slider on the left. Model make predicition by loading the pre-trained neural network model. 

# Interactive Visualization To further aid understanding, the app includes interactive data visualizations using Plotly. Users can explore key metrics like feature distributions and compare them with predicted outcomes, making the results more interpretable. The app provides visual insights into how different characteristics influence the model's predictions.
# """

# conclusion = """
# The App represents the intersection of machine learning and healthcare, providing an innovative and user-friendly solution for breast mass diagnosis. By leveraging a neural network trained on real-world data, the app aims to improve diagnostic accuracy and aid in early detection, ultimately helping to save lives. With its easy-to-use interface, real-time predictions, and powerful visualizations, the app offers a modern tool that can benefit both healthcare professionals and researchers alike. Whether used in clinical settings or for academic research, this app demonstrates the potential of artificial intelligence in transforming breast cancer diagnostics.
# """

st.markdown(intro)

st.divider()
st.write("[Link](%s) to the app."% url)
# st.markdown(Features)

# st.divider()

# st.markdown(conclusion)