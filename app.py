import streamlit as st


st.header('Hello again :)')
st.write('Completing the survey usually takes 14 minutes')

st.write(
    '''Your doctor was worried about your previous answers and we would 
    like to check up if the answers to a few questions have changed:''')

symptom = st.radio(
    label=('You mentioned on 25-04-2021 that you experienced severe nausea.' 
    'Is that still a symptom you\'re experiencing?'), 
    options=['No', 'Yes'],
    )

if symptom == 'Yes':    
    st.slider(f'Please rate the severity of Nausea (1 means "Not at all" and 4 "Very much")', 1, 3, 1)

st.subheader('Sliders?')
last_week_symptoms = st.multiselect(
     'In the PAST WEEK have you experienced',
     ['Nausea', 'Pain', 'Weakness', 'Tiredness', 'Shortness of breath', 'Diarrhea', 'Lack of apetite', 'Troubles concentrating','Loss of hair'])

for last_week_symptom in last_week_symptoms:
    st.slider(f'Please rate the severity of {last_week_symptom}', 1, 3, 1)


st.subheader('Radio buttons?')
st.radio(label = 'Please rate the severity of your pain last week', options = ['Not at all','Sometimes','Often','Very much'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)