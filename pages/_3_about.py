import streamlit as st

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
    "<h1 style='text-align: center;'>About Us</h1>",
    unsafe_allow_html=True,
)
st.write(
    "Welcome to our project! We are a team of dedicated students from the Department of Technology, Shivaji University, committed to leveraging technology to solve real-world problems."
)
st.write(
    "Our mission is to develop innovative solutions that positively impact society and contribute to a better future. Through our project, we aim to showcase our skills and expertise in data science, machine learning, and software engineering in the medical field."
)

st.markdown(
    "<h4 style='text-align: center;'>Institute Information</h4>",
    unsafe_allow_html=True,
)
st.write(
    "We are proud to be part of the Department of Technology at Shivaji University, a renowned institution known for its academic excellence and cutting-edge research. Our college provides a nurturing environment for students to explore their interests, develop their skills, and prepare for successful careers in the technology industry."
)

st.markdown(
    "<h4 style='text-align: center;'>Our Team</h4>",
    unsafe_allow_html=True,
)
st.write(
    "Our team comprises highly motivated and talented individuals who bring diverse backgrounds and expertise to the table. We believe in collaboration, innovation, and continuous learning. Each member contributes their unique skills and perspectives, fostering an environment of growth and knowledge-sharing."
)
project_guide_image_path = "Images/AboutSection/AAM.png"
col1, col2, col3 = st.columns([1.5, 2, 1])
with col2:
    st.image(
        project_guide_image_path,
        caption="Project Guide: Mrs. Amrita Manjrekar [Assistant Professor]",
        use_column_width=False,
        width=220,
    )
team_member_images = [
    "Images/AboutSection/tejas.png",
    "Images/AboutSection/aditya.png",
    "Images/AboutSection/vasudha.png",
    "Images/AboutSection/vaishnavi.png",
]
row1, row2, row3, row4 = st.columns(4)
row1.image(
    team_member_images[0],
    caption="Tejas Shingan [Computer Science Student]",
    use_column_width=True,
)
row2.image(
    team_member_images[1],
    caption="Aditya Nimbarkar [Computer Science Student]",
    use_column_width=True,
)
row3.image(
    team_member_images[2],
    caption="Vasudha Dake [Computer Science Student]",
    use_column_width=True,
)
row4.image(
    team_member_images[3],
    caption="Vaishnavi Kamble [Computer Science Student]",
    use_column_width=True,
)


st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"> ',
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #f4f4f4; border-top: 1px solid #ddd;">
        <p style="font-size: 14px; color: #555;">Connect for More:</p>
        <a href="https://github.com/tejas-shingan" style="margin-right: 20px; color: #007BFF; text-decoration: none;" target="_blank"><i class="fab fa-github"></i> GitHub</a>
        <a href="https://in.linkedin.com/in/tsshingan" style="margin-right: 20px; color: #007BFF; text-decoration: none;" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
        <a href="https://www.kaggle.com/tejassureshshingan" style="margin-right: 20px; color: #007BFF; text-decoration: none;" target="_blank"><i class="fab fa-kaggle"></i> Kaggle</a>
        <a href="mailto:acad@tejas.maskmy.id" style="margin-right: 20px; color: #007BFF; text-decoration: none;"><i class="fas fa-envelope"></i> Email</a>
        <br>
        <p style="font-size: 12px; margin-top: 10px; color: #777;">© 2024 Your Company Name. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
