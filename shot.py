import pygame

from circleshape import CircleShape
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SHOT_EDGE_BUFFER,
    SHOT_RADIUS
)

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        
        # remove the shot if it goes off screen
        if (self.position.x < -SHOT_EDGE_BUFFER or self.position.x > SCREEN_WIDTH + SHOT_EDGE_BUFFER or
            self.position.y < -SHOT_EDGE_BUFFER or self.position.y > SCREEN_HEIGHT + SHOT_EDGE_BUFFER):
            self.kill()
    