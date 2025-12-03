import pygame
import random

from circleshape import CircleShape
from constants import (
    ASTEROID_EDGE_BUFFER, 
    ASTEROID_MIN_RADIUS, 
    ASTEROID_SPLIT_SPEED_SCALE, 
    LINE_WIDTH, 
    SCREEN_HEIGHT, 
    SCREEN_WIDTH
)
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = "white"
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
        # # remove asteroid if it goes off screen
        # if (self.position.x < -ASTEROID_EDGE_BUFFER or self.position.x > SCREEN_WIDTH + ASTEROID_EDGE_BUFFER or
        #     self.position.y < -ASTEROID_EDGE_BUFFER or self.position.y > SCREEN_HEIGHT + ASTEROID_EDGE_BUFFER):
        #     print(f"Asteroid went off screen at position: {self.position}")
        #     self.kill()

        # allow asteroids to wrap around screen edges
        wrapped_edge = False
        if self.position.x < -ASTEROID_EDGE_BUFFER:
            wrapped_edge = True
            self.position.x = SCREEN_WIDTH + ASTEROID_EDGE_BUFFER
        if self.position.x > SCREEN_WIDTH + ASTEROID_EDGE_BUFFER:
            wrapped_edge = True
            self.position.x = -ASTEROID_EDGE_BUFFER
        if self.position.y < -ASTEROID_EDGE_BUFFER:
            wrapped_edge = True
            self.position.y = SCREEN_HEIGHT + ASTEROID_EDGE_BUFFER
        if self.position.y > SCREEN_HEIGHT + ASTEROID_EDGE_BUFFER:
            wrapped_edge = True
            self.position.y = -ASTEROID_EDGE_BUFFER
        if wrapped_edge:
            # change color to red
            self.color = "red"
            print(f"Asteroid wrapped around screen to position: {self.position}")   
    
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
