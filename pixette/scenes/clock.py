from datetime import date, datetime

from pixette.scene import Scene
from pixette.constants import DATETIME_FONT, Colors

import pygame


class ClockScene(Scene):
    def __init__(self):
        self.datetime_font = pygame.font.Font(DATETIME_FONT, 16)
        self.now = datetime.now()

    def update(self, dt):
        self.now = datetime.now()

    def draw(self, screen):
        screen.fill(Colors.BLACK)
        date_text = self.datetime_font.render(
            self.now.strftime("%a, %d.%m.%Y"), True, Colors.WHITE
        )
        time_text = self.datetime_font.render(
            self.now.strftime("%H:%M:%S"), True, Colors.WHITE
        )
        date_text_rect = date_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 24)
        )
        time_text_rect = time_text.get_rect(
            center=(self.application.width / 2, self.application.height / 2)
        )
        screen.blit(date_text, date_text_rect)
        screen.blit(time_text, time_text_rect)
