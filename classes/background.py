# classes/background.py
import pygame

class Background:
    def __init__(self):
        # Carrega a imagem do fundo (floresta)
        self.image = pygame.image.load("assets/images/forest_background.png")
        self.rect = self.image.get_rect()

    def render(self, screen):
        # Preenche a tela com a imagem de fundo
        screen.blit(self.image, self.rect)
