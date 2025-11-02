import streamlit as st

st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator App")

st.markdown("Perform basic arithmetic operations below:")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Division by zero is not allowed!")
                result = None
            else:
                result = num1 / num2

        if result is not None:
            st.success(f"✅ Result: **{result:.4f}**")

    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
