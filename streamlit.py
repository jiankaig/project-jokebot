import streamlit as st


c1 = st.container()
c1.title('AIAP#10 - Team 7 - Joke Bot')
c1.write('This Joke Bot generates jokes for our AIAP apprentices.')


# Text Area for Apprentice to input their name
c2 = st.container()
text_input = c2.text_input('Apprentice Name', placeholder='Enter you name')
if c2.button('Submit Name'):
    if text_input == '':
        c2.write('Please enter your name. Thanks!')
    else:
        c2.write(f'Hi, {text_input}. Nice to meet you!')


# Option for Apprentice to choose the type of joke
c3 = st.container()
preference = c3.selectbox('Choose your preference', ['Reddit', 'Stupidstuff', 'Wocka'])
button1 = c3.button('Submit Preference')
if button1:
    if preference == 'Reddit':
        c3.write('REDDIT JOKE!')
    elif preference == 'Stupidstuff':
        c3.write('STUPIDSTUFF JOKE!')
    elif preference == 'Wocka':
        c3.write('WOCKA JOKE!')
    else:
        c3.write('Please state your preference.')


c4 = st.container()
joke_button = c4.button('Click me for a joke!')
if joke_button:
    c4.write('Here is the joke!')


# Feedback Section that includes 'LIKE' and 'DISLIKE'
c5 = st.container()
c5.header('Feedback')
like = c5.checkbox('LIKE')
dislike = c5.checkbox('DISLIKE')
button2 = c5.button('Submit')
if button2 & like & dislike:
    c5.write('Please choose 1 option ONLY!')
elif button2 & like:
    c5.write('You liked the joke! ;D')
elif button2 & dislike :
    c5.write('You disliked the joke! ;(')
else:
    c5.write('Please choose!')


def run_sentiment_analysis(text):
    st.write('Sentiment Analysis Completed!')


c6 = st.container()
c6.header('Remarks Section')
c6.write('What did you think of the joke?')
text_input = c6.text_area('')
if c6.button('Submit Feedback'):
    c6.write('Sentiment Analysis Result: ', run_sentiment_analysis(text_input))