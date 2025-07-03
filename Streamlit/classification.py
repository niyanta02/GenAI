import numpy as np
import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.title("Iris Flower Species Prediction")

# Input features
sepal_length = st.slider("Sepal length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.slider("Sepal width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.slider("Petal length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.slider("Petal width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Prediction
prediction = model.predict(input_data)
prediction_species = target_names[prediction[0]]

st.subheader("Prediction")
st.write(f"The predicted species is: **{prediction_species}**")
