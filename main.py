import sys

print('Loading...', end='')
sys.stdout.flush()

from listen_vosk import listen
from respond_dialogpt_small import respond
from speak_gtts import speak

def preprocess(text):
    return text # TODO not implemented

greeting = 'Hello there!'
print('\rAI:', greeting)
speak(greeting)

history = None
while True:
    print('Say something to her!', end='')
    sys.stdout.flush()
    text, _ = listen()
    text = preprocess(text)
    print('\rYou:', text if len(text) > 0 else '...', ' ' * 15)
    if len(text) == 0:
        break
    text, history = respond(text, history)
    print('AI:', text)
    speak(text)

salutation = 'Well... I\'ll be here if you want to talk.'
print('AI:', salutation)
speak(salutation)
