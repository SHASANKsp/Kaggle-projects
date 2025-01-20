import streamlit as st
import requests

st.title("Plant Health Monitor")

# User input
feature1 = st.number_input("Soil Moisture", value=0.0)
feature2 = st.number_input("Nitrogen Level", value=0.0)


category_colors = {
    "Healthy": "green",
    "High Stress": "red",
    "Moderate Stress": "yellow"}

if st.button("Predict"):
    url = "http://localhost:8000/predict"
    data = {"Soil_Moisture": feature1, "Nitrogen_Level": feature2}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        color = category_colors.get(prediction, "white")
        st.markdown(
            f"""
            <div style="background-color:{color}; padding: 10px; border-radius: 5px; text-align: center;">
                <h3 style="color:black;">{prediction}</h3>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Error in API call")

