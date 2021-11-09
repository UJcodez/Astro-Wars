##
# AstroWars
# Usayd Jahangiri
##

## Setup

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 128, 255)

# initialize font
pygame.font.init()

# Load background
background_image = pygame.image.load("space.png")

## Blue Player Atrributes

# player image
blue_player_image = pygame.image.load("spaceship.png")
blue_player_image = pygame.transform.rotate(blue_player_image, 90)

# set position
blue_x = 700
blue_y = 250

# speed vector
blue_Xchange = 0
blue_Ychange = 0

# blue player score
score_blue = 100
blue_text = pygame.font.Font(None, 36)
textblueX = 760
textblueY = 5

## Red Player Attributes

# player image
red_player_image = pygame.image.load("redship.png")
red_player_image = pygame.transform.rotate(red_player_image, 270)

# set position
red_x = 150
red_y = 250

# speed vector
red_Xchange = 0
red_Ychange = 0

# blue player score
score_red = 100
red_text = pygame.font.Font(None, 36)
textredX = 5
textredY = 5

## Blue laser

# laser image
blue_laser_image = pygame.image.load("blueLaser.png")
blue_laser_image = pygame.transform.scale(blue_laser_image, [42,27])
#blue_laser_image = pygame.transform.rotate(blue_laser_image, 270)

# set position
blue_laser_x = 700
blue_laser_y = 0

# set speed
blue_laser_Xchange = 15
blue_laser_Ychange = 0

# state of laser
blue_laser_state = "set"

## Red laser

# laser image
red_laser_image = pygame.image.load("redLaser.png")
red_laser_image = pygame.transform.scale(red_laser_image, [60,40])

# set position
red_laser_x = 150
red_laser_y = 0

# set speed
red_laser_Xchange = 15
red_laser_Ychange = 0

# state of laser
red_laser_state = "ready"

# font for game over
text_over = pygame.font.Font(None, 64)

## Defining objects

# define blue player
def bluePlayer(x,y):
    screen.blit(blue_player_image, [x,y])

# define red player
def redPlayer(x,y):
    screen.blit(red_player_image, [x,y])

# define blue score
def blueScore(x,y):
    blue_points = blue_text.render("Health: " +str(score_blue), True, BLUE)
    screen.blit(blue_points, (x,y))

# define red score
def redScore(x,y):
    red_points = red_text.render("Health: " +str(score_red), True, RED)
    screen.blit(red_points, (x,y))

# Define game over
def gameOverRed():
    show_over = text_over.render("Red Player Wins!!!", True, RED)
    screen.blit(show_over, (250, 250))

def gameOverBlue():
    show_overblue = text_over.render("Blue Player Wins!!!", True, BLUE)
    screen.blit(show_overblue, (250, 250))

# define laser
def blueLaser(x,y):
    global blue_laser_state
    blue_laser_state = "shoot"
    screen.blit(blue_laser_image, [x,y])

# define red laser
def redLaser(x,y):
    global red_laser_state
    red_laser_state = "fire"
    screen.blit(red_laser_image, [x,y])

 # Define collision
def checkCollision(red_x, red_y, blue_laser_x, blue_laser_y):
    # use distance formula ((d = √((x_2-x_1)² + (y_2-y_1)²))
    # (exponent 0.5 can be used to sqaure root formula)
    distance = ((red_x - blue_laser_x)**2 + (red_y - blue_laser_y)**2)**0.5
    if distance <= 27:
        return True
    else:
        return False

 # Define collision
def checkCollisionRed(blue_x, blue_y, red_laser_x, red_laser_y):
    # use distance formula ((d = √((x_2-x_1)² + (y_2-y_1)²))
    # (exponent 0.5 can be used to sqaure root formula)
    distance_red = ((blue_x - red_laser_x)**2 + (blue_y - red_laser_y)**2)**0.5
    if distance_red <= 27:
        return True
    else:
        return False

