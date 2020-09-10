import streamlit as st
import os
import speech_recognition as sr
import time


st.title("Speech to Text App")


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select an audio file (only supports .wav)', filenames) #will have to put audio files in the same directory
    os.path.join(folder_path, selected_filename)



filename = file_selector()
st.write('`%s` Audio file successfully uploaded' % filename)
with st.spinner('Transcribing speech to text...'):
    time.sleep(5)
    st.success('Done!')


def speechtotext():
    if st.button("Convert Speech to Text"):
        r = sr.Recognizer()
        audio_file = sr.AudioFile(filename)
    with audio_file as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    result = r.recognize_google(audio)
    st.write(result)
speechtotext()
