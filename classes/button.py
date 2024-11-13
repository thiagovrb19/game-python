# classes/button.py
import pygame

class Button:
    def __init__(self, text, position):
        self.text = text
        self.position = position
        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(position[0], position[1], 200, 50)

    def render(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.rect)
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surf, (self.position[0] + 10, self.position[1] + 10))