pygame.init()

## screen setup

# Set the width and height of the screen [width, height]
size = (900, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("AstroWars")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

## -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # manual control of blue player
            if event.key == pygame.K_RIGHT:
                blue_Xchange = 7
            elif event.key == pygame.K_LEFT:
                blue_Xchange = -7
            elif event.key == pygame.K_UP:
                blue_Ychange = -7
            elif event.key == pygame.K_DOWN:
                blue_Ychange = 7

            # manual control of blue laser
            elif event.key == pygame.K_SPACE:
                if blue_laser_state == "set":
                    blue_laser_y = blue_y
                    blue_laser_x = blue_x
                    blueLaser(blue_laser_x, blue_laser_y)

            # manual control of red laser
            elif event.key == pygame.K_q:
                if red_laser_state == "ready":
                    red_laser_y = red_y
                    red_laser_x = red_x
                    redLaser(red_laser_x, red_laser_y)

            # manual control of red player
            elif event.key == pygame.K_d:
                red_Xchange = 7
            elif event.key == pygame.K_a:
                red_Xchange = -7
            elif event.key == pygame.K_w:
                red_Ychange = -7
            elif event.key == pygame.K_s:
                red_Ychange= 7

        # User let up on a key for blue player?
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                blue_Xchange = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                blue_Ychange = 0
        # User let up on a key for red player?
            elif event.key == pygame.K_a or event.key == pygame.K_d:
                red_Xchange = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                red_Ychange = 0


# --- Game logic

    # Move blue player according to spped vector
    blue_x = blue_x + blue_Xchange
    blue_y = blue_y + blue_Ychange

    # Move red player according to speed vector
    red_x = red_x + red_Xchange
    red_y = red_y + red_Ychange

    # Player Boundries
    if blue_x <= 650:
        blue_x = 650
    elif blue_x >= 846:
        blue_x = 846
    if blue_y <= 0:
        blue_y = 0
    elif blue_y >= 546:
        blue_y = 546

    # Player Boundries
    if red_x >= 150:
        red_x = 150
    elif red_x <= 0:
        red_x = 0
    if red_y <= 0:
        red_y = 0
    elif red_y >= 546:
        red_y = 546

    # check collision
    collisionBlue = checkCollision(red_x, red_y, blue_laser_x, blue_laser_y)
    if collisionBlue:
        blue_laser_x = 700
        blue_laser_state = "set"
        score_red -= 10
        print(score_blue)

    # check collision
    collisionRed = checkCollisionRed(blue_x, blue_y, red_laser_x, red_laser_y)
    if collisionRed:
        red_laser_x = 150
        red_laser_state = "ready"
        score_blue -= 10
        print(score_red)

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image, [0,0])

    ## Drawing code should go here

   # bullet boundaries
    if blue_laser_x <= 0:
        blue_laser_x = blue_x
        blue_laser_state = "set"
    if blue_laser_state  == "shoot":
        blueLaser(blue_laser_x - 10, blue_laser_y + 20)
        blue_laser_x -= blue_laser_Xchange

    # red bullet boundaries
    if red_laser_x >= 900:
        red_laser_x = red_x
        red_laser_state = "ready"
    if red_laser_state  == "fire":
        redLaser(red_laser_x + 20, red_laser_y + 12)
        red_laser_x += red_laser_Xchange

    # draw line
    y = 0
    while y < 900:
        pygame.draw.line(screen, WHITE, [450, 0+y], [450, 40+y], 4)
        y = y + 70


    # draw blue score
    blueScore(textblueX, textblueY)

    # draw red score
    redScore(textredX, textredY)

    # draw blue player
    bluePlayer(blue_x, blue_y)

    # draw red player
    redPlayer(red_x, red_y)

    # game over
    if score_blue <= 0:
        screen.fill(BLACK)
        gameOverRed()
    if score_red <= 0:
        screen.fill(BLACK)
        gameOverBlue()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

