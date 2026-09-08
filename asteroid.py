import pygame
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import random
from logger import log_event

from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius, LINE_WIDTH,)

    def update(self,dt):
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        split_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1, ast2 = Asteroid(self.position.x, self.position.y, new_radius), Asteroid(self.position.x, self.position.y, new_radius)
        ast1.velocity, ast2.velocity = 1.2*self.velocity.rotate(split_angle), 1.2*self.velocity.rotate(-split_angle)
        