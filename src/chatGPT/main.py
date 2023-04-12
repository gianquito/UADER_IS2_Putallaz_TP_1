"""
Este script provee una interfaz para hacer consultas a gpt
"""
import sys
import openai
#Constantes
openai.api_key = ""
TOP_P=1
FREQ_PENALTY=0
PRES_PENALTY=0
STOP=["You:","chatGPT:"]
MAX_TOKENS=1024
TEMPERATURE=0.75
NMAX=1
MODEL_ENGINE = "text-davinci-003"

#El historial que guardará la conversación
historial = ""
#Comprueba si existe el argumento y activa el modo conversación
conversacion = len(sys.argv) > 1 and sys.argv[1] == '-convers'

#El ciclo principal del programa
while True:
    #Primer nido try/excecpt, controla que la consulta del usuario sea valida
    try:
        #Recibe la consulta del usuario
        userText = input('You: ')
        if userText == '':
            raise ValueError("Cadena vacia")
        #Segundo nido try/excecpt, controla la manipulacion de la cadena
        try:
            #Transforma la consulta para darle formato según corresponda
            if conversacion:
                userText = historial + 'You: ' + userText + '\nchatGPT:'
                historial = userText
            else:
                userText = 'You: ' + userText + '\nchatGPT:'
            #Tercer nido try/excecpt, llamada a la api
            try:
                # Realiza la consulta a la api
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
                #Muestra la respuesta
                print('chatGPT:' + completion.choices[0].text)
                #Agrega la respuesta al historial
                if conversacion:
                    historial += completion.choices[0].text + '\n'
            except:
                print("Error llamando a la API")
        except:
            print("Error en el tratamiento de la cadena")
    except ValueError as e:
        print("Error en la consulta:", e)
