#!/bin/python3

import speech_recognition as sr
from subprocess import call

# Função para reconhecimento de fala.
def listen_mic():
    # Habilita o microfone para para ouvir aúdio
    mic = sr.Recognizer()
    with sr.Microphone() as source:
        # Chama a função para diminuir ruídos
        mic.adjust_for_ambient_noise(source)
        # Informa ao usuário que o programa já está ouvindo.
        print("Diga alguma coisa: ")
        # Armazena o aúdio em um variável
        audio = mic.listen(source)

    try:
        # Passa o audio para o mecanimos de reconhecimento de fala
        phrase = mic.recognize_google(audio,language='pt-br')
        # Checa se o que foi dito bate com o esperado para executar a próxima atividade
        if phrase == "bloco de notas":
            print("Abrindo bloco de notas")
            call(["notepad.exe"])
        else:
            print("Você disse: " + phrase)
    except sr.UnknownValueError:
        print("Não entendi")

listen_mic()