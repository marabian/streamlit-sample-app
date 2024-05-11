import streamlit as st

# 1. Styling Buttons

st.markdown("""
<style>
button {
    color: white;
    background-color: blue;
    border-radius: 10px;
    border: 2px solid white;
}
</style>
""", unsafe_allow_html=True)

st.button("Styled Button")


# 2. Styling Text Inputs

st.markdown("""
<style>
.stTextInput > div > div > input {
    color: black;
    background-color: yellow;
}
</style>
""", unsafe_allow_html=True)

st.text_input("Styled Text Input")

# 3. Styling Sliders

st.markdown("""
<style>
.css-14s5rfu {
    color: black; /* This styles the numeric input part of the slider */
}
.css-j7qwjs {
    background-color: #f63366; /* This styles the background of the slider */
}
</style>
""", unsafe_allow_html=True)

st.slider("Styled Slider", 0, 100, 50)

# 4. Styling Checkboxes

st.markdown("""
<style>
.stCheckbox > div {
    background-color: #f1f1f1;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.checkbox("Styled Checkbox")

# 5. Styling Radio Buttons

st.markdown("""
<style>
.stRadio > div {
    background-color: #abc;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.radio("Styled Radio", ['Option 1', 'Option 2', 'Option 3'])

# 6. Styling DataFrames

import pandas as pd

# Styling for dataframes
st.markdown("""
<style>
.stDataFrame {
    font-family: monospace;
    background-color: #f4f4f2;
}
</style>
""", unsafe_allow_html=True)

df = pd.DataFrame({
    'A': range(1, 6),
    'B': range(10, 15)
})
st.dataframe(df)


# General Tips for Styling
# Inspect Element: Use your browser's developer tools to inspect the elements and find the appropriate classes applied by Streamlit. This can help you target your CSS more accurately.
# Specificity and Scope: The more specific your CSS selectors, the less likely they are to impact unintended parts of your app. Streamlit may use generic class names that can affect multiple widgets if not carefully targeted.
# Testing and Maintenance: Regularly test your styles with different browsers and Streamlit versions, as updates may affect how styles are applied.
