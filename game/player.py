import pygame
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from game.world import World
from game.player import Player
from game.camera import Camera
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player:
    def __init__(self):
        self.position = [0.0, 0.0, 0.0]  # (x, y, z)
        self.rotation = [0.0, 0.0]       # (yaw, pitch)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position[2] -= PLAYER_SPEED  # Move forward
        if keys[pygame.K_s]:
            self.position[2] += PLAYER_SPEED  # Move backward
        if keys[pygame.K_a]:
            self.position[0] -= PLAYER_SPEED  # Move left
        if keys[pygame.K_d]:
            self.position[0] += PLAYER_SPEED  # Move right
        if keys[pygame.K_SPACE]:
            self.position[1] += PLAYER_SPEED  # Move up
        if keys[pygame.K_LSHIFT]:
            self.position[1] -= PLAYER_SPEED  # Move down