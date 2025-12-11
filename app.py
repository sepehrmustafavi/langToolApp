import streamlit as st
import translator
import summarizer

st.set_page_config(page_title='Lang Tool App')

menu = st.sidebar.selectbox(
    'Tool selection:',
    ['Translator', 'Summarizer']
)

if menu == 'Translator':
    tran_text = st.text_area('Enter your text here:')
    if st.button('Translate'):
        with st.spinner('Translating...'):
            result = translator.translate_en_to_fr(tran_text)
            st.write(result)
            st.success('Done✅')

if menu == 'Summarizer':
    sum_text = st.text_area('Enter your text here:')
    if st.button('Summarize'):
        with st.spinner('Summarizing...'):
            result2 = summarizer.text_summarizer(sum_text)
            st.write(result2)
            st.success('Done✅')