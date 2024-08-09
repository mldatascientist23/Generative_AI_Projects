import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(page_title="Simple Calculator", page_icon=":abacus:")

# Apply custom CSS for background color
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.markdown("##### Created By: **Engr. Hamesh Raj**")
st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/datascientisthameshraj)")

st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Operations
operation = st.selectbox("Choose an operation", ("Addition", "Subtraction", "Multiplication", "Division", "Remainder", "Quotient"))

# Calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of adding {num1} and {num2} is {result}.")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of subtracting {num2} from {num1} is {result}.")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of multiplying {num1} by {num2} is {result}.")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of dividing {num1} by {num2} is {result}.")
        else:
            st.error("Division by zero is not allowed.")
    elif operation == "Remainder":
        if num2 != 0:
            result = num1 % num2
            st.success(f"The remainder when {num1} is divided by {num2} is {result}.")
        else:
            st.error("Division by zero is not allowed.")
    elif operation == "Quotient":
        if num2 != 0:
            result = num1 // num2
            st.success(f"The quotient when {num1} is divided by {num2} is {result}.")
        else:
            st.error("Division by zero is not allowed.")