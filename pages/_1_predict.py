# predict.py
import streamlit as st
import pickle
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model

st.markdown(
    "<h1 style='text-align: center;'>Prediction</h1>",
    unsafe_allow_html=True,
)

st.write(
    "Prediction in the context of machine learning refers to the process of estimating or forecasting future outcomes based on trained models and input data. "
    "These models learn patterns and relationships from historical data, allowing them to make informed predictions on new, unseen data. "
    "Predictive models are commonly used for various tasks such as disease diagnosis, stock price forecasting, and customer behavior analysis."
)


image_path = "Images/prediction.png"
st.image(image_path, use_column_width=True, output_format="JPEG")
st.write(
    "### Why Choose These Three Diseases?\n"
    "We have focused on predicting the likelihood of three major diseases—Diabetes, Lung Cancer, and Heart Disease—due to their significant impact on global health. These diseases were selected based on their high prevalence and frequency in populations worldwide. By addressing these health concerns, our application aims to contribute to early detection, proactive healthcare management, and ultimately, improved public health outcomes."
)

# Tabular Form for Disease Symptoms
symptoms_data = {
    "Disease": ["Diabetes", "Lung Cancer", "Heart Disease"],
    "Symptom 1": ["Frequent Urination", "Persistent Cough", "Chest Pain"],
    "Symptom 2": ["Increased Thirst", "Shortness of Breath", "Shortness of Breath"],
    "Symptom 3": ["Fatigue", "Chest Pain", "Fatigue"],
    "Symptom 4": ["Unexplained Weight Loss", "Wheezing", "Irregular Heartbeat"],
}

st.write(
    "### Disease Symptoms (Hint)\n"
    "Here are some common symptoms associated with each disease:"
)
st.table(symptoms_data)

st.write("### Select a Disease for Prediction:")
selected_disease = st.selectbox(
    "", ["Choose", "Diabetes", "Lung Cancer", "Heart Disease"]
)
if selected_disease == "Choose":
    pass
elif selected_disease == "Diabetes":
    st.markdown(
        "<h1 style='text-align: center;'>Diabetes Prediction</h1>",
        unsafe_allow_html=True,
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
                st.write("### Precautions:")
                st.write("1. Monitor blood sugar levels regularly.")
                st.write("2. Follow a balanced and healthy diet.")
                st.write("3. Engage in regular physical activity.")
                st.write(
                    "4. Consult with a healthcare professional for personalized advice."
                )
        else:
            st.warning("Please enter valid numeric values for all fields.")


elif selected_disease == "Heart Disease":
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

        fasting_blood_sugar = st.selectbox(
            "Fasting Blood Sugar", options=["False", "True"]
        )
        rest_ecg = st.selectbox(
            "Resting Electrocardiographic Results", options=[0, 1, 2]
        )

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
        num_major_vessels = st.selectbox(
            "Number of Major Vessels", options=[0, 1, 2, 3]
        )
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
            if heart_diagnosis[0] == 1:
                st.write("### Precautions:")
                st.write(
                    "1. Adopt a heart-healthy diet, low in saturated fats and cholesterol."
                )
                st.write("2. Engage in regular aerobic exercise.")
                st.write("3. Manage stress through relaxation techniques.")
                st.write(
                    "4. Take medications as prescribed by a healthcare professional."
                )

        else:
            st.warning("Please enter valid numeric values for all fields.")


elif selected_disease == "Lung Cancer":

    # Load the trained model
    loaded_model = load_model("Models/lung_cancer_model.h5")

    # Function to preprocess the user-uploaded image
    def preprocess_image(image):
        # Resize the image to match the input size used during training
        img_size = (256, 256)
        img = cv2.resize(image, img_size)
        img = img.reshape((1,) + img.shape + (1,))
        return img

    st.markdown(
        "<h1 style='text-align: center;'>Lung Cancer Detection</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Welcome to our Lung Cancer Detection tool! To get started, please upload a clear and high-resolution image of your chest CT scan. Our advanced model will analyze the image and provide you with insights on potential lung conditions. "
        "The Lung Cancer Detection algorithm is designed using Convolutional Neural Networks (CNNs), a robust approach for image recognition. The process involves preprocessing the CT scan images by resizing and applying Gaussian blur to enhance image quality and reduce noise."
    )

    image_path = "Images/lung.png"
    st.image(image_path, output_format="JPEG", use_column_width=True)

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Upload you chest CT Scan Image:", type="jpg")

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
        col1, col2, col3 = st.columns([1, 2, 2])
        with col2:
            st.image(
                image,
                caption="Image Uploaded Successfullly",
                use_column_width=False,
                width=400,
            )

        # Preprocess the image
        processed_image = preprocess_image(np.array(image))

        # Make prediction
        prediction = loaded_model.predict(processed_image)

        st.write("### Prediction Result:")
        heart_message_style = (
            "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
            "background-color: #FFD2D2; color: #FF0000; text-align: center;"
        )

        no_heart_message_style = (
            "font-size: 20px; font-weight: bold; padding: 10px; border-radius: 5px; "
            "background-color: #C2E0FF; color: #0000FF; text-align: center;"
        )

        if np.argmax(prediction) == 1:
            st.markdown(
                "<div style='{}'>No lung Cancer Detected.</div>".format(
                    heart_message_style
                ),
                unsafe_allow_html=True,
            )
        elif np.argmax(prediction) == 0:
            st.markdown(
                "<div style='{}'>Lung Cancer Detected.</div>".format(
                    heart_message_style
                ),
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<div style='{}'>It is the average case might be present or might not be..!</div>".format(
                    heart_message_style
                ),
                unsafe_allow_html=True,
            )
