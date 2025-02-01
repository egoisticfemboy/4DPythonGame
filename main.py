import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from game.world import World
from game.player import Player
from game.camera import Camera
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("4D Simulation Game")

    # Initialize game components
    camera = Camera()
    player = Player()
    world = World()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update player and camera
        player.update()
        camera.update(player.position)

        # Render the world
        world.render(camera)

        pygame.display.flip()

if __name__ == "__main__":
    main()