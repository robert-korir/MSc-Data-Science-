import streamlit as st
import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# # Load your trained model
# # model = load_model('path_to_your_model.h5')from keras.models import load_model

# model = load_model('my_lstm_model.h5')

# # Initialize your scaler (assuming you saved it during training)
# # scaler = ...

# st.title('LSTM ModelDeployment')

# # Input fields for new data
# st.header('Input Data')
# # Example: Input for the features your model requires
# input_data = st.number_input('Enter some input for the model')

# # The predict button
# if st.button('Predict'):
    

#     # Display the prediction
#     st.write('Prediction:', prediction)

import streamlit as st

# Function to read HTML file
def load_html(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

# Load and display the HTML content
html_content = load_html('revenue-html.html')
st.markdown(html_content, unsafe_allow_html=True)

# Your Streamlit app logic continues here...
# For example, collecting input data
day_1 = st.number_input('Enter value for Day 1')
day_2 = st.number_input('Enter value for Day 2')
day_3 = st.number_input('Enter value for Day 3')

# Prediction button
if st.button('Predict'):
    # For debugging
    st.write('Predict button clicked')

    # Prediction logic here...
    pass

