from pixette.scene import Scene
from pixette.constants import *

import pygame
import spotipy


class SpotifyScene(Scene):
    def __init__(self):
        self.font = pygame.font.Font(DATETIME_FONT, 16)

    def on_enter(self, previous_scene):
        super().on_enter(previous_scene)

        self.sp = spotipy.Spotify(
            auth_manager=self.application.config.spotify_auth_manager
        )

        self.spotify_logo = pygame.image.load(SPOTIFY_LOGO)
        self.spotify_logo_rect = self.spotify_logo.get_rect(
            center=(
                (self.application.width / 2) - 36,
                (self.application.height / 2) - 36,
            )
        )

        self.skip_back = pygame.image.load(SKIP_BACK)
        self.skip_back_rect = self.skip_back.get_rect(
            center=((self.application.width / 2) - 36, self.application.height / 2)
        )
        self.skip_forward = pygame.image.load(SKIP_FORWARD)
        self.skip_forward_rect = self.skip_forward.get_rect(
            center=((self.application.width / 2) + 36, self.application.height / 2)
        )
        self.pause = pygame.image.load(PAUSE)
        self.pause_rect = self.pause.get_rect(
            center=(self.application.width / 2, self.application.height / 2)
        )
        self.play = pygame.image.load(PLAY)
        self.play_rect = self.play.get_rect(
            center=(self.application.width / 2, self.application.height / 2)
        )

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill(Colors.BLACK)
        screen.blit(self.spotify_logo, self.spotify_logo_rect)
        screen.blit(self.skip_back, self.skip_back_rect)
        screen.blit(self.skip_forward, self.skip_forward_rect)
        # screen.blit(self.pause, self.pause_rect)
        screen.blit(self.play, self.play_rect)
