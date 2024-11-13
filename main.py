# main.py
import pygame
from classes.player import Player
from classes.obstacle import Obstacle

pygame.init()

# Configurações básicas da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo do Rato")

# Criação do jogador e obstáculos
player = Player()
obstacles = [
    Obstacle(300, 500, 50, 50),
    Obstacle(500, 400, 50, 50),
    Obstacle(200, 300, 50, 50)
]

# Definir a posição do queijo
cheese_image = pygame.image.load("assets/images/cheese.png")
cheese_image = pygame.transform.scale(cheese_image, (30, 30))  # Escala a imagem do queijo
cheese_rect = cheese_image.get_rect(topleft=(700, 100))

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((0, 255, 0))  # Background verde para simular a grama

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    # Detectar colisão com obstáculos
    for obstacle in obstacles:
        if obstacle.check_collision(player.rect):
            print("O rato morreu. Tente novamente.")
            player.reset()  # Reseta a posição do jogador

    # Detectar se o jogador pegou o queijo
    player.collect_cheese(cheese_rect)
    if player.has_cheese and player.rect.colliderect(cheese_rect):
        print("O rato pegou o queijo e voltou para a toca! Parabéns!")
        running = False  # Encerra o jogo

    # Renderizar todos os elementos na tela
    player.render(screen)
    for obstacle in obstacles:
        obstacle.render(screen)
    screen.blit(cheese_image, cheese_rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
