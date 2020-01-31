import pygame
#Initialize the game engine
pygame.init()

#Define the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (255,0,0)
BLUE  = (0,0,255)

#Open a window
dimensions = (700,300)
window = pygame.display.set_mode(dimensions)
pygame.display.set_caption('PygameDrawingShapes')

#Main program

proceed = True

clock = pygame.time.Clock()

#Capturing events till exit
while proceed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            proceed = False

    window.fill(WHITE)
    #window.pygame.Surface.fill(color, rect=None, special_flags=0)
    pygame.draw.rect(window, RED, [55, 200, 100, 70], 0)
    pygame.draw.line(window, GREEN, [0, 0],  [100, 100], 1)
    pygame.draw.ellipse(window, BLUE, [20,20,250,100], 0)
    pygame.draw.circle(window, BLACK, [30, 30], 10, 0)

    pygame.display.flip()

    clock.tick(100)

pygame.quit()
