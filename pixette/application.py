import logging
import os
from typing import Optional, Type

import pygame

from pixette.device import Device
from pixette.scenes.admin import AdminScene
from pixette.scenes.base import Scene
from pixette.scenes.clock import ClockScene
from pixette.scenes.currencies import CurrenciesScene
from pixette.scenes.weather import WeatherScene


class Application:
    def __init__(self, device: Device, title: str, resolution: tuple[int, int], update_rate: int, debug: bool = False):
        self.device = device
        if not debug:
            os.environ["SDL_FBDEV"] = "/dev/fb1"
            os.environ["SDL_VIDEO_CENTERED"] = "1"

        pygame.init()
        pygame.mouse.set_visible(False)

        self._scene = None
        self._screen = None

        self.title = title
        self.resolution = resolution
        self.update_rate = update_rate

        self.scenes = [ClockScene(), CurrenciesScene(), WeatherScene(lat=51.11, lon=17.04), AdminScene()]

        self.device.left_btn.when_pressed = self.previous_scene
        self.device.right_btn.when_pressed = self.next_scene

    @property
    def title(self) -> str:
        return pygame.display.get_caption()

    @title.setter
    def title(self, value: str) -> None:
        pygame.display.set_caption(value)

    @property
    def resolution(self) -> tuple[int, int]:
        return self._screen.get_size()

    @resolution.setter
    def resolution(self, value: tuple[int, int]) -> None:
        self._screen = pygame.display.set_mode(value)

    @property
    def width(self) -> int:
        return self.resolution[0]

    @property
    def height(self) -> int:
        return self.resolution[1]

    @property
    def active_scene(self) -> Optional[Scene]:
        return self._scene

    def next_scene(self) -> None:
        index = self.scenes.index(self.active_scene)
        if index == len(self.scenes) - 1:
            self.change_scene(self.scenes[0])
        else:
            self.change_scene(self.scenes[index + 1])

    def previous_scene(self) -> None:
        index = self.scenes.index(self.active_scene)
        if index == 0:
            self.change_scene(self.scenes[-1])
        else:
            self.change_scene(self.scenes[index - 1])

    def change_scene(self, scene: Scene) -> None:
        """
        Change the currently active scene.
        This will invoke `scene.on_exit` and `scene.on_enter` methods on the switching scenes.

        If `None` is provided, the application's execution will end.
        """
        if self.active_scene is not None:
            self.active_scene.on_exit(next_scene=scene)
            self.active_scene._application = None
        self._scene, old_scene = scene, self.active_scene
        if self.active_scene is not None:
            self.active_scene._application = self
            self.active_scene.on_enter(previous_scene=old_scene)

    def run(self, scene: Optional[Type[Scene]] = None) -> None:
        """
        Start the application at given scene.
        """
        if scene is not None:
            for s in self.scenes:
                if type(s) == scene:
                    self.change_scene(s)
                    break
        elif self.active_scene is not None:
            self.change_scene(scene)
        else:
            raise ValueError("No scene provided")

        clock = pygame.time.Clock()
        while self.active_scene is not None:
            try:
                for event in pygame.event.get():
                    self.active_scene.handle_event(event)
                    if event.type == pygame.QUIT:
                        self.change_scene(None)  # trigger scene.on_exit()
                        return
                    self.device.keys(event)

                dt = clock.tick(self.update_rate)
                self.active_scene.update(dt)
                self.active_scene.draw(self._screen)
                pygame.display.update()
            except KeyboardInterrupt:
                logging.info("Shutting down")
                break
            except Exception as e:
                logging.exception(f"Caught exception: {e}", exc_info=True)
                break
