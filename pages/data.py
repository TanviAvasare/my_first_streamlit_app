import streamlit as st
#st.title('Ramniranjan Jhunjunwala college')
st.header('Alan Turing', divider=True)
col1, col2 = st.columns(2)
with st.sidebar:
    st.link_button('Know More', 'https://en.wikipedia.org/wiki/Alan_Turing')
with col1:
    st.image('Alan_Turing_(1951).jpg')
with col2:
    st.text("Alan Turing (born June 23, 1912, London, England—died June 7, 1954, Wilmslow, Cheshire) British mathematician and logician who made major contributions to mathematics, cryptanalysis, logic, philosophy, and mathematical biology and also to the new areas later named computer science, cognitive science, artificial intelligence, and artificial life.")

with st.sidebar:
    st.link_button('Analysis', 'http://localhost:8502/')
