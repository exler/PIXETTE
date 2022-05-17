import argparse
import logging

from pixette.application import Application
from pixette.device import Device
from pixette.scenes.clock import ClockScene
from pixette.utils import set_logging


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="turn on debugging mode")
    args = parser.parse_args()

    set_logging(level=(logging.DEBUG if args.debug else logging.INFO))

    device = Device(mock=args.debug)
    app = Application(device=device, title="PIXETTE", resolution=(128, 128), update_rate=60, debug=args.debug)
    app.run(scene=ClockScene)


if __name__ == "__main__":
    main()
