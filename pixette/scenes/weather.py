from datetime import datetime

import pygame
import requests
from pixette.constants import STANDARD_FONT, Colors
from pixette.scenes.base import Scene

WEATHER_CODES = {
    (0,): "clear sky",
    (1,): "mainly clear",
    (2,): "partly cloudy",
    (3,): "overcast",
    (45, 48): "fog",
    (51, 53, 55): "drizzle",
    (56, 57): "freezing drizzle",
    (61, 63, 65): "rain",
    (66, 67): "freezing rain",
    (71, 73, 75): "snow fall",
    (77,): "snow grains",
    (80, 81, 82): "rain showers",
    (85, 86): "snow showers",
    (95, 96, 99): "thunderstorm",
}


class WeatherData:
    def __init__(self, temperature, weather_code):
        self.temperature = temperature
        self.weather_code = weather_code

    @property
    def weather(self):
        for k, v in WEATHER_CODES.items():
            if self.weather_code in k:
                return v


class OpenMeteoAPIClient:
    FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self):
        self.session = requests.Session()

    def get_current_weather(self, lat, lon):
        response = self.session.get(
            self.FORECAST_URL, params={"latitude": lat, "longitude": lon, "current_weather": True}
        )
        current_weather = response.json().get("current_weather")
        return WeatherData(
            temperature=current_weather.get("temperature"),
            weather_code=current_weather.get("weathercode"),
        )


class WeatherScene(Scene):
    def __init__(self, lat, lon, update_interval=3600):
        super().__init__()

        self.latitude = lat
        self.longitude = lon

        self.update_interval = update_interval

        self.font = pygame.font.Font(STANDARD_FONT, 16)
        self.small_font = pygame.font.Font(STANDARD_FONT, 14)

        self.open_meteo = OpenMeteoAPIClient()
        self.last_check = None

    def update(self, dt):
        now = datetime.now()
        if not self.last_check or (now - self.last_check).seconds > self.update_interval:
            self._update_weather()
            self.last_check = now

    def draw(self, screen):
        screen.fill(Colors.BLACK)

        self.temp_text = self.font.render("%.0f DEG C" % self.weather_data.temperature, True, Colors.WHITE)
        self.temp_text_rect = self.temp_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) + 16)
        )

        self.weather_text = self.font.render(self.weather_data.weather, True, Colors.WHITE)
        self.weather_text_rect = self.weather_text.get_rect(
            center=(self.application.width / 2, (self.application.height / 2) - 16)
        )
        screen.blit(self.temp_text, self.temp_text_rect)
        screen.blit(self.weather_text, self.weather_text_rect)

    def _update_weather(self):
        self.weather_data = self.open_meteo.get_current_weather(self.latitude, self.longitude)
