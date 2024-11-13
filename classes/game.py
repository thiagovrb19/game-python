# classes/game.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from classes.menu import Menu
from classes.player import Player
from classes.cheese import Cheese
from classes.obstacle import Obstacle
from classes.background import Background
from classes.ground import Ground
from classes.audio import Audio

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.menu = Menu(self.screen)
        self.player = Player()
        self.cheese = Cheese()
        self.obstacles = [Obstacle() for _ in range(5)]  # exemplo: 5 obstáculos
        self.background = Background()
        self.ground = Ground()
        self.audio = Audio()
        self.game_over = False
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.audio.play_music()

    def update(self):
        if not self.game_over:
            self.player.update()
            for obstacle in self.obstacles:
                if self.player.collides_with(obstacle):
                    self.player.die()
                    self.game_over = True

            if self.player.collides_with(self.cheese):
                self.end_time = pygame.time.get_ticks()
                self.game_over = True
                print(f"Você venceu! Tempo: {(self.end_time - self.start_time) / 1000} segundos")

    def render(self):
        self.background.render(self.screen)
        self.ground.render(self.screen)
        self.player.render(self.screen)
        self.cheese.render(self.screen)
        for obstacle in self.obstacles:
            obstacle.render(self.screen)
