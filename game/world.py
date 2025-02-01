from OpenGL.GL import *
from game.utils import project_4d_to_3d
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from game.world import World
from game.player import Player
from game.camera import Camera
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class World:
    def __init__(self):
        self.vertices_4d = [
            (-1, -1, -1, -1),
            (-1, -1, -1, 1),
            # Add all 16 vertices of a tesseract
        ]
        self.edges_4d = [
            (0, 1), (0, 2), (0, 4), (1, 3), (1, 5),
            # Add all 32 edges of a tesseract
        ]

    def render(self, camera):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_LINES)
        for edge in self.edges_4d:
            for vertex in edge:
                x, y, z = project_4d_to_3d(self.vertices_4d[vertex])
                glVertex3f(x, y, z)
        glEnd()