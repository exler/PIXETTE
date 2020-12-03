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
    BTN_LIST = [
        Pins.UP,
        Pins.DOWN,
        Pins.LEFT,
        Pins.RIGHT,
        Pins.KEY_A,
        Pins.KEY_B,
        Pins.KEY_C,
        Pins.PRESS,
    ]

    def __init__(
        self,
        debug: bool = False,
    ):
        self.debug = debug

        self._backlight = True

        if self.debug:
            logger.setLevel(logging.DEBUG)
        else:
            self.init_GPIO()

    def init_GPIO(self):
        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Buttons
        for btn in self.BTN_LIST:
            GPIO.setup(btn, GPIO.IN, GPIO.PUD_UP)

        # Backlight
        GPIO.setup(Pins.BACKLIGHT, GPIO.OUT)

    def keys(self, event=None):
        if event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    logging.debug("Backlight button pressed!")
        else:
            import RPi.GPIO as GPIO

            BACKLIGHT_BTN = GPIO.input(Pins.KEY_C)
            if not BACKLIGHT_BTN:
                if self._backlight:
                    GPIO.output(Pins.BACKLIGHT, 0)
                else:
                    GPIO.output(Pins.BACKLIGHT, 1)
                self._backlight = not self._backlight