#!/usr/bin/python
import openai
#……. [ mas Código de inicialización aqui ] …………
openai.api_key = "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"
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

userText = input('You: ')
if(userText != ''):
    userText = 'You: ' + userText + '\nchatGPT:'
    # Set up the model and prompt
    completion = openai.Completion.create(
                    engine=MODEL_ENGINE,
                    prompt=userText,
                    max_tokens=MAX_TOKENS,
                    n=NMAX,
                    top_p=TOP_P,
                    frequency_penalty=FREQ_PENALTY,
                    presence_penalty=PRES_PENALTY,
                    temperature=TEMPERATURE,
                    stop=STOP)

    print('chatGPT:' + completion.choices[0].text)
else:
    print('La consulta está vacia')
