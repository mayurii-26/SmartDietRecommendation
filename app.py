import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Smart Diet Recommendation",
    page_icon="🥗",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================

model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background-color: #f5f7f2;
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background: linear-gradient(to bottom,#eaf7d5,#f4ffe8);
    border-right: 2px solid #d6e9b8;
}

[data-testid="stSidebar"] *{
    color:#1c3b1c !important;
    font-size:17px;
}

/* TITLE */

.main-title{
    font-size:50px;
    font-weight:bold;
    color:#176b1f;
}

.sub-text{
    font-size:24px;
    color:#555;
}

/* INPUT LABELS */

label {
    color: black !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* NUMBER INPUT BOX */

.stNumberInput input {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
    font-size: 18px !important;
    border: 2px solid #cfe8c6 !important;
}

/* NUMBER INPUT PLACEHOLDER */

.stNumberInput input::placeholder {
    color: #555 !important;
}

/* SELECTBOX MAIN */

.stSelectbox div[data-baseweb="select"] {
    background: white !important;
    color: black !important;
    border-radius: 12px !important;
    border: 2px solid #cfe8c6 !important;
    font-size: 18px !important;
}

/* SELECTBOX INNER AREA */

.stSelectbox div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}

/* SELECTED TEXT */

.stSelectbox div[data-baseweb="select"] span {
    color: black !important;
    font-size: 18px !important;
}

/* DROPDOWN ICON */

.stSelectbox svg {
    fill: black !important;
}

/* SELECTBOX TEXT */

.stSelectbox div[data-baseweb="select"] span {
    color: black !important;
}

/* DROPDOWN MENU */

div[role="listbox"] {
    background-color: white !important;
    color: black !important;
    border-radius: 10px !important;
}

/* DROPDOWN OPTIONS */

div[role="option"] {
    background-color: white !important;
    color: black !important;
    font-size: 17px !important;
}

/* HOVER EFFECT */

div[role="option"]:hover {
    background-color: #dff5d8 !important;
    color: black !important;
}

/* BUTTON */

