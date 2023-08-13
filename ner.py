import gradio as gr
from transformers import pipeline

ner_example = [
"""
My name is Superman, and I come from the planet Krypton
""",
]

get_entities = pipeline("ner", model="dslim/bert-base-NER")

def merge_tokens(tokens):
    merged_tokens = []
    for token in tokens:
        if merged_tokens and token['entity'].startswith('I-') and merged_tokens[-1]['entity'].endswith(token['entity'][2:]):
            # If current token continues the entity of the last one, merge them
            last_token = merged_tokens[-1]
            last_token['word'] += token['word'].replace('##', '')
            last_token['end'] = token['end']
            last_token['score'] = (last_token['score'] + token['score']) / 2
        else:
            # Otherwise, add the token to the list
            merged_tokens.append(token)
    return merged_tokens

def ner(input):
    if not input:
        pass
    else:
        output = get_entities(input)
        merged_tokens = merge_tokens(output)
        return {"text": input, "entities": merged_tokens}

interface_ner = gr.Interface(fn=ner,
                            inputs=[gr.Textbox(label="Text to identify entities", lines=1)],
                            outputs=[gr.HighlightedText(label="Text with entities")],
                            examples=ner_example,
                            title="Named Entity Recognition",
                            description="Find entities in given text.",
                            css="footer{display:none !important}",
                            allow_flagging="never"
                            )