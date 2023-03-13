import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import time

st.header("Results of the file")
file = st.file_uploader(label = "upload your excel dataset")
try:
    df = pd.read_excel(file)
    st.write(df)
    column_list = df.columns.to_list()
    first_column = column_list[0]
    dataset_columns = column_list[1:len(column_list)]
    selector = st.sidebar.selectbox(label="Select the type of graph", options = ["Heap-map" , "Scatterplot",  "Line Chart", "Bar Graph"] )
    column_of_dataset = st.sidebar.selectbox(label="Select your column", options=dataset_columns)
    if selector == "Heap-map":
        st.sidebar.warning("The column selection will not affect the heapmap figure")
        All = df[dataset_columns]
        fig1 = px.imshow(df, labels = dict(x = 'Details', y = 'Category', color = "Highest to lowest"), y = df[first_column], text_auto = True )
        st.plotly_chart(fig1, text_auto=True, use_container_width= True)
    elif selector == 'Scatterplot':
        fig = px.scatter(df, y = column_of_dataset, x = first_column)
        st.plotly_chart(fig)
    elif selector == 'Line Chart':
        fig = px.line(df, y = column_of_dataset, x = first_column)
        st.plotly_chart(fig)
    elif selector == 'Bar Graph':
        fig = px.bar(df, y = column_of_dataset, x = first_column)
        st.plotly_chart(fig)

        
except:
    if file is None:
        time.sleep(5)
        st.warning("Please upload your file")
