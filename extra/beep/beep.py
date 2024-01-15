import pygame
import time
import os
import sys
sys.path.append(os.getcwd())
from lib.core.Exceptions.exceptions import SQLGOBeepSoundException

def find_beep_wav():
    module_directory = os.path.dirname(os.path.abspath(__file__))
    beep_wav_path = os.path.join(module_directory, 'beep.wav')
    return beep_wav_path if os.path.exists(beep_wav_path) else None

def beep():
    pygame.mixer.init()
    beep_wav_path = find_beep_wav()

    if beep_wav_path:
        sound = pygame.mixer.Sound(beep_wav_path)
        sound.play()
        time.sleep(0.5)  # Adjust the sleep time as needed
    else:
        raise SQLGOBeepSoundException

beep()
