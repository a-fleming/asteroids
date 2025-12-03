import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_SCALE, LINE_WIDTH
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        angle_offset = random.uniform(20, 50)

        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = self.velocity.rotate(-angle_offset) * ASTEROID_SPLIT_SPEED_SCALE

        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid.velocity = self.velocity.rotate(angle_offset) * ASTEROID_SPLIT_SPEED_SCALE
