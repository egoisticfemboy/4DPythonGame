from OpenGL.GL import *
from OpenGL.GLU import *
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, NEAR_PLANE, FAR_PLANE, FOV
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from game.world import World
from game.player import Player
from game.camera import Camera


class Camera:
    def __init__(self):
        self.position = [0.0, 0.0, 5.0]  # Camera position
        self.yaw = 0.0                   # Horizontal rotation
        self.pitch = 0.0                 # Vertical rotation

    def update(self, player_position):
        # Follow the player
        self.position = player_position.copy()
        self.position[2] += 5.0  # Offset the camera behind the player

        # Set up the view
        glLoadIdentity() 
        gluPerspective(FOV, (SCREEN_WIDTH / SCREEN_HEIGHT), NEAR_PLANE, FAR_PLANE)
        gluLookAt(
            self.position[0], self.position[1], self.position[2],  # Camera position
            player_position[0], player_position[1], player_position[2],  # Look at player
            0, 1, 0  # Up vector
        )