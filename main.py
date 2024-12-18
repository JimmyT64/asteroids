import pygame
from constants import *
from player import *

def main():
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
        player.update(dt)
        screen.fill("black",rect = None, special_flags = 0)
        player.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60)/1000
        

    
if __name__ == "__main__":
    main()