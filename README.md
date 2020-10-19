<p align="center">
    <img src="pixette.png" width="224">
    <p align="center">🔳 Streaming camera with LCD live preview and web interface on a Raspberry Pi Zero W</P>
    <p align="center">
        <img src="https://img.shields.io/badge/-Raspberry%20Pi%20Zero%20W-black?style=flat-square&logo=raspberry%20pi&logoColor=C51A4A">
        <img src="https://img.shields.io/badge/python-3.8%2B-lightblue?style=flat-square&logo=python&logoColor=lightblue">
        <img src="https://img.shields.io/github/license/EXLER/pixette?style=flat-square">
        <img src="https://img.shields.io/github/repo-size/EXLER/pixette?style=flat-square">
    </p>
</p>

## Hardware

* Raspberry Pi Zero W
* [Waveshare 1.44 ST7735S LCD HAT](https://www.waveshare.com/wiki/1.44inch_LCD_HAT)

### Setup

* Enable SPI in `Interfacting Options > SPI` in `raspi-config`

```bash
$ sudo raspi-config
```

* Add the following lines to `/etc/modules`
```bash
# /etc/modules
spi-bcm2835
fbtft_device
```

* Add the following lines to `/etc/modprobe.d/fbtft.conf`
```bash
# /etc/modprobe.d/fbtft.conf
options fbtft_device name=adafruit18_green gpios=reset:27,dc:25,cs:8,led:24 speed=40000000 bgr=1 fps=60 custom=1 height=128 width=128 rotate=180
```

## Software

### Requirements

* Python >= 3.8

```bash
$ sudo apt install python3-pil python3-spidev python3-rpi.gpio
```

### Usage

## License

Copyright (c) 2020 by ***Kamil Marut***

`Pixette` is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file](LICENSE).