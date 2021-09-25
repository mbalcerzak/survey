from typing import List
import streamlit as st
import json


def create_slider_severity(x: str):
    """ X = symptom """
    return st.slider(f'Please rate the severity of {x}', 1, 3, 1)


def create_radio(x: str, options: List):
    st.radio(label = f'{x}', options=options)
    return st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', 
            unsafe_allow_html=True) 


with open('data/questions.json', 'r') as f:
    questions = json.load(f)


gender = 'Female'

st.header('Welcome back Sarah :)')
st.write('Completing the survey usually takes 14 minutes')

# st.write(
#     '''Your doctor was worried about your previous answers and we would 
#     like to check up if the answers to a few questions have changed:''')
# symptom = st.radio(
#     label=('You mentioned on 25-04-2021 that you experienced severe nausea.' 
#     'Is that still a symptom you\'re experiencing?'), 
#     options=['No', 'Yes'],
#     )
# if symptom == 'Yes':    
#     st.slider(f'Please rate the severity of Nausea (1 means "Not at all" and 4 "Very much")', 1, 3, 1)


st.subheader('Overall wellbeing ')
# Overall wellbeing 
# 29, 30
for n in [29, 30]:
    create_radio(
        questions[str(n)], 
        ['Very Poor :(', 'Poor', 'OK', 'Good', 'Very good', 'Excellent :)']
    )

# trouble walking / lifting
for n in range(1,8):
    create_radio(
        questions[str(n)], 
        ['Not at all','Sometimes','Often','Very much']
    )


# to remove
for n in range(19, 48):
    create_radio(
    questions[str(n)], 
    ['Not at all','Sometimes','Often','Very much']
    )  
###

# Questions about past week 
# Questions 8-18, 70
st.subheader('In the past week... ')
last_week_symptoms = st.multiselect(
     'Have you experienced: ',
     ['Constipation', 'Diarrhea', 'Lack of apetite', 'Loss of hair',
      'Nausea', 'Pain', 'Shortness of breath', 'Tangling hads or feet', 
      'Tiredness', 'Troubles sleeping', 'Weakness'])

for last_week_symptom in last_week_symptoms:
    create_slider_severity(last_week_symptom)

# stoma
stoma = st.radio(questions["48"], ('No', 'Yes'))

if stoma == 'Yes':
    for n in range(49, 56):
        create_radio(
            questions[str(n)], 
            ['Not at all','Sometimes','Often','Very much']
        )
else:
    for n in range(56, 62):
        create_radio(
            questions[str(n)], 
            ['Not at all','Sometimes','Often','Very much']
        )

st.subheader('In the past 4 weeks ... ')

# interest in sex
create_radio(
        questions["62"], 
        ['Not at all','Sometimes','Often','Very much']
    )

if gender == 'Female':
    create_radio(
            questions["65"], 
            ['Not at all','Sometimes','Often','Very much']
        )
elif gender == 'Male':
    create_radio(
            questions["63"], 
            ['Not at all','Sometimes','Often','Very much']
        )

for n in range(66, 70):
    create_radio(
        questions[str(n)], 
        ['Not at all','Sometimes','Often','Very much']
    )

if st.button('Sumbit results'):
    st.write('Thank you for completing the survey Sarah :)')
