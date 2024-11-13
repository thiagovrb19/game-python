# obstacle.py
import pygame

class Obstacle:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))  # Cor vermelha para o obstáculo
        self.rect = self.image.get_rect(topleft=(x, y))

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
