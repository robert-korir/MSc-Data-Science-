import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

# Load your trained model
model = load_model('lstm_model.h5')

# Function to make predictions (modify according to your model's input requirements)
def make_prediction(input_data):
    # Ensure input_data is correctly preprocessed for your model
    # This may include scaling, reshaping, etc.
    prediction = model.predict(input_data)
    return prediction

# Streamlit interface
st.title('LSTM Model Deployment for Monthly Revenue Prediction')

# Creating user input fields for three monthly amounts
month1_amount = st.number_input('Enter amount for Month 1:', step=1.0, format="%.2f")
month2_amount = st.number_input('Enter amount for Month 2:', step=1.0, format="%.2f")
month3_amount = st.number_input('Enter amount for Month 3:', step=1.0, format="%.2f")

# When 'Predict' button is clicked, make a prediction and display it
if st.button('Predict'):
    # Convert input data to the correct format for your model
    # Adjust this part based on how your model expects the input data
    input_data = np.array([month1_amount, month2_amount, month3_amount]).reshape(1, 3, 1)  # Example reshaping

    # Make prediction
    prediction = make_prediction(input_data)
    
    # Display the prediction
    st.write(f'Prediction for next month: {prediction[0][0]}')

# To run, use: streamlit run your_script_name.py
