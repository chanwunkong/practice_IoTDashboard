import streamlit as st
col1, col2 = st.columns(2)

col1.title('欄位1title')
col1.header('欄位1header')
col1.subheader('欄位1subHeader')

col2.title('欄位2title')
col2.header('欄位2header')
col2.subheader('欄位2subHeader')

col3, col4 = st.columns(2)
with col3:
    st.title('欄位3title')
    st.header('欄位3header')
    st.subheader('欄位3subHeader')

with col4:
    st.title('欄位4title')
    st.header('欄位4header')
    st.subheader('欄位4subHeader')