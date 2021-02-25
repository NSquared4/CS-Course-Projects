# Martin Bernard, Amadou Tine, Cheikhouna Gueye
import pygame
import random
import sys
from fruitClass import Fruit
from extraScreen import Screen

# initialize pygame
pygame.mixer.pre_init(44100, -16, 1, 512)  # initialize the sound
pygame.init()

# Create game window
displayW = 700
displayH = 700
win = pygame.display.set_mode((displayW, displayH))
pygame.display.set_caption("PySnake")
pygame.display.update()

# time variable to control the fps of the game
time = pygame.time.Clock()

# sound variable for the sound the snake makes when it eats the fruit
snakeBite = pygame.mixer.Sound('snakeSound.wav')

# loops variables
gameStart = True
gameOn = False
gameEnd = False

# variables to move snake
snakeXVel = 0
snakeYVel = 0
velocity = 25
snakeX = 350
snakeY = 350

# variables for displaying score
score = 0
font = pygame.font.SysFont(None, 55)

# color variables
skyblue = (135, 206, 250)
orangeRed = (255, 69, 0)

# variables to add to snake length
listSnake = []
snakeSize = 25
snakeLength = 1

# variables for fruit
fruitX = random.randint(65, 635)
while fruitX % 25 != 0:
    """Only allows fruitX to be int that are divisible by 25"""
    fruitX = random.randint(65, 635)

fruitY = random.randint(65, 635)
while fruitY % 25 != 0:
    """Only allows fruitX to be int that are divisible by 25"""
    fruitY = random.randint(65, 635)
fruit = Fruit(win, orangeRed)  # calls the fruitClass class


def scoreScreen(text, color, x, y):
    """Create the score appear on the game screen"""
    screenScore = font.render(text, True, color)
    win.blit(screenScore, [x, y])


def makeSnake(win, color, snake_list, snake_size):
    """Create the snake"""
    for x, y in snake_list:
        pygame.draw.rect(win, color, [x, y, snake_size, snake_size])


# Variable for Screen
gameStart = True
gameEnd = False
extraScreen = Screen(win)

# Loop for the start screen
while gameStart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameStart = False
        if event.type == pygame.KEYDOWN:
            if event. key == pygame.K_SPACE:
                gameStart = False
                gameOn = True

    extraScreen.startScreen()
    pygame.display.update()

# Game Loop
while gameOn:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snakeXVel = velocity
                snakeYVel = 0
            elif event.key == pygame.K_LEFT:
                snakeXVel = -velocity
                snakeYVel = 0
            elif event.key == pygame.K_UP:
                snakeYVel = -velocity
                snakeXVel = 0
            elif event.key == pygame.K_DOWN:
                snakeYVel = velocity
                snakeXVel = 0

    # Moves in the snake in snakeXVel and snakeYVel distance
    snakeX += snakeXVel
    snakeY += snakeYVel

    # list for adding length to snake body
    head = []
    head.append(snakeX)
    head.append(snakeY)
    listSnake.append(head)  # adding length to the snake

    # Collision detectioin between snake head and fruit
    if abs(snakeX - fruit.getX()) <= 20 and abs(snakeY - fruit.getY()) <= 20:
        snakeBite.play()
        score += 10
        fruitX = random.randint(65, 635)
        while fruitX % 25 != 0:
            fruitX = random.randint(65, 635)

        fruitY = random.randint(65, 635)
        while fruitY % 25 != 0:
            fruitY = random.randint(65, 635)
        snakeLength += 5

    # Ensures tha snake only grow if it eats a fruit
    if len(listSnake) > snakeLength:
        del listSnake[0]

    # Draw the snake, fruit and score on the window
    win.fill((0, 100, 0))
    pygame.draw.rect(win, (0, 50, 0), [0, 0, 700, 700], 65)
    scoreScreen("Score: " + str(score), (255, 255, 255), 0, 0)
    makeSnake(win, skyblue, listSnake, snakeSize)
    fruit.drawFruit(fruitX, fruitY)

    # Boundaries checker
    if snakeX < 35 or snakeX > 635 or snakeY < 35 or snakeY > 635 or head in listSnake[:-1]:
        gameOn = False
        gameEnd = True

    pygame.display.update()
    time.tick(10)

# End game loop
while gameEnd:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnd = False
        # If statement to close the window by pressing the "r"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                sys.exit()



    win.fill((0, 0, 0))
    extraScreen.endScreen()
    extraScreen.quit()
    pygame.display.update()
