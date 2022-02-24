import pygame
pygame.init()
from player import Player

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player()
        self.pressed = {}

