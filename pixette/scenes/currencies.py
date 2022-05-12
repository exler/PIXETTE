import pygame
import requests
from pixette.constants import DATETIME_FONT, Colors
from pixette.scenes.base import Scene


class NBPWebClient:
    CURRENT_EXCHANGE_RATE_URL = "http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/"

    def __init__(self) -> None:
        self.session = requests.Session()

    def get_exchange_rate(self, currency: str) -> float:
        """
        Gets latest exchange rate from `currency` to PLN.

        Args:
            - currency - ISO 4217 currency code
        """
        response = self.session.get(self.CURRENT_EXCHANGE_RATE_URL.format(table="A", code=currency))
        return response.json()["rates"][0]["mid"]


class CurrenciesScene(Scene):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(DATETIME_FONT, 16)
        self.small_font = pygame.font.SysFont(DATETIME_FONT, 12)

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.up_text = self.small_font.render("Screen", True, Colors.WHITE)
        self.up_text_rect = self.up_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 44)
        )

    def draw(self, screen):
        screen.fill(Colors.BLACK)

        screen.blit(self.up_text, self.up_text_rect)
