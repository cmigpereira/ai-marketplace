import gradio as gr

#Blocks or Interface instances
from summarizer import interface_summarization
from sentiment import interface_sentiment
from ner import interface_ner
from wc import interface_wc
from qa import interface_qa
from img2txt import interface_img2txt
from keyextract import interface_keyextract


with gr.Blocks(title='AI Marketplace') as main_demo:
    gr.Markdown("Your NLP Swiss Army Knife. Start by selecting the app you want to run in the tabbed interface.")

    with gr.Tabs():
        with gr.TabItem('Summarization'):
             interface_summarization.render()
        with gr.TabItem('Sentiment Analysis'):
            interface_sentiment.render()
        with gr.TabItem('NER'):
             interface_ner.render()
        with gr.TabItem('WordCloud'):
            interface_wc.render()
        with gr.TabItem('Question Answering'):
            interface_qa.render()
        with gr.TabItem('Image captioning'):
            interface_img2txt.render()
        with gr.TabItem('Keyword Extraction'):
            interface_keyextract.render()

main_demo.launch()