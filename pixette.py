import logging
import argparse

from lcd.window import Window
from server.app import create_app
from server.settings import DevConfig, ProdConfig

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.FileHandler("logs.log"), logging.StreamHandler()],
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Turn on debugging mode")
    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        config = DevConfig
    else:
        config = ProdConfig

    app = create_app(config)

    window = Window(debug=args.debug)
    window.run()