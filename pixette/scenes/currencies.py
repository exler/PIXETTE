from datetime import datetime

import pygame
import requests
from pixette.constants import STANDARD_FONT, Colors
from pixette.scenes.base import Scene


class NBPWebClient:
    CURRENT_EXCHANGE_RATE_URL = "http://api.nbp.pl/api/exchangerates/rates/{table}/{code}/"

    def __init__(self):
        self.session = requests.Session()

    def get_exchange_rate(self, currency):
        """
        Gets latest exchange rate from `currency` to PLN.

        Args:
            - currency - ISO 4217 currency code
        """
        response = self.session.get(self.CURRENT_EXCHANGE_RATE_URL.format(table="A", code=currency))
        return response.json()["rates"][0]["mid"]


class CurrenciesScene(Scene):
    def __init__(self, update_interval=3600):
        super().__init__()

        self.update_interval = update_interval

        self.font = pygame.font.Font(STANDARD_FONT, 16)

        self.nbp = NBPWebClient()
        self._update_currencies()
        self.last_check = datetime.now()

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.eur_text = self.font.render("EUR", True, Colors.WHITE)
        self.eur_text_rect = self.eur_text.get_rect(
            center=((self.application.width / 2) - 32, (self.application.height / 2) - 24)
        )

        self.usd_text = self.font.render("USD", True, Colors.WHITE)
        self.usd_text_rect = self.usd_text.get_rect(
            center=((self.application.width / 2) - 32, (self.application.height / 2) + 24)
        )

    def update(self, dt):
        now = datetime.now()
        if not self.last_check or (now - self.last_check).seconds > self.update_interval:
            self._update_currencies()
            self.last_check = now

    def draw(self, screen):
        screen.fill(Colors.BLACK)

        screen.blit(self.eur_text, self.eur_text_rect)
        screen.blit(self.usd_text, self.usd_text_rect)

        eur_value = self.font.render(str(self.exchange_rates["eur"]), True, Colors.WHITE)
        usd_value = self.font.render(str(self.exchange_rates["usd"]), True, Colors.WHITE)
        eur_value_rect = eur_value.get_rect(
            center=((self.application.width / 2) + 16, (self.application.height / 2) - 24)
        )
        usd_value_rect = usd_value.get_rect(
            center=((self.application.width / 2) + 16, (self.application.height / 2) + 24)
        )
        screen.blit(eur_value, eur_value_rect)
        screen.blit(usd_value, usd_value_rect)

    def _update_currencies(self):
        eur = self.nbp.get_exchange_rate("eur")
        usd = self.nbp.get_exchange_rate("usd")
        self.exchange_rates = {"eur": eur, "usd": usd}
