import streamlit as st
from transformers import pipeline


st.title('RU/ENG translation')
# текст который вводит пользователь на страничке в браузере
text_from_st = st.text_input('Text from streamlit')

translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")


def translate_model(ruText):
    st.write('Переведенный текст :', translator(ruText)[0]['translation_text'])


translate_model(text_from_st)
