import platform
import subprocess
from datetime import datetime

import pygame
from pixette.constants import ARROW_RIGHT, STANDARD_FONT, Colors
from pixette.scenes.base import Scene


class AdminScene(Scene):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(STANDARD_FONT, 16)
        self.small_font = pygame.font.Font(STANDARD_FONT, 14)

        self.arrow_right = pygame.image.load(ARROW_RIGHT)

        self.index = None
        self.max_index = 1

        self._update_ssh_status()
        self.last_check = datetime.now()

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.title_text = self.small_font.render("Admin", True, Colors.WHITE)
        self.title_text_rect = self.title_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 48)
        )

        self.reboot_text = self.font.render("Reboot", True, Colors.WHITE)
        self.reboot_text_rect = self.reboot_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) + 24)
        )

        self.application.device.up_btn.when_pressed = self.previous_index
        self.application.device.down_btn.when_pressed = self.next_index
        self.application.device.key_a.when_pressed = self.perform_operation

    def on_exit(self, next_scene):
        super().on_exit(next_scene)

        self.application.device.up_btn.when_pressed = None
        self.application.device.down_btn.when_pressed = None
        self.application.device.key_a.when_pressed = None

    def update(self, dt):
        now = datetime.now()
        if not self.last_check or (now - self.last_check).seconds > 60:
            self._update_ssh_status()
            self.last_check = now

    def draw(self, screen):
        screen.fill(Colors.BLACK)

        if self.ssh_enabled is None:
            self.ssh_text = self.font.render("SSH unavailable", True, Colors.RED)
        elif self.ssh_enabled:
            self.ssh_text = self.font.render("Disable SSH", True, Colors.WHITE)
        else:
            self.ssh_text = self.font.render("Enable SSH", True, Colors.WHITE)

        self.ssh_text_rect = self.ssh_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 8)
        )

        if self.index == 0:
            self.arrow_rect = self.arrow_right.get_rect(
                center=(
                    (self.application.width / 2) - (self.ssh_text.get_size()[0] / 2) - 12,
                    (self.application.height / 2) - 8,
                )
            )
            screen.blit(self.arrow_right, self.arrow_rect)
        elif self.index == 1:
            self.arrow_rect = self.arrow_right.get_rect(
                center=(
                    (self.application.width / 2) - (self.reboot_text.get_size()[0] / 2) - 12,
                    (self.application.height / 2) + 24,
                )
            )
            screen.blit(self.arrow_right, self.arrow_rect)

        screen.blit(self.title_text, self.title_text_rect)
        pygame.draw.line(screen, Colors.WHITE, (24, 28), (104, 28))
        screen.blit(self.ssh_text, self.ssh_text_rect)
        screen.blit(self.reboot_text, self.reboot_text_rect)

    def next_index(self):
        if self.index is None and self.ssh_enabled is None:
            self.index = 1
        elif self.index is None:
            self.index = 0
        elif self.index == self.max_index:
            if self.ssh_enabled is None:
                self.index = 1
            else:
                self.index = 0
        else:
            self.index += 1

    def previous_index(self):
        if self.index is None or self.index == 0:
            self.index = self.max_index
        else:
            if self.ssh_enabled is None and self.index - 1 == 0:
                self.index = self.max_index
            else:
                self.index -= 1

    def perform_operation(self):
        if self.index == 0:
            self._toggle_ssh()
        elif self.index == 1:
            self._reboot()

    def _update_ssh_status(self):
        if platform.system() == "Linux":
            output = subprocess.check_output(["service", "ssh", "status"])
            try:
                if str(output).find("active (running)") != -1:
                    self.ssh_enabled = True
                else:
                    self.ssh_enabled = False
            except subprocess.CalledProcessError:
                self.ssh_enabled = False
        else:
            self.ssh_enabled = None

    def _toggle_ssh(self):
        if platform.system() == "Linux":
            if self.ssh_enabled:
                subprocess.run(["sudo", "service", "ssh", "stop"])
            else:
                subprocess.run(["sudo", "service", "ssh", "start"])
            self.ssh_enabled = not self.ssh_enabled
        else:
            pass

    def _reboot(self):
        if platform.system() == "Linux":
            subprocess.run(["sudo", "reboot"])
        else:
            pass
