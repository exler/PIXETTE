import logging


def set_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="[%(asctime)s] [PIXETTE] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )
