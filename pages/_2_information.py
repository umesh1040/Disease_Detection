import streamlit as st
import pandas as pd
from PIL import Image

tile_style = """
<style>
    .tile {
        padding: 8px;
        border-radius: 20px;
        text-align: center;
        transition: transform 0.2s;
    }
    .tile:hover {
        transform: scale(1.05);
    }
</style>
"""
st.markdown(tile_style, unsafe_allow_html=True)
st.markdown(
    "<h1 style='text-align: center;'>Project Insights</h1>",
    unsafe_allow_html=True,
)

st.write(
    """
The topic of "Multiple Disease Detection using Machine Learning" is about using computer 
technology to help find illnesses in people early on. Sometimes, it's hard for people to see a doctor 
because they live far away or hospitals are too busy. Machine learning can look at lots of health 
information and pictures to find signs of diseases. This can be a big help, especially in places 
where it's hard to see a doctor quickly.

This page serves as a comprehensive health journal, focusing on the detection of diabetes using machine learning algorithms. 
Explore below for details on the algorithms employed, images related to diabetes, and the accuracy scores of the project.
"""
)

st.markdown(
    "<h3 style='text-align: center;'>Data Cards</h3>",
    unsafe_allow_html=True,
)

diabetes_df = pd.read_csv("Dataset/diabetes.csv")
heart_disease_df = pd.read_csv("Dataset/heart.csv")

selected_disease = st.selectbox(
    "Select a Disease",
    ["Choose", "Diabetes", "Heart Disease", "Lung Cancer"],
    help="Choose a disease to see more information.",
)

st.write("##### Input Parameters Information:")

if selected_disease == "Diabetes":
    st.write(
        """
    - **Pregnancies:** Number of times the patient has been pregnant.
    - **Glucose:** Plasma glucose concentration after 2 hours in an oral glucose tolerance test.
    - **Blood Pressure:** Diastolic blood pressure (mm Hg).
    - **Skin Thickness:** Thickness of the skin on the triceps (mm).
    - **Insulin:** 2-hour serum insulin (mu U/ml).
    - **BMI:** Body mass index, a measure of body fat based on height and weight.
    - **Diabetes Pedigree Function:** A function that scores the likelihood of diabetes based on family history.
    - **Age:** Age of the patient in years.
    """
    )

elif selected_disease == "Lung Cancer":
    st.write("Takes the input as the Image for prediction.")


elif selected_disease == "Heart Disease":
    st.write(
        """
    - **Age:** Age of the patient in years.
    - **Sex:** Gender of the patient (1 = male, 0 = female).
    - **Chest Pain Type:** Type of chest pain (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic).
    - **Resting Blood Pressure:** Resting blood pressure (mm Hg).
    - **Serum Cholesterol:** Serum cholesterol level in mg/dl.
    - **Fasting Blood Sugar:** Fasting blood sugar > 120 mg/dl (1 = true, 0 = false).
    - **Rest ECG:** Resting electrocardiographic results (0: normal, 1: having ST-T wave abnormality, 2: probable or definite left ventricular hypertrophy).
    - **Max Heart Rate Achieved:** Maximum heart rate achieved during exercise.
    - **Exercise Induced Angina:** Presence of exercise-induced angina (1 = yes, 0 = no).
    - **ST Depression:** ST depression induced by exercise relative to rest.
    - **Slope:** Slope of the peak exercise ST segment.
    - **Num Major Vessels:** Number of major vessels colored by fluoroscopy (0-3).
    - **Thalassemia Test Result:** Thalassemia test result (3 = normal; 6 = fixed defect; 7 = reversible defect).
    """
    )

st.write("##### Sample Data:")
if selected_disease == "Diabetes":
    st.table(diabetes_df.head())
elif selected_disease == "Heart Disease":
    st.table(heart_disease_df.head())
elif selected_disease == "Lung Cancer":
    col1, col2 = st.columns(2)
    col1.image(
        "Images\Lungs\Bengin case.jpg", use_column_width=True, caption="Bengin Case"
    )
    col2.image(
        "Images\Lungs\Malligent.jpg", use_column_width=True, caption="Malligent Case"
    )

st.markdown(
    "<h3 style='text-align: center;'>Accuracy Measures</h3>",
    unsafe_allow_html=True,
)

selected_disease = st.selectbox(
    "Select a Disease",
    ["Select", "Diabetes", "Heart Disease", "Lung Cancer"],
    help="Choose a disease to see more information.",
)

if selected_disease == "Select":
    pass

elif selected_disease == "Diabetes":
    accuracy_image_path = "Images/InformationSection/diabetes_accuracy.png"
    try:
        accuracy_image = Image.open(accuracy_image_path)
        st.image(
            accuracy_image,
            caption="Alogrithm Used: Support Vector Machine (SVM)",
            use_column_width=True,
        )
    except FileNotFoundError:
        st.warning("Accuracy score image not found for Diabetes.")

elif selected_disease == "Heart Disease":
    accuracy_image_path = "Images/InformationSection/heart disease_accuracy.png"
    try:
        accuracy_image = Image.open(accuracy_image_path)
        st.image(
            accuracy_image,
            caption="Alogrithm Used: Random Forest and Grid CV Search",
            use_column_width=True,
        )
    except FileNotFoundError:
        st.warning("Accuracy score image not found for Heart Disease.")


elif selected_disease == "Lung Cancer":
    accuracy_image_path = "Images/InformationSection/lung cancer_accuracy.png"
    try:
        accuracy_image = Image.open(accuracy_image_path)
        st.image(
            accuracy_image,
            caption="Alogrithm Used: Convolutional Neural Networks (CNN)",
            use_column_width=True,
        )
    except FileNotFoundError:
        st.warning("Accuracy score image not found for Lung Cancer.")
