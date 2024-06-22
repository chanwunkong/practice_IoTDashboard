import streamlit as st

with st.form('my_form'):
    st.write('Inside tje form')
    slider_val = st.slider('Form Slider')
    checkbox_val = st.checkbox('Form Checkbox')

    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write

st.write('Outside Form')