.stButton button{
    width:100%;
    background: linear-gradient(to right,#44c94d,#2f9e44);
    color:white;
    border:none;
    border-radius:15px;
    height:60px;
    font-size:24px;
    font-weight:bold;
}

/* RESULT BOX */

.result-box{
    background:#eef8e9;
    padding:30px;
    border-radius:20px;
    border:2px solid #b7e4a8;
}

/* BMI BOX */

.bmi-box{
    background:#e8f8e8;
    padding:20px;
    border-radius:15px;
    font-size:24px;
    font-weight:bold;
    color:#1b5e20;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("""
# 🥗 About Our Project

### 🍎 Smart Diet Recommendation System

This AI-powered application predicts the most suitable diet plan based on your health and lifestyle details.

---

## ⭐ Features

✔ Personalized Diet Plans  
✔ Smart BMI Calculation  
✔ AI-Based Prediction  
✔ Fast & Accurate Results  
✔ User-Friendly Interface

---

## 🎯 Our Mission

To encourage healthier lifestyles using Artificial Intelligence and smart nutrition recommendations.

---

💚 Eat Healthy, Stay Happy!
""")

# =========================
# HEADER IMAGE
# =========================

banner = Image.open("images/banner.png")
st.image(banner, use_container_width=True)


# =========================
# INPUT SECTION
# =========================

st.markdown("## 📝 Enter Your Health Details")

# ROW 1

col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input("👤 Age", 1, 100, 20)

with col2:
    gender = st.selectbox(
        "🚻 Gender",
        ["Male", "Female"]
    )

with col3:
    weight = st.number_input(
        "⚖ Weight (kg)",
        1,
        200,
        50
    )

with col4:
    height = st.number_input(
        "📏 Height (cm)",
        50,
        250,
        160
    )

# BMI Calculation

bmi = round(weight / ((height / 100) ** 2), 2)

st.markdown(f"""
<div class='bmi-box'>
🧮 Your Calculated BMI is: {bmi}
</div>
""", unsafe_allow_html=True)

st.write("")

# ROW 2

c1, c2, c3, c4 = st.columns(4)

with c1:
    disease = st.selectbox(
        "🩺 Disease Type",
        ["None", "Diabetes", "Hypertension", "Heart Disease"]
    )

with c2:
    severity = st.selectbox(
        "⚠ Severity",
        ["Low", "Medium", "High"]
    )

with c3:
    activity = st.selectbox(
        "🏃 Physical Activity",
        ["Low", "Medium", "High"]
    )

with c4:
    calories = st.number_input(
        "🔥 Daily Calories",
        500,
        5000,
        2000
    )

# ROW 3

d1, d2, d3, d4 = st.columns(4)

with d1:
    cholesterol = st.number_input(
        "❤️ Cholesterol",
        50,
        300,
        150
    )

with d2:
    blood_pressure = st.number_input(
        "🩸 Blood Pressure",
        50,
        200,
        120
    )

with d3:
    glucose = st.number_input(
        "💧 Glucose",
        50,
        300,
        100
    )

with d4:
    dietary = st.selectbox(
        "🥗 Dietary Restriction",
        ["None", "Vegetarian", "Vegan"]
    )

# ROW 4

e1, e2, e3, e4 = st.columns(4)

with e1:
    allergies = st.selectbox(
        "🤧 Allergies",
        ["None", "Nuts", "Dairy", "Gluten"]
    )

with e2:
    cuisine = st.selectbox(
        "🍜 Preferred Cuisine",
        ["Indian", "Italian", "Chinese", "Mexican"]
    )

with e3:
    exercise = st.slider(
        "🏋 Weekly Exercise Hours",
        0,
        30,
        5
    )

with e4:
    adherence = st.selectbox(
        "📋 Adherence to Diet Plan",
        ["Low", "Medium", "High"]
    )

# ROW 5

nutrient = st.selectbox(
    "🧪 Nutrient Deficiency",
    ["None", "Protein", "Iron", "Vitamin"]
)

# =========================
# PREDICTION
# =========================

if st.button("✨ Predict Diet Recommendation"):

    # Encoding mappings

    gender_map = {
        "Male": 1,
        "Female": 0
    }

    level_map = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    disease_map = {
        "None": 0,
        "Diabetes": 1,
        "Hypertension": 2,
        "Heart Disease": 3
    }

    dietary_map = {
        "None": 0,
        "Vegetarian": 1,
        "Vegan": 2
    }

    allergy_map = {
        "None": 0,
        "Nuts": 1,
        "Dairy": 2,
        "Gluten": 3
    }

    cuisine_map = {
        "Indian": 0,
        "Italian": 1,
        "Chinese": 2,
        "Mexican": 3
    }

    nutrient_map = {
        "None": 0,
        "Protein": 1,
        "Iron": 2,
        "Vitamin": 3
    }

    # Create input array with 18 features

    input_data = np.array([[
        age,
        gender_map[gender],
        weight,
        height,
        bmi,
        disease_map[disease],
        level_map[severity],
        level_map[activity],
        calories,
        cholesterol,
        blood_pressure,
        glucose,
        dietary_map[dietary],
        allergy_map[allergies],
        cuisine_map[cuisine],
        exercise,
        level_map[adherence],
        nutrient_map[nutrient]
    ]])

    # Scale data

    scaled_data = scaler.transform(input_data)

    # Predict

    prediction = model.predict(scaled_data)[0]

    # Diet labels

    diet_map = {
        0: "Balanced Diet",
        1: "Low Carb Diet",
        2: "High Protein Diet",
        3: "Low Fat Diet"
    }

    diet_result = diet_map.get(
        prediction,
        "Balanced Diet"
    )
        # Results Section

    st.write("")

    col1, col2 = st.columns([1,2])

    with col1:

        diet_img = Image.open("images/diet.png")
        st.image(diet_img, use_container_width=True)

    with col2:

        st.markdown(f"""
        <div class='result-box'>

        <h1 style='color:#14532d; font-size:42px;'>
        🥗 {diet_result}
        </h1>

        <h3 style='color:#333; font-size:26px;'>
        Personalized diet recommendation for your health profile 💚
        </h3>

        <br>

        <h3 style='color:#14532d;'>
        🌟 Benefits
        </h3>

        <div style='color:black; font-size:20px;'>

        ✔ Improves overall health<br>
        ✔ Maintains proper nutrition<br>
        ✔ Boosts energy and fitness<br>
        ✔ Supports healthy lifestyle

        </div>

        </div>
        """, unsafe_allow_html=True)

    # =========================
    # HEALTH TIPS SECTION
    # =========================

    st.write("")
    st.write("")

    st.markdown("""
    <div class='result-box'>

    <h2 style='color:#14532d;'>
    💡 Healthy Lifestyle Tips
    </h2>

    <h4 style='color:#333;'>

    🥗 Eat more fresh fruits and vegetables<br><br>

    💧 Drink at least 2-3 liters of water daily<br><br>

    🏃 Exercise regularly to stay fit and active<br><br>

    😴 Maintain proper sleep schedule for better health<br><br>

    🍔 Avoid excessive junk and processed food<br><br>

    ❤️ Small healthy habits create big positive changes

    </h4>

    </div>
    """, unsafe_allow_html=True)

# FOOTER

st.write("")
st.write("")

st.markdown("""
<center>
<h4 style='color:gray;'>
Made with ❤️ using Streamlit
</h4>
</center>
""", unsafe_allow_html=True)
