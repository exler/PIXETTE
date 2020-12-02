import logging

from spotipy.oauth2 import SpotifyOAuth

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
        spotify_client_id: str,
        spotify_client_secret: str,
        spotify_redirect_uri: str = "http://localhost",
        debug: bool = False,
    ):
        self.debug = debug

        if self.debug:
            logger.setLevel(logging.DEBUG)

        self.spotify_auth_manager = SpotifyOAuth(
            client_id=spotify_client_id,
            client_secret=spotify_client_secret,
            redirect_uri=spotify_redirect_uri,
            scope="app-remote-control",
        )
