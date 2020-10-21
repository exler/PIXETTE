import logging

import pygame

from lcd.screens import LockScreen


class EventManager:
    def __init__(self, screen: pygame.Surface):
        self.screens = {"lockscreen": LockScreen(screen)}
        self.current_screen = self.screens["lockscreen"]
        self.current_screen.show()

    def run_event_loop(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            logging.info("KeyboardInterrupt detected, closing the event loop...")
