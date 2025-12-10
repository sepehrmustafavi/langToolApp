from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import streamlit as st

@st.cache_resource
def load_model_resources():
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    print('Model has loaded!✅')
    return tokenizer, model

def translate_en_to_fr(text):
    tokenizer, model = load_model_resources()
    inputs = tokenizer(text, return_tensors="pt", padding=True)

    with torch.no_grad():
        generated_ids = model.generate(
            inputs['input_ids'],
            max_length = 128,
            num_beams = 4,
            early_stopping = True
        )

    translated_text = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens = True
    )
    return translated_text

if __name__ == '__main__':
    test_text = input('Text: ')
    print(translate_en_to_fr(test_text))