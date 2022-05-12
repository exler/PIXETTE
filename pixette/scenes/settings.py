import pygame
from pixette.constants import STANDARD_FONT, Colors
from pixette.scenes.base import Scene


class SettingsScene(Scene):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(STANDARD_FONT, 16)
        self.small_font = pygame.font.SysFont(STANDARD_FONT, 12)

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.up_text = self.small_font.render("Screen", True, Colors.WHITE)
        self.up_text_rect = self.up_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 44)
        )

    def draw(self, screen):
        screen.fill(Colors.BLACK)

        screen.blit(self.up_text, self.up_text_rect)
