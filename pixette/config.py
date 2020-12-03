import logging

import pygame

from pixette.constants import Pins

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger()


class AppConfig:
    def __init__(
        self,
        debug: bool = False,
    ):
        self.debug = debug

        if self.debug:
            logger.setLevel(logging.DEBUG)
        else:
            self.init_GPIO()

    def init_GPIO(self):
        from gpiozero import Button, LED

        self.backlight = LED(Pins.BACKLIGHT)

        backlight_button = Button(Pins.KEY_C)
        backlight_button.when_pressed = self._toggle_backlight

    def keys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                logging.debug("Backlight button pressed!")

    def _toggle_backlight(self):
        if self.backlight.is_active:
            self.backlight.off()
        else:
            self.backlight.on()