# Martin Bernard, Amadou Tine, Cheikhouna Gueye
import pygame


class Fruit:
    """Class to create the fruit"""
    def __init__(self, win, color):
        """initialize instances variables needed to create the methods in fruit class
        
        Parameters:
            win: A pygame window object
            color: A rbg value color
        """
        self.gameBoard = win
        self.color = color
        self.x = 0
        self.y = 0
        self.fruitW = 25
        self.fruitH = 25

    def drawFruit(self, fruitX, fruitY):
        """Draws the fruit on the screen of the game board

        Parameters:
            fruitX: The X position of the fruit in int
            frutiY: The Y position of the fruit in int
        """
        self.x = fruitX
        self.y = fruitY
        self.fruit = pygame.draw.rect(self.gameBoard, self.color, [self.x, self.y, self.fruitW, self.fruitH])

    def getX(self):
        """Return the x position of the fruit"""
        return self.x

    def getY(self):
        """Return the y position of the fruit"""
        return self.y
