# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "George the Pumpkin"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GREY = (137, 139, 131)
STORM_SKY = (83, 109, 138)
DARK_GREEN = (83, 146, 75)
ORANGE = (255, 121, 0)
STEM_GREEN = (115, 230, 118)
BLACK = (0, 0, 0)
RAIN = (214, 229, 255)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])

ghost_position = [500, 300]

def draw_ghost(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 70, 100])
    pygame.draw.ellipse(screen, BLACK, [x + 10, y + 20, 20, 20])
    pygame.draw.ellipse(screen, BLACK, [x + 40, y + 20, 20, 20])
    pygame.draw.ellipse(screen, BLACK, [x + 20, y + 50, 30, 30])
    

    
''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])

rain = []
for n in range(1000):
    x = random.randrange(0, 800)
    y = random.randrange(0, 800)
    r = random.randrange(1, 4)
    r2 = random.randrange(1, 4)
    speed = random.randrange(1,4)
    rain.append([x, y, r, r2])

daytime = True
lights_on = False
key_down_left = False
key_down_right = False
key_down_up = False
key_down_down = False
key_down_equals = False
key_down_minus = False
    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_LEFT:
                key_down_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                key_down_left = False
    if key_down_left:
        if ghost_position[0] == -10:
            ghost_position[0] = 810
        else:
            ghost_position[0] -= 5
            
    # Game logic
    ''' move clouds '''
    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)
            
    for r in rain:
        r[1] += 2

        if r[1] > 700:
            r[0] = random.randrange(0, 800)
            r[1] = random.randrange(-200, 0)

    ''' set face color '''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
  
    # Drawing code
    ''' sky '''
    screen.fill(BLACK)
    
    ''' rain'''
    for r in rain:
        pygame.draw.ellipse(screen, RAIN, r)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])
    pygame.draw.ellipse(screen, BLACK, [550, 80, 95, 95])


    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    ''' grass '''
    pygame.draw.rect(screen, DARK_GREEN, [0, 400, 800, 200])


    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, BLACK, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
        
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]],3)
        
    pygame.draw.line(screen, WHITE, [0, 387], [800, 387], 3)
    pygame.draw.line(screen, WHITE, [0, 393], [800, 393], 3)
    pygame.draw.line(screen, BLACK, [0, 390], [800, 390], 5)
    
    pygame.draw.line(screen, WHITE, [0, 407], [800, 407], 3)
    pygame.draw.line(screen, WHITE, [0, 413], [800, 413], 3)
    pygame.draw.line(screen, BLACK, [0, 410], [800, 410], 5)
    
    
    
    ''' stem '''
    pygame.draw.rect(screen, STEM_GREEN, [395, 260, 38, 50]) 

    ''' great pumpkin '''
    pygame.draw.ellipse(screen, ORANGE, [210, 300, 400, 300])

    ''' pumpkin face'''
    if lights_on:
        pygame.draw.ellipse(screen, YELLOW, [275, 330, 100, 125])
        pygame.draw.ellipse(screen, YELLOW, [440, 330, 100, 125])
        pygame.draw.ellipse(screen, ORANGE, [275, 405, 100, 125])
        pygame.draw.ellipse(screen, ORANGE, [440, 405, 100, 125])
        pygame.draw.ellipse(screen, YELLOW, [335, 470, 150, 125])
    else:
        pygame.draw.ellipse(screen, BLACK, [275, 330, 100, 125])
        pygame.draw.ellipse(screen, BLACK, [440, 330, 100, 125])
        pygame.draw.ellipse(screen, ORANGE, [275, 405, 100, 125])
        pygame.draw.ellipse(screen, ORANGE, [440, 405, 100, 125])
        pygame.draw.ellipse(screen, BLACK, [335, 470, 150, 125])

    draw_ghost(ghost_position[0], ghost_position[1])
                                            
                                



    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
