import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open('SVC_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Streamlit page config
st.set_page_config(page_title="PCOS Risk Predictor", layout="centered")

# Custom styling
st.markdown("""
<style>
body, html, .stApp {
    font-family: 'Segoe UI', sans-serif;
    color: #5a2a41;
}
.stButton>button {
    background-color: #e91e63;
    color: white;
    font-weight: bold;
}
.stMarkdown h1, .stMarkdown h2 {
    color: #d81b60;
}
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("PCOS Risk Predictor 💫")

st.markdown("""
Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder affecting women of reproductive age.  
This tool provides an estimate of your PCOS risk based on health and lifestyle indicators.

**Note:** This is not a diagnosis. For medical advice, consult a certified healthcare professional.
""")

# Input form
with st.form("pcos_form"):
    col1, col2 = st.columns(2)

    with col1:
        skin_darkening = st.selectbox("Skin Darkening", ['Yes', 'No'])
        hair_growth = st.selectbox("Excess Hair Growth", ['Yes', 'No'])
        weight_gain = st.selectbox("Weight Gain", ['Yes', 'No'])
        cycle_type = st.selectbox("Cycle Type", ['Regular', 'Irregular'])
        fast_food = st.selectbox("Frequent Fast Food", ['Yes', 'No'])
        pimples = st.selectbox("Pimples", ['Yes', 'No'])

    with col2:
        hair_loss = st.selectbox("Hair Loss", ['Yes', 'No'])
        waist = st.number_input("Waist (in inches)", min_value=24.0, max_value=40.0, step=0.1)
        hip = st.number_input("Hip (in inches)", min_value=30.0, max_value=50.0, step=0.1)
        age = st.number_input("Age (in years)", min_value=11, max_value=50)
        period_duration = st.number_input("Period Duration (in days)", min_value=1, max_value=15)

    submitted = st.form_submit_button("Predict PCOS Risk")

# Prediction logic
if submitted:
    def to_binary(val): return 1 if val == 'Yes' or val == 'Irregular' else 0

    input_features = np.array([[
        to_binary(skin_darkening),
        to_binary(hair_growth),
        to_binary(weight_gain),
        to_binary(cycle_type),
        to_binary(fast_food),
        to_binary(pimples),
        to_binary(hair_loss),
        waist,
        hip,
        age,
        period_duration
    ]])

    scaled_input = scaler.transform(input_features)
    prediction = model.predict(scaled_input)[0]

    st.markdown("---")
    st.subheader("🔍 Prediction Result")

    if prediction == 0:
        st.error("⚠️ **Positive**: You may be at risk of PCOS. Please consult a gynecologist for further diagnosis.")
    else:
        st.success("✅ **Negative**: Low likelihood of PCOS based on the provided indicators.")

    st.markdown("""
    ---
    ⚠️ **Disclaimer:** This tool provides a statistical prediction based on past data.  
    It is **not a substitute for professional medical advice or diagnosis.**
    """)