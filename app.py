import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline, CustomData


predict_pipeline = PredictPipeline()

st.title("Data2Conversion App")

st.write("""
### About this App:
The Data2Conversion App helps you predict the likelihood of customer conversions based on input metrics like age range, gender, interest level, ad impressions, clicks, and spending. 
This tool is designed for marketing teams and analysts to optimize their ad campaigns and improve ROI.
""")

min_age = st.number_input("Minimum Age", min_value=0, max_value=100, value=25)
max_age = st.number_input("Maximum Age", min_value=0, max_value=100, value=35)
gender = st.selectbox("Gender", ["Male", "Female"])
interest = st.slider("Interest Level", min_value=0, max_value=150, value=5)
Impressions = st.number_input("Impressions", min_value=0, value=1000)
Clicks = st.number_input("Clicks", min_value=0, value=50)
Spent = st.number_input("Amount Spent", min_value=0.0, value=20.0)

# Predict button
if st.button("Predict"):
    user_data = CustomData(
        min_age=int(min_age),
        max_age=int(max_age),
        gender=gender,
        interest=int(interest),
        Impressions=int(Impressions),
        Clicks=int(Clicks),
        Spent=float(Spent),
    )
    
    input_df = user_data.get_data_as_data_frame()
    prediction = predict_pipeline.predict(input_df)
    
    # Round off the prediction to 4 decimal places
    rounded_prediction = round(prediction[0], 4)
    
    st.success(f"Based on the analysis, we predict {rounded_prediction} customers will convert from this ad campaign.")
