import argparse

import pixette
from pixette.config import AppConfig
from pixette.application import Application
from pixette.scenes.clock import ClockScene


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=pixette.__version__,
        help="show program version and exit",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="turn on debugging mode"
    )
    args = parser.parse_args()

    config = AppConfig(debug=args.debug)
    app = Application(
        config=config, title="Pixette", resolution=(128, 128), update_rate=4
    )
    app.run(ClockScene())