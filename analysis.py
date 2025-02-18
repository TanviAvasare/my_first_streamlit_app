import pandas as pd
import streamlit as st
df = pd.read_csv('Automobile.csv')
st.dataframe(df)
st.bar_chart(data=df, x='length', y='mileage', x_label='Length', y_label='Mileage')
st.bar_chart(data=df, x='mileage', y='company', x_label='Mileage', y_label='Company')
