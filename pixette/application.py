import os
import logging

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

import pixette
from pixette.config import AppConfig


class Application:
    def __init__(
        self, config: AppConfig, title: str, resolution: tuple, update_rate: int
    ):
        self.config = config
        if not self.config.debug:
            os.environ["SDL_FBDEV"] = "/dev/fb1"
            os.environ["SDL_VIDEO_CENTERED"] = "1"

        pygame.init()
        pygame.mouse.set_visible(False)

        self._scene = None

        self.title = title
        self.resolution = resolution
        self.update_rate = update_rate

        logging.info(f"Pixette v{pixette.__version__}")

    @property
    def title(self):
        return pygame.display.get_caption()

    @title.setter
    def title(self, value):
        pygame.display.set_caption(value)

    @property
    def resolution(self):
        return self._screen.get_size()

    @resolution.setter
    def resolution(self, value):
        self._screen = pygame.display.set_mode(value)

    @property
    def width(self):
        return self.resolution[0]

    @property
    def height(self):
        return self.resolution[1]

    @property
    def active_scene(self):
        return self._scene

    def change_scene(self, scene):
        """
        Change the currently active scene.
        This will invoke `scene.on_exit` and `scene.on_enter` methods on the switching scenes.

        If ``None`` is provided, the application's execution will end.
        """
        if self.active_scene is not None:
            self.active_scene.on_exit(next_scene=scene)
            self.active_scene._application = None
        self._scene, old_scene = scene, self.active_scene
        if self.active_scene is not None:
            self.active_scene._application = self
            self.active_scene.on_enter(previous_scene=old_scene)

    def run(self, scene=None):
        """
        Execute the application at given scene.
        """
        if scene is None:
            if self.active_scene is None:
                raise ValueError("No scene provided")
        else:
            self.change_scene(scene)

        clock = pygame.time.Clock()

        while self.active_scene is not None:
            try:
                for event in pygame.event.get():
                    self.active_scene.handle_event(event)
                    if event.type == pygame.QUIT:
                        self.change_scene(None)  # trigger scene.on_exit()
                        return
                    self.config.keys(event)

                dt = clock.tick(self.update_rate)
                self.active_scene.update(dt)

                self.active_scene.draw(self._screen)
                pygame.display.update()
            except KeyboardInterrupt:
                logging.info("Shutting down")

                if self.config.debug:
                    import RPi.GPIO as GPIO

                    GPIO.cleanup()

                os.exit(0)
            except Exception as e:
                logging.exception(f"Caught exception: {e}", exc_info=True)

                if self.config.debug:
                    import RPi.GPIO as GPIO

                    GPIO.cleanup()

                os.exit(1)