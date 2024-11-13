# classes/audio.py

import pygame

def play_background_music():
    pygame.mixer.init()  # Inicializa o mixer de áudio
    pygame.mixer.music.load("sounds/background_music.mp3")  # Caminho correto para o arquivo
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume para 50%
    pygame.mixer.music.play(-1)  # Toca a música em loop
