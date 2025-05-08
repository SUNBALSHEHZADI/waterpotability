import streamlit as st
import pandas as pd
import numpy as np
import joblib  


model = joblib.load('water_potability_model.pkl') 


st.title('Water Potability Prediction')
st.write('Enter the values below to predict if the water is potable or not.')

#User input 
ph = st.number_input('pH Value', min_value=0.0, max_value=14.0, value=7.0, step=0.1) 

hardness = st.number_input('Hardness', min_value=0, max_value=1000, value=150)

solids = st.number_input('Solids', min_value=0, max_value=1000, value=200)

chloramines = st.number_input('Chloramines', min_value=0, max_value=10, value=1)

sulfate = st.number_input('Sulfate', min_value=0, max_value=1000, value=150)

conductivity = st.number_input('Conductivity', min_value=0, max_value=1000, value=300)

organic_carbon = st.number_input('Organic Carbon', min_value=0, max_value=1000, value=100)

trihalomethanes = st.number_input('Trihalomethanes', min_value=0, max_value=1000, value=50)

turbidity = st.number_input('Turbidity', min_value=0, max_value=1000, value=10)

# dataFrame from the user input
input_data = pd.DataFrame({
    'ph': [ph],
    'Hardness': [hardness],
    'Solids': [solids],
    'Chloramines': [chloramines],
    'Sulfate': [sulfate],
    'Conductivity': [conductivity],
    'Organic_carbon': [organic_carbon],
    'Trihalomethanes': [trihalomethanes],
    'Turbidity': [turbidity]
})

# make prediction button
if st.button('Predict Potability'):
   
    prediction = model.predict(input_data)
    potability = 'Potable' if prediction == 1 else 'Not Potable'
    
    #result
    st.write(f"The water is: {potability}")
