from transformers import pipeline

def summarizer(text, max_length = 50, min_length = 10 , do_sample = False):
    print("Loading...")
    pipe = pipeline(
        task = 'summarization',
        model = 'facebook/bart-large-cnn'
    )
    output = pipe(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    summarized_text = output[0]['summary_text']
    return summarized_text

if __name__ == '__main__':
    user_text = input('Enter a text: ')
    result = summarizer(user_text)
    print(f'\nSummerized text : {result}')