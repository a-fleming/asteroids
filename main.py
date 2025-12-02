import sys
import os
import pygame

# # show which Python and pygame are being used (useful for virtualenv debugging)
# print(f"Python executable: {sys.executable}")
# print(f"In virtualenv: {getattr(sys, 'base_prefix', None) != getattr(sys, 'prefix', None)}")
# print(f"Pygame module: {getattr(pygame, '__file__', 'built-in or frozen')}")

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
