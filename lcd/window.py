import os

# Disable Pygame welcome message
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

from lcd import WINDOW_SIZE
from lcd.event_manager import EventManager


class Window:
    def __init__(self, debug: bool = False):
        self.debug = debug

        pygame.init()
        pygame.display.set_caption("Pixette")
        pygame.mouse.set_visible(False)

        if self.debug:
            self.screen = pygame.display.set_mode(WINDOW_SIZE)
        else:
            os.environ["SDL_VIDEODRIVER"] = "fbcon"
            os.environ["SDL_FBDEV"] = "/dev/fb1"

            self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.FULLSCREEN)

        self.event_manager = EventManager(self.screen)

    def run(self):
        self.event_manager.run_event_loop()