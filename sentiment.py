import gradio as gr
from transformers import pipeline

sentiment_examples = [
"""
I have been a customer for several years now. I have always received 
the best service, product, and customer service whenever I come here.
For all my service needs, this is the place I trust
""", """
I had a terrible experience here. Everyone was rude and unhelpful. I would not recommend this place to anyone.
""",]

sentiment = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def get_sentiment(input):
    if not input:
        pass
    else:
        output = sentiment(input.lower())
        return output[0]['label']

interface_sentiment = gr.Interface(fn = get_sentiment,
                                    inputs=gr.Textbox(label="Text", lines=4),
                                    outputs=gr.Textbox(label="Sentiment"),
                                    title = 'Sentiment Analysis',
                                    examples=sentiment_examples,
                                    description="Get Sentiment (Positive / Negative) for a given text.",
                                    css="footer{display:none !important}",
                                    allow_flagging="never"
                                    )