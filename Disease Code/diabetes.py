# diabetes.py

import streamlit as st
import pickle

st.markdown(
    "<h1 style='text-align: center;'>Diabetes Prediction</h1>", unsafe_allow_html=True
)

st.write(
    "In this section, you can input relevant parameters for diabetes prediction. "
    "These parameters include information such as the number of pregnancies, glucose level, blood pressure, "
    "skin thickness, insulin level, BMI (Body Mass Index), diabetes pedigree function, and age of the person. "
    "Please enter the values within the specified ranges for accurate predictions. "
    "Once you've entered the necessary information, click the 'Predict' button to get insights based on our machine learning model."
)


image_path = "Images/diabetes.png"
col1, col2, col3 = st.columns([0.1, 2, 2])
with col2:
    st.image(
        image_path,
        width=650,
        output_format="JPEG",
    )

st.write("### Input Parameters:")
numeric_fields = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
]

col1, col2 = st.columns(2)
with col1:
    pregnancies = st.text_input("Pregnancies (0-17)")
    try:
        pregnancies = int(pregnancies)
        if not 0 <= pregnancies <= 17:
            raise ValueError("Value must be between 0 and 17.")
    except (ValueError, TypeError):
        if pregnancies != "":
            st.warning("Please enter a valid integer between 0 and 17.")

    glucose = st.text_input("Glucose Level (70-199 mg/dL)")
    try:
        glucose = float(glucose)
        if not 70 <= glucose <= 199:
            raise ValueError("Value must be between 70 and 199.")
    except (ValueError, TypeError):
        if glucose != "":
            st.warning("Please enter a valid number between 70 and 199.")

    blood_pressure = st.text_input("Blood Pressure value (60-200 Hg)")
    try:
        blood_pressure = float(blood_pressure)
        if not 60 <= blood_pressure <= 200:
            raise ValueError("Value must be between 60 and 200.")
    except (ValueError, TypeError):
        if blood_pressure != "":
            st.warning("Please enter a valid number between 60 and 200.")

    skin_thickness = st.text_input("Skin Thickness value (0-90 mm)")
    try:
        skin_thickness = float(skin_thickness)
        if not 0 <= skin_thickness <= 90:
            raise ValueError("Value must be between 0 and 90.")
    except (ValueError, TypeError):
        if skin_thickness != "":
            st.warning("Please enter a valid number between 90 and 140.")

with col2:
    insulin = st.text_input("Insulin Level (0-1000 μU/mL)")
    try:
        insulin = float(insulin)
        if not 0 <= insulin <= 1000:
            raise ValueError("Value must be between 0 and 1000.")
    except (ValueError, TypeError):
        if insulin != "":
            st.warning("Please enter a valid number between 0 and 1000.")

    bmi = st.text_input("BMI value (18-50 kg/m2)")
    try:
        bmi = float(bmi)
        if not 18 <= bmi <= 50:
            raise ValueError("Value must be between 18 and 50.")
    except (ValueError, TypeError):
        if bmi != "":
            st.warning("Please enter a valid number between 18 and 50.")

    diabetes_pedigree_function = st.text_input(
        "Diabetes Pedigree Function value (0.0-2.0)"
    )
    try:
        diabetes_pedigree_function = float(diabetes_pedigree_function)
        if not 0.0 <= diabetes_pedigree_function <= 2.0:
            raise ValueError("Value must be between 0.0 and 2.0.")
    except (ValueError, TypeError):
        if diabetes_pedigree_function != "":
            st.warning("Please enter a valid number between 0.0 and 2.0.")

    age = st.text_input("Age of the Person (14-100 years)")
    try:
        age = int(age)
        if not 14 <= age <= 100:
            raise ValueError("Value must be between 14 and 100.")
    except (ValueError, TypeError):
        if age != "":
            st.warning("Please enter a valid integer between 14 and 100.")


# Prediction and Output
diab_diagnosis = ""
with open("Models/diabetes_model_k.pkl", "rb") as model_file:
    diabetes_model = pickle.load(model_file)
if st.button("Predict"):

    def is_numeric(field):
        try:
            float(field)
            return True
        except ValueError:
            return False

    numeric_fields = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        diabetes_pedigree_function,
        age,
    ]

    if all(is_numeric(field) for field in numeric_fields):
        diab_diagnosis = diabetes_model.predict([numeric_fields])
        st.write("## Prediction Result:", unsafe_allow_html=True)

        diabetes_message_style = (
            "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
            "background-color: #FFD2D2; color: #FF0000; text-align: center;"
        )

        no_diabetes_message_style = (
            "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
            "background-color: #C2E0FF; color: #0000FF; text-align: center;"
        )

        if diab_diagnosis[0] == 1:
            st.markdown(
                "<div style='{}'>The model predicts the presence of diabetes.</div>".format(
                    diabetes_message_style
                ),
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div style='{}'>The model predicts no diabetes.</div>".format(
                    no_diabetes_message_style
                ),
                unsafe_allow_html=True,
            )
        if diab_diagnosis[0] == 1:
            st.write("### Precautions for Diabetes:")
            st.write("1. Monitor blood sugar levels regularly.")
            st.write("2. Follow a balanced and healthy diet.")
            st.write("3. Engage in regular physical activity.")
            st.write(
                "4. Consult with a healthcare professional for personalized advice."
            )
    else:
        st.warning("Please enter valid numeric values for all fields.")
