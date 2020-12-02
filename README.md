<p align="center">
    <img src="pixette/assets/images/logo.png" width="224">
    <p align="center">📟 Clock and Spotify controller on a Raspberry Pi Zero LCD HAT</p>
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

* Add the following lines to `/boot/config.txt`
```bash
# /boot/config.txt
dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4
hdmi_force_hotplug=1
hdmi_cvt=128 128 60 1 0 0 0
hdmi_group=2
hdmi_mode=1
hdmi_mode=87
display_rotate=1
```

* Synchroneous copy between `fb0` and `fb1`  
If you want to display console on the screen you will need to use `fbcp`:

```bash
$ sudo apt install git cmake
$ git clone https://github.com/tasanakorn/rpi-fbcp
$ mkdir rpi-fbcp/build
$ cd rpi-fbcp/build/
$ cmake .. && make
$ sudo install fbcp /usr/local/bin/fbcp
```

* Launch `fbcp` automatically at startup  
Add the following lines to `/etc/modprobe.d/fbtft.conf` before `exit 0`:
```bash
fbcp&
```

## Software

### Requirements

* Python >= 3.8

```bash
$ sudo apt install python3-rpi.gpio python3-pygame
```

### Usage
You need root access to modify the framebuffer!

## License

Copyright (c) 2020 by ***Kamil Marut***

`Pixette` is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file](LICENSE).