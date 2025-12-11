import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

@st.cache_resource
def model_resources():
    model_name = 'facebook/bart-large-cnn'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def text_summarizer(text, max_length=50, min_length=10, do_sample=False):
    tokenizer, model = model_resources()
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=1024)

    with torch.no_grad():
        generated_ids = model.generate(
            inputs['input_ids'],
            max_length = max_length,
            min_length = min_length,
            do_sample = do_sample,
            num_beams = 4,
            early_stopping = True
        )
    
    summarized_text = tokenizer.decode(
        generated_ids[0],
        skip_special_tokens = True
    )
    return summarized_text

if __name__ == '__main__':
    test_text = 'This study examines the impact of transformer models on sentiment analysis accuracy and shows that they significantly outperform traditional approaches.'
    print(text_summarizer(test_text))