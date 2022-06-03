import sys
import pyttsx3

__engine = pyttsx3.init()
__engine.setProperty('rate', 160)

__voices = __engine.getProperty('voices')

def speak(text, lang=None):
    voice_id = None
    if lang is not None:
        for voice in __voices:
            if voice.languages[0] == lang:
                voice_id = voice.id
    if voice_id is not None:
        __engine.setProperty('voice', voice_id)
    elif lang is not None:
        print('Warning: Invalid language name', file=sys.stderr)
    __engine.say(text)
    __engine.runAndWait()