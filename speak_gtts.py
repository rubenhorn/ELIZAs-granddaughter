from gtts import gTTS
from io import BytesIO
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


pygame.init()
pygame.mixer.init()

def speak(text, lang='en'):
    mp3_fp = BytesIO()
    tts = gTTS(text, lang=lang)
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
