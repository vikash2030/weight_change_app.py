import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title("Weight Change Prediction App")

# Input form for user details
st.header("Enter your details")

# Collect user inputs
age = st.number_input("Age", min_value=1, max_value=120, value=25)
current_weight = st.number_input("Current Weight (kg)", min_value=30, max_value=200, value=70)
calories_consumed = st.number_input("Calories Consumed", min_value=0, value=2000)
activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"])

# Mapping activity level to numerical values
activity_mapping = {
    "Sedentary": 1,
    "Lightly Active": 2,
    "Moderately Active": 3,
    "Very Active": 4
}
activity_value = activity_mapping[activity_level]

# Create a DataFrame for the model input
input_data = pd.DataFrame({
    'Age': [age],
    'Caloric Intake per Weight': [current_weight],
    'BMR (Calories)': [calories_consumed],
    'Activity Weighted Calories': [activity_value]
})

# Button to predict
if st.button("Predict Weight Change"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Weight Change: {prediction[0]:.2f} kg")

    # Provide advice based on the prediction
    if prediction[0] > 0:
        st.info("You may gain weight. Consider monitoring your caloric intake.")
    elif prediction[0] < 0:
        st.info("You may lose weight. Ensure you're getting enough nutrition.")
    else:
        st.info("Your weight is likely to remain stable.")
