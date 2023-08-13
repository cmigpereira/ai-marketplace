import gradio as gr
from transformers import pipeline

context_example = """
Machine learning (ML) is an umbrella term for solving problems for which development of algorithms by human programmers would be cost-prohibitive, and instead the problems are solved by helping machines 'discover' their 'own' algorithms, without needing to be explicitly told what to do by any human-developed algorithms. 
Recently, generative artificial neural networks have been able to surpass results of many previous approaches. Machine learning approaches have been applied to large language models, computer vision, speech recognition, email filtering, agriculture and medicine, where it is too costly to develop algorithms to perform the needed tasks.
The mathematical foundations of ML are provided by mathematical optimization (mathematical programming) methods. Data mining is a related (parallel) field of study, focusing on exploratory data analysis through unsupervised learning.
ML is known in its application across business problems under the name predictive analytics. Although not all machine learning is statistically-based, computational statistics is an important source of the field's methods.
"""
question_example = "What are the foundations of Machine learning?"

get_question_answering = pipeline("question-answering", model='distilbert-base-cased-distilled-squad')

def qa(context, question):
    if not context or not question:
        pass
    else:
        output = get_question_answering(question=question, context=context)
        return output['answer']

interface_qa = gr.Interface(qa,
                            inputs=[gr.Textbox(label="Text to ask questions from", lines=4), gr.Textbox(label="Question", lines=4)],
                            outputs=[gr.Textbox(label="Answer")],
                            examples = [[context_example, question_example]],
                            title="Question Answering",
                            description="Ask questions about a given text.",
                            css="footer{display:none !important}",
                            allow_flagging="never"
                            )