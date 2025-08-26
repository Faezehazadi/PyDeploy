import streamlit as st

# Title
st.title("BMI Calculator")

# Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=10.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        st.write(f"Your BMI is: **{bmi:.2f}**")

        # Output
        if bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("You have Normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are Overweight")
        else:
            st.error("You are Obese")
    else:
        st.error("Please enter a valid height")





