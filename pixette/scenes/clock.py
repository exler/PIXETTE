from datetime import date, datetime

from pixette.scene import Scene
from pixette.constants import *

import pygame


class ClockScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font(DATETIME_FONT, 16)

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.logo = pygame.image.load(LOGO_LIGHT)
        self.logo_rect = self.logo.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 32)
        )

    def update(self, dt):
        self.now = datetime.now()

    def draw(self, screen):
        screen.fill(Colors.BLACK)
        date = self.font.render(self.now.strftime("%a, %d.%m.%Y"), True, Colors.WHITE)
        time = self.font.render(self.now.strftime("%H:%M:%S"), True, Colors.WHITE)
        date_rect = date.get_rect(
            center=(self.application.width / 2, self.application.height / 2)
        )
        time_rect = time.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) + 24)
        )

        screen.blit(self.logo, self.logo_rect)
        screen.blit(date, date_rect)
        screen.blit(time, time_rect)
