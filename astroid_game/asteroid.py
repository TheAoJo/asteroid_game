import random

import pygame

from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroid (CircleShape):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
    def draw(self, screen:pygame.Surface, color= "white") -> None:
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
            