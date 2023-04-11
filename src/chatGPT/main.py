import openai
#……. [ mas Código de inicialización aqui ] …………
openai.api_key = ""
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=None
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

try:
    userText = input('You: ')
    if(userText == ''):
        raise Exception("Cadena vacia")
    try:
        userText = 'You: ' + userText + '\nchatGPT:'
        try:
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
        except:
            print("Error llamando a la API")
    except:
        print("Error en el tratamiento de la cadena")
except:
    print("Error en la consulta del usuario")
# if(userText != ''):
    
   

# else:
#     print('La consulta está vacia')
