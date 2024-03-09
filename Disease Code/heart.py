# Importing necessary libraries
import streamlit as st
import pickle
import numpy as np

st.markdown(
    "<h1 style='text-align: center;'>Heart Disease Prediction</h1>",
    unsafe_allow_html=True,
)


st.write(
    "In this section, you can input relevant parameters for heart disease prediction. "
    "These parameters include information such as age, sex, chest pain type, resting blood pressure, "
    "serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, "
    "exercise-induced angina, ST depression induced by exercise relative to rest, slope of the peak exercise ST segment, "
    "number of major vessels, and thalassemia test result."
    "Please enter the values within the specified ranges for accurate predictions. "
    "Once you've entered the necessary information, click the 'Predict' button to get insights based on our machine learning model."
)
image_path = "Images/Heart.png"
col1, col2, col3 = st.columns([0.3, 2, 2])
with col2:
    st.image(
        image_path,
        width=550,
        output_format="JPEG",
    )

st.write("### Input Parameters:")
col1, col2 = st.columns(2)
with col1:
    age = st.text_input("Age (17-100)")
    try:
        age = int(age)
        if not 17 <= age <= 100:
            raise ValueError("Value must be between 17 and 100.")
    except (ValueError, TypeError):
        if age != "":
            st.warning("Please enter a valid integer between 17 and 100.")

    sex = st.radio("Sex", options=["Female", "Male"])
    chest_pain_type = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3])
    resting_blood_pressure = st.text_input("Resting Blood Pressure (60-200)")
    try:
        resting_blood_pressure = float(resting_blood_pressure)
        if not 60 <= resting_blood_pressure <= 200:
            raise ValueError("Value must be between 60 and 200.")
    except (ValueError, TypeError):
        if resting_blood_pressure != "":
            st.warning("Please enter a valid number between 60 and 200.")

    serum_cholesterol = st.text_input("Serum Cholesterol (100-600)")
    try:
        serum_cholesterol = float(serum_cholesterol)
        if not 100 <= serum_cholesterol <= 600:
            raise ValueError("Value must be between 100 and 600.")
    except (ValueError, TypeError):
        if serum_cholesterol != "":
            st.warning("Please enter a valid number between 100 and 600.")

    fasting_blood_sugar = st.selectbox("Fasting Blood Sugar", options=["False", "True"])
    rest_ecg = st.selectbox("Resting Electrocardiographic Results", options=[0, 1, 2])

with col2:
    max_heart_rate_achieved = st.text_input("Maximum Heart Rate Achieved (50-250)")
    try:
        max_heart_rate_achieved = float(max_heart_rate_achieved)
        if not 50 <= max_heart_rate_achieved <= 250:
            raise ValueError("Value must be between 50 and 250.")
    except (ValueError, TypeError):
        if max_heart_rate_achieved != "":
            st.warning("Please enter a valid number between 50 and 250.")

    exercise_induced_angina = st.selectbox(
        "Exercise-Induced Angina", options=["No", "Yes"]
    )
    st_depression = st.text_input(
        "ST Depression Induced by Exercise Relative to Rest (0-7)"
    )
    try:
        st_depression = float(st_depression)
        if not 0 <= st_depression <= 7:
            raise ValueError("Value must be between 0 and 7.")
    except (ValueError, TypeError):
        if st_depression != "":
            st.warning("Please enter a valid number between 0 and 7.")

    slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2])
    num_major_vessels = st.selectbox("Number of Major Vessels", options=[0, 1, 2, 3])
    thalassemia_test_result = st.selectbox(
        "Thalassemia Test Result", options=[0, 1, 2, 3]
    )

# Prediction and Output
heart_diagnosis = ""
with open("Models/heart_rf_model.pkl", "rb") as model_file:
    heart_model = pickle.load(model_file)

if st.button("Predict"):
    sex = 0 if sex == "Female" else 1
    fasting_blood_sugar = 1 if fasting_blood_sugar == "True" else 0
    exercise_induced_angina = 1 if exercise_induced_angina == "Yes" else 0

    numeric_fields = [
        age,
        chest_pain_type,
        resting_blood_pressure,
        serum_cholesterol,
        rest_ecg,
        max_heart_rate_achieved,
        st_depression,
        slope,
        num_major_vessels,
        thalassemia_test_result,
    ]

    if all(isinstance(field, (int, float)) for field in numeric_fields):
        user_input = np.array(
            [
                age,
                sex,
                chest_pain_type,
                resting_blood_pressure,
                serum_cholesterol,
                fasting_blood_sugar,
                rest_ecg,
                max_heart_rate_achieved,
                exercise_induced_angina,
                st_depression,
                slope,
                num_major_vessels,
                thalassemia_test_result,
            ]
        ).reshape(1, -1)

        heart_diagnosis = heart_model.predict(user_input)

        st.write("### Prediction Result:")
        heart_message_style = (
            "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
            "background-color: #FFD2D2; color: #FF0000; text-align: center;"
        )

        no_heart_message_style = (
            "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
            "background-color: #C2E0FF; color: #0000FF; text-align: center;"
        )
        if heart_diagnosis[0] == 1:
            st.markdown(
                "<div style='{}'>The model predicts the presence of heart disease .</div>".format(
                    heart_message_style
                ),
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div style='{}'>The model predicts no heart disease.</div>".format(
                    no_heart_message_style
                ),
                unsafe_allow_html=True,
            )
    else:
        st.warning("Please enter valid numeric values for all fields.")
