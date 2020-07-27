# Voice Recon

Utilizando da biblioteca speech_recognition e subprocess criei um programa para abrir o bloco de notas por comando de voz. Deve ser um terrível programa pra se fazer isso, tanto que abrir-lo de forma convenvional é muito mais prático, contudo fiz para utilizar a biblioteca por curiosidade e é muito fázil de utiliza-la! Nem parece que várias empresas num passado não tão distante sofreram tanto para produzir algo que hoje qualquer um pode utilizar.

## Usage

```python
import speech_recognition as sr
from subprocess import call

Syntax:> python voice_recon.py
O programa irá printar na tela:
"Diga alguma coisa: "

Após você falar ele irá retornar o que você disse, no meu caso, fiz com o objetivo
de se falar bloco de notas, para abrir o mesmo.
```

## Aprendendo
Projeto feito só para utilização da lib.