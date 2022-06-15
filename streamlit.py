import streamlit as st
import json


# Title of our Mini-Project
c1 = st.container()
c1.title('AIAP#10 - Team 7 - Humour Detector')
c1.write('This Humour Detector decides whether your joke is humourous.')


# Text Area for Apprentice to input their name
c2 = st.container()
text_input = c2.text_input('Apprentice Name', placeholder='ENTER YOUR NAME')
if c2.button('Submit Name'):
    if text_input == '':
        c2.write('Please enter your name. Thanks!')
    else:
        c2.write(f'Hi, {text_input}. Nice to meet you!')


# Text Area for Apprentice to input their joke
c3 = st.container()
c3.header('Input Section')
c3.write('Please tell me a joke.')
text_input = c3.text_area('', placeholder='INPUT JOKE HERE')
if c3.button('Submit Feedback'):
    c3.write('Thanks for the input.')
    c3.write(f'This is your joke: {text_input}')
    joke_json = json.dump(text_input)