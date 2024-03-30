# home.py
import streamlit as st


st.markdown(
    "<h1 style='text-align: center;'>Multiple Disease Detection</h1>",
    unsafe_allow_html=True,
)
st.write(
    "Welcome to the Multiple Disease Detection Project. This application employs machine learning models to predict three major diseases: Diabetes, Lung Cancer, and Heart Disease. By analyzing relevant data, it provides valuable insights into the likelihood of these health conditions, assisting in early detection and proactive healthcare management."
)
image_path = "Images/home.png"
col1, col2, col3 = st.columns([0.1, 2, 2])
with col2:
    st.image(
        image_path,
        width=650,
        output_format="JPEG",
    )
st.markdown("### The Role of Machine Learning in Healthcare:")
st.write(
    "1. **Early Disease Detection:** Machine Learning algorithms analyze medical data to identify patterns and markers, enabling early detection of diseases such as Diabetes, Lung Cancer, and Heart Disease."
    "\n2. **Predictive Analytics:** ML models forecast patient outcomes and disease progression, aiding healthcare professionals in making informed decisions for personalized treatment plans."
    "\n3. **Efficient Diagnostics:** Machine Learning enhances diagnostic accuracy by interpreting medical imaging, pathology, and diagnostic test results, reducing the chances of human error."
    "\n4. **Proactive Healthcare Management:** ML-driven insights empower proactive healthcare interventions, allowing for preventive measures and personalized patient care."
)
image_path = "Images/application.png"
st.image(image_path, use_column_width=True)
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"> ',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #f4f4f4; border-top: 1px solid #ddd;">
        <p style="font-size: 14px; color: #555;">Explore More:</p>
        <a href="https://github.com/tejasshingan" style="margin-right: 20px; color: #007BFF; text-decoration: none;" target="_blank"><i class="fab fa-github"></i> GitHub</a>
        <a href="https://in.linkedin.com/in/tsshingan" style="margin-right: 20px; color: #007BFF; text-decoration: none;" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
        <a href="https://www.kaggle.com/tejassureshshingan" style="color: #007BFF; text-decoration: none;" target="_blank"><i class="fab fa-kaggle"></i> Kaggle</a>
        <br>
        <p style="font-size: 12px; margin-top: 10px; color: #777;">© 2024 Your Company Name. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
