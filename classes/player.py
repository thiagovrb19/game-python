# player.py
import pygame

class Player:
    def __init__(self):
        self.image = pygame.image.load("assets/images/mouse.png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Escala a imagem para 50x50 px
        self.rect = self.image.get_rect(topleft=(100, 500))  # Posição inicial do rato ajustada
        self.speed = 5
        self.has_cheese = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def collect_cheese(self, cheese_rect):
        if self.rect.colliderect(cheese_rect):
            self.has_cheese = True

    def reset(self):
        self.rect.topleft = (100, 500)  # Posição de reset para evitar sobreposição com obstáculos
        self.has_cheese = False
