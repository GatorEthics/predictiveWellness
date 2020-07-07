import streamlit as st

st.title("Welcome to Vigor!")
st.sidebar.title("Welcome to Vigor!")
individual_data = st.selectbox(
    "Would you like to analyze provided or customized data?",
    [
        "Provided",
        "Customized"
    ],
)
if individual_data == "Customized":
    age = st.number_input("Please enter your age (in years)", min_value=1)
    weight = st.number_input("Please enter your weight (in pounds)")
    
    activity_level = st.slider("Please enter your activity level", min_value=1, max_value=5)
    
