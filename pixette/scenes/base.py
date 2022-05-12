from abc import ABC
from typing import Optional


class Scene(ABC):
    def __init__(
        self,
        title: Optional[str] = None,
        resolution: Optional[tuple[int, int]] = None,
        update_rate: Optional[int] = None,
    ):
        self._application = None

        self.title = title
        self.resolution = resolution
        self.update_rate = update_rate

    @property
    def application(self):
        return self._application

    def draw(self, screen):
        """
        Override this with the scene drawing.

        :param screen: Screen to draw the scene on
        """
        pass

    def update(self, dt):
        """
        Override this with the scene update tick.

        :param dt: Time in milliseconds since the last update
        """
        pass

    def handle_event(self, event):
        """
        Override this to handle an event in the scene.

        All of `pygame` events are sent here, so filtering should be applied manually in the subclass.

        :param event: Event to handle
        """
        pass

    def on_enter(self, previous_scene):
        """
        Override this to initialize upon scene entering.

        The `application` property is initialized at this point.
        If you override this method and want to use class variables to change the application's settings,
        you must call `super().on_enter(previous_scenen)` in the subclass.

        :param previous_scene: Previous scene to run
        """
        for attr in ("title", "resolution", "update_rate"):
            value = getattr(self, attr)
            if value is not None:
                setattr(self.application, attr.lower(), value)

    def on_exit(self, next_scene):
        """
        Override this to deinitialize upon scene exiting.

        The `application` property is still initialized at this point.

        :param next_scene: Next scene to run
        """
        pass
