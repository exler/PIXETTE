from datetime import datetime

import pytz
import pygame

from lcd import WINDOW_HEIGHT, WINDOW_WIDTH
from lcd.colors import Colors


class Screen:
    """Base class for deriving screens from."""

    def show(self):
        raise NotImplementedError(
            "This screen has not yet implemented the `show` method."
        )


class LockScreen(Screen):
    """LockScreen shows current date and time."""

    def __init__(self, screen: pygame.Surface, timezone: str = "Europe/Warsaw"):
        self.screen = screen
        self.timezone = pytz.timezone(timezone)

        self.font = pygame.font.SysFont("monospace", 24)

    def show(self):
        now = datetime.now(tz=self.timezone)
        clock = self.font.render(now.strftime("%H:%M"), 1, Colors.BLACK)
        self.screen.blit(clock, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))