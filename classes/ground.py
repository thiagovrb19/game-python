# classes/ground.py
import pygame

class Ground:
    def __init__(self):
        # Carrega a textura do chão
        self.image = pygame.image.load("assets/images/ground_texture.png")
        self.rect = self.image.get_rect()
        self.rect.y = 500  # Posiciona o chão na parte inferior da tela

    def render(self, screen):
        # Renderiza a textura do chão na parte inferior da tela
        screen.blit(self.image, self.rect)
