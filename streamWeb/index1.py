# index1
import streamlit as st

st.write('## Hello **_World_**')

st.title('Title')
st.subheader('subHeader')
st.caption('caption')
st.markdown('markdowm')
st.divider()
st.markdown('上面橫線是divider')
st.code('''
print('Hello World!')
''')

# index2
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

# index3
import numpy as np

with st.container():
    st.write('This is inside the container')
    st.bar_chart(np.random.randn(50,3))

st.write(np.random.randn(50,3))

# index4
# import time

# placehoder = st.empty()

# with st.empty():
#     for seconds in range(60):
#         st.write(f'{seconds} seconds have passed')
#         time.sleep(1)

#     st.write('1 minute over!')

# time.sleep(5)
# placehoder.empty()

# index5
st.bar_chart({'data':[1, 5, 2, 3, 6]})

with st.expander('See explanation'):
    # st.markdown('')
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyQeKMmWgVVFB1BESinASmyvJUJmLIkDyFzw&s')

# index6
st.write('Sumit and work')
with st.form('my_form'):
    st.write('Inside the form')
    slider_val = st.slider('Form Slider')
    checkbox_val = st.checkbox('Form Checkbox')

    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('slide', slider_val, 'checkbox', checkbox_val )

# index7
st.write('Live work')
slider_val_2 = st.slider('Form Slider')
checkbox_val_2 = st.checkbox('Form Checkbox')

st.write('slide', slider_val_2, 'checkbox', checkbox_val_2 )

# index8
with st.popover('open popover'):
    st.markdown('Hello')
    name = st.text_input("What's your name?")

st.write('your name:', name)

# index9

# # type1
# select1 = st.sidebar.selectbox('How', ('Email', 'Phone'))

# type2
with st.sidebar:
    select2 = st.radio('How', ('Email', 'Phone'))

st.write(select2)