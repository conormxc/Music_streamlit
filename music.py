import numpy as np
import streamlit as st
import pandas as pd
import re
import librosa

#y, sr = librosa.load('your_file.mp3')
st.title('Objective song rater')

file = st.file_uploader("Please upload your favourite song! (.mp3 only)", type = ['mp3'])

if file:
    
    if re.search('taylor', file.name, re.IGNORECASE) and re.search('swift', file.name, re.IGNORECASE):
        st.write('Oh no ...')
    
    else:
        y = librosa.load(file)
        x = int(str(y[0].max())[-1])
        if x % 5 == 0:
            st.write('Amazing!')
        elif x % 2 == 0:
            st.write('Nice song')
        else:
            st.write('Overrated')
