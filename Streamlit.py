import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.set_page_config(layout="wide")
st.header('Streamlit')

page = st.sidebar.selectbox('Select page', ['Ankieta', 'Straty'])


def validation():
    if firstname == "" or lastname == "":
        st.info("Please confirm the fields and submit it again.")
    else:
        st.success("Data saved correctly.")


if page == 'Ankieta':
    firstname = st.text_input("First Name")
    lastname = st.text_input("Last Name")

    st.button("Submit", on_click=validation)

if page == 'Straty':
    data = st.file_uploader("Upload your dataset", type=['csv'])
    if data is not None:
        with st.spinner("Waiting..."):
            time.sleep(2)
            st.success("Dataset uploaded")
        df = pd.read_csv(data)
        st.dataframe(df.head(20))

        columns = df.columns.to_list()
        selected_columns = st.multiselect("Select columns to plot", columns)
        plot_data = df[selected_columns]
        selected_chart = st.selectbox("Select chart type", ['Histogram', 'Scatter plot'])
        if selected_chart == 'Histogram':
            fig = px.scatter(plot_data)
            st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
        if selected_chart == 'Scatter plot':
            fig = px.histogram(plot_data)
            st.plotly_chart(fig, theme="streamlit", use_conatiner_width=True)
