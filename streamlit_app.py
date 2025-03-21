import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Kitchensink Streamlit Dashboard")
st.write("This is a demonstration of various Streamlit components.")

# Sidebar
st.sidebar.header("Sidebar Controls")
slider_value = st.sidebar.slider("Select a value", 0, 100, 50)
checkbox = st.sidebar.checkbox("Show DataFrame")
selectbox = st.sidebar.selectbox("Choose a chart type", ["Line Chart", "Bar Chart", "Scatter Plot"])

# Data
st.header("Random Data")
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["A", "B", "C"]
)

if checkbox:
    st.write("Here is a sample DataFrame:")
    st.dataframe(data)

# Chart
st.header("Chart Visualization")
if selectbox == "Line Chart":
    st.line_chart(data)
elif selectbox == "Bar Chart":
    st.bar_chart(data)
elif selectbox == "Scatter Plot":
    fig, ax = plt.subplots()
    ax.scatter(data["A"], data["B"], alpha=0.5)
    ax.set_xlabel("A")
    ax.set_ylabel("B")
    st.pyplot(fig)

# User Input
st.header("User Input")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# File Upload
st.header("File Upload")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    uploaded_data = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(uploaded_data)

# Progress Bar
st.header("Progress Bar")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)

# Conclusion
st.write("This is the end of the kitchensink dashboard. Explore the features!")
