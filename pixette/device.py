import logging

import pygame
from gpiozero import LED, Button
from gpiozero import Device as GPIODevice
from gpiozero.pins.mock import MockFactory

from pixette.constants import Pins


class Device:
    def __init__(self, mock: bool = False) -> None:
        self.initialize_pins(mock=mock)

    def initialize_pins(self, mock: bool = False) -> None:
        if mock:
            GPIODevice.pin_factory = MockFactory()

        self.backlight = LED(Pins.BACKLIGHT)
        self.backlight.on()

        self.backlight_btn = Button(Pins.KEY_C)
        self.backlight_btn.when_pressed = self.toggle_backlight

        self.left_btn = Button(Pins.LEFT)
        self.right_btn = Button(Pins.RIGHT)

    def toggle_backlight(self) -> None:
        if self.backlight.is_active:
            self.backlight.off()
        else:
            self.backlight.on()

    def keys(self, event: pygame.event.Event) -> None:
        def press_button(button: Button) -> None:
            button.pin.drive_low()
            button.pin.drive_high()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                press_button(self.backlight_btn)
                logging.debug(f"Backlight is turned {'on' if self.backlight.is_active else 'off'}!")
            elif event.key == pygame.K_LEFT:
                press_button(self.left_btn)
            elif event.key == pygame.K_RIGHT:
                press_button(self.right_btn)
