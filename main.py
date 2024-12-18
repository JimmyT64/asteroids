import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids,drawable,updateable)
    Shot.containers = (shots,drawable,updateable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    pygame.init
    Clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        screen.fill("black",rect = None, special_flags = 0)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60)/1000
        for ast in asteroids:
            if ast.collision(player) == True:
                print("Game over!")
                exit()
        
        

    
if __name__ == "__main__":
    main()