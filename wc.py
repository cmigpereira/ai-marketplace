import gradio as gr
from wordcloud import WordCloud

wc_example = ["""
Machine learning (ML) is an umbrella term for solving problems for which development of algorithms by human programmers would be cost-prohibitive, and instead the problems are solved by helping machines 'discover' their 'own' algorithms, without needing to be explicitly told what to do by any human-developed algorithms.
Recently, generative artificial neural networks have been able to surpass results of many previous approaches. Machine learning approaches have been applied to large language models, computer vision, speech recognition, email filtering, agriculture and medicine, where it is too costly to develop algorithms to perform the needed tasks.
The mathematical foundations of ML are provided by mathematical optimization (mathematical programming) methods. Data mining is a related (parallel) field of study, focusing on exploratory data analysis through unsupervised learning.
ML is known in its application across business problems under the name predictive analytics. Although not all machine learning is statistically-based, computational statistics is an important source of the field's methods.
""",]

def create_wc(text):
    """
    Generate wordcloud
    """
    if not text:
        pass
    else:
        wordcloud = WordCloud(collocations=False).generate(text.lower())
        return wordcloud.to_image()

interface_wc = gr.Interface(create_wc,
                            inputs=gr.Textbox(placeholder="Insert text here", label='Text'),
                            outputs=[gr.Image(type="pil", label="Wordcloud", show_label=False)],
                            examples = wc_example,
                            title="WordCloud builder",
                            description="Create a WordCloud from given text.",
                            css="footer{display:none !important}",
                            allow_flagging="never"
                            )