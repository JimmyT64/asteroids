import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    def draw(self,screen):
        return pygame.draw.circle(screen,"white",self.position,self.radius,width = 2)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            a = random.uniform(20,50)
            rad = self.radius - ASTEROID_MIN_RADIUS
            asta = Asteroid(self.position.x,self.position.y,rad)
            astb = Asteroid(self.position.x,self.position.y,rad)
            asta.velocity = self.velocity * 1.2
            astb.velocity = self.velocity * 1.2
            asta.velocity = pygame.math.Vector2.rotate(asta.velocity,a)
            astb.velocity = pygame.math.Vector2.rotate(astb.velocity,-a)

        
    
        
