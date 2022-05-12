import pygame
from pixette.constants import ARROWS_UP, DATETIME_FONT, Colors
from pixette.scenes.base import Scene


class SettingsScene(Scene):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(DATETIME_FONT, 16)
        self.small_font = pygame.font.SysFont(DATETIME_FONT, 12)

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.arrows_up = pygame.image.load(ARROWS_UP)
        self.arrows_up = pygame.transform.scale(self.arrows_up, (12, 12))
        self.arrows_up_rect = self.arrows_up.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 54)
        )
        self.up_text = self.small_font.render("Screen", True, Colors.WHITE)
        self.up_text_rect = self.up_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 44)
        )

    def draw(self, screen):
        screen.fill(Colors.BLACK)

        screen.blit(self.arrows_up, self.arrows_up_rect)
        screen.blit(self.up_text, self.up_text_rect)
