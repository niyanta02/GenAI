import pandas as pd
import numpy as np
import streamlit as st

#Title of the aplication
st.title("Hello, My Streamlit app")

#display a simple text
st.write("this is a simple text")

#create a dataframe 
df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})

#display dataframe 
st.write("here is my dataframe")
st.write(df)

#craete a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns = ['a', 'b','c']
)
st.line_chart(chart_data)