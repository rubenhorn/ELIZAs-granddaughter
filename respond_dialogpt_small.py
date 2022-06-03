import sys
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


__model_name = 'microsoft/DialoGPT-small'
__tokenizer = AutoTokenizer.from_pretrained(__model_name)
__model = AutoModelForCausalLM.from_pretrained(__model_name)

def respond(text, history=None):
    if history is not None:
        print('Warning: History is not implemented', file=sys.stderr)
    global __last_response
    user_in = __tokenizer.encode(text + __tokenizer.eos_token, return_tensors='pt')
    history_out = __model.generate(user_in, max_length=1000, pad_token_id=__tokenizer.eos_token_id, temperature=0.6)
    response = __tokenizer.decode(history_out[:, user_in.shape[-1]:][0], skip_special_tokens=True)
    return (response, None)