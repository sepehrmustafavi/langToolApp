from transformers import pipeline
import streamlit as st

@st.cache_resource
def translate_en_to_fr(text):
    pipe = pipeline(
        task='translation',
        model='Helsinki-NLP/opus-mt-en-fr'
    )
    output = pipe(text)
    translated_text = output[0]['translation_text']
    return translated_text

if __name__ == '__main__':
    user_text = input('Enter an English text: ')
    result = translate_en_to_fr(user_text)
    print(f'Translated text : {result}')