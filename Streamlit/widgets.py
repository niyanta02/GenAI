import streamlit as st
import numpy as np
import pandas as pd

st.title("streamlit text input")

name = st.text_input("Enter your name:")

age = st.slider("Select your age", 0,100,25)
st.write(f"Your age is:{age}")

options = ["c", "c++", "java", "python"]
choice = st.selectbox("choose your favourite option",options)
st.write(f"you selected : {choice}")

if name:
    st.write(f"Hello, {name}")


data = {
    "name": ["John", "Jane", "Jake", "Jill"], 
    "Age": [28, 24,35,40], 
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file = st.file_uploader("Choose a csv file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)