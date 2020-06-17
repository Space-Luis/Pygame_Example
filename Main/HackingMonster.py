import pygame
import sys
import time
import random

from pygame.locals import *

Window_width = 800
Window_height = 600
White - (255, 255, 255)

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set.mode((Window_width, Window_height), 0, 32)
    pygame.display.set_caption("Hacking Monster")
    surface = pygame.Surface(window.get_size())
    surface = surface.convert()
    surface.fill(White)
    clock = pygame.time.Clock()
    pygame.key_set_repeat(1, 40)
    window.blit(surface, (0, 0))
    
