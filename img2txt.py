import gradio as gr
from transformers import pipeline

get_caption = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def caption(img):
    if not img:
        pass
    else:
        output = get_caption(img)
        return output[0]["generated_text"]

interface_img2txt = gr.Interface(fn=caption,
                                inputs=gr.Image(label="Image", type='pil'),
                                outputs=gr.Textbox(label="Caption"),
                                examples=["imgs/car.jpg", "imgs/tiger.jpg", "imgs/swan.jpg"],
                                title="Image captioning",
                                description="Get a image caption.",
                                css="footer{display:none !important}",
                                allow_flagging="never"
                                )
