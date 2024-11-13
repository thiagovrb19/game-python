# classes/cheese.py
import pygame

class Cheese:
    def __init__(self):
        self.image = pygame.image.load("assets/images/cheese.png")
        self.rect = self.image.get_rect(center=(700, 500))

    def render(self, screen):
        screen.blit(self.image, self.rect)
