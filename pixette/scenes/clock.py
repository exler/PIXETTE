from datetime import date, datetime

from pixette.scene import Scene
from pixette.constants import *

import pygame


class ClockScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font(DATETIME_FONT, 16)
        self.small_font = pygame.font.SysFont(DATETIME_FONT, 12)

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.logo = pygame.image.load(LOGO_LIGHT)
        self.logo_rect = self.logo.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 26)
        )

        self.arrows_up = pygame.image.load(ARROWS_UP)
        self.arrows_up = pygame.transform.scale(self.arrows_up, (12, 12))
        self.arrows_up_rect = self.arrows_up.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 54)
        )
        self.up_text = self.small_font.render("Screen", True, Colors.WHITE)
        self.up_text_rect = self.up_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 44)
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
        # screen.blit(self.arrows_up, self.arrows_up_rect)
        # screen.blit(self.up_text, self.up_text_rect)
        screen.blit(date, date_rect)
        screen.blit(time, time_rect)
