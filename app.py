import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Load the saved model
loaded_model = load_model('best_milk_quality_model')

# Streamlit App Title
st.title('Milk Quality Prediction')

# Input fields for milk quality parameters
st.header('Enter Milk Quality Parameters:')

ph = st.number_input('pH', min_value=0.0, max_value=14.0, value=6.6)
temperature = st.number_input('Temperature', min_value=0, value=35)
taste = st.number_input('Taste (0 or 1)', min_value=0, max_value=1, value=1)
odor = st.number_input('Odor (0 or 1)', min_value=0, max_value=1, value=0)
fat = st.number_input('Fat (0 or 1)', min_value=0, max_value=1, value=1)
turbidity = st.number_input('Turbidity (0 or 1)', min_value=0, max_value=1, value=0)
colour = st.number_input('Colour', min_value=0, value=254)

# Create a dictionary with user input
user_input = {
    'pH': ph,
    'Temprature': temperature,
    'Taste': taste,
    'Odor': odor,
    'Fat ': fat,
    'Turbidity': turbidity,
    'Colour': colour
}

# Convert input to a pandas DataFrame
input_df = pd.DataFrame([user_input])

# Prediction button
if st.button('Predict Milk Quality'):
    # Make prediction
    predictions = predict_model(loaded_model, data=input_df)

    # Display the prediction result
    predicted_grade = predictions['prediction_label'].iloc[0]

    # Assuming 0: High, 1: Low, 2: Medium based on previous LabelEncoding
    grade_mapping = {0: 'High', 1: 'Low', 2: 'Medium'}
    predicted_grade_label = grade_mapping.get(predicted_grade, 'Unknown')

    st.success(f'The predicted Milk Quality Grade is: {predicted_grade_label}')