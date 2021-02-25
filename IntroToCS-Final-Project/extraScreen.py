# Martin Bernard, Amadou Tine, Cheikhouna Gueye
import pygame


class Screen:
    """Create the Screen class"""

    def __init__(self, win):
        """Create instance varaibles need for the methods

        Parameters:
            win: A pygame windows object
        """
        self.win = win

        # string variables
        self.start = "PySnake"
        self.end = "Game Over"
        self.instruct = "Press space to start..."
        self.endInst = "Press R to close window"

        # color variables in rgb values
        self.purple = (128, 0, 128)
        self.black = (0, 0, 0)
        self.wht = (255, 255, 255)
        self.red = (128, 0, 0)

        # font variables
        self.fontScreen = pygame.font.SysFont(None, 100)
        self.fontInstruct = pygame.font.SysFont(None, 50)
        self.endFont = pygame.font.SysFont(None, 150)
        self.endInstructFont = pygame.font.SysFont(None, 50)

    def startScreen(self):
        """Create the start screen the player sees"""
        self.win.fill((0, 100, 0))
        pygame.draw.rect(self.win, (0, 50, 0), [0, 0, 700, 700], 65)
        startScreen = self.fontScreen.render(self.start, True, self.purple)
        self.win.blit(startScreen, [200, 200])
        startInst = self.fontInstruct.render(self.instruct, True, self.black)
        self.win.blit(startInst, [180, 500])

    def endScreen(self):
        """Create the "Game Over" screen"""
        self.win.fill((0, 100, 0))
        pygame.draw.rect(self.win, (0, 50, 0), [0, 0, 700, 700], 65)
        endScreen = self.endFont.render(self.end, True, self.red)
        self.win.blit(endScreen, [65, 280])

    def quit(self):
        """Gives user instruction on how to quit the game"""
        endInstruct = self.endInstructFont.render(self.endInst, True, self.wht)
        self.win.blit(endInstruct, [155, 500])
