import streamlit as st
import pandas as pd
import pickle
import re, os

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def load_cuisine_predictor():
    print('loading model')
    return pickle.load(open('models/cuisine_predction_model', 'rb'))


def predict_cuisine(ingredients):
    print(ingredients)
    sgd = load_cuisine_predictor()
    return sgd.predict([ingredients])

st.subheader('Ingredients')
# st.write('Enter the ingredients you have')

col1, col2, col3 = st.columns(3)
with col1:
    i1 = st.text_input('', key='i1')
    i2 = st.text_input('', key='i2')
    i3 = st.text_input('', key='i3')
    i4 = st.text_input('', key='i4')
with col2:
    i5 = st.text_input('', key='i5')
    i6 = st.text_input('', key='i6')
    i7 = st.text_input('', key='i7')
    i8 = st.text_input('', key='i8')
with col3:
    i9 = st.text_input('', key='i9')
    i10 = st.text_input('', key='i10')
    i11 = st.text_input('', key='i11')
    i12 = st.text_input('', key='i12')


predict_button = st.button('Whats the cuisine?')

if predict_button:
    ingredients = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12]
    ingredients = ' '.join(ingredients)
    if ingredients is None or len(ingredients.strip()) == 0:
        st.error('Add few ingredients')
    else:
        cuisine = predict_cuisine(ingredients)[0].title()
        st.header(cuisine.title())
        try:
            st.image(os.path.join(os.path.dirname(os.path.abspath(__file__)),f'img/{cuisine}.jpeg'), width=300)
        except FileNotFoundError:
            println(f'Could not find image for {cusine}')



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
