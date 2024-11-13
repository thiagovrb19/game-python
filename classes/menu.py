# classes/menu.py
import pygame
from classes.button import Button

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.start_button = Button("Iniciar", (150, 250))
        self.audio_button = Button("Áudio", (150, 350))
        self.exit_button = Button("Sair", (150, 450))

    def render(self):
        self.start_button.render(self.screen)
        self.audio_button.render(self.screen)
        self.exit_button.render(self.screen)
