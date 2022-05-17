<p align="center">
    <img src="pixette/assets/images/logo.png" width="256">
    <p align="center">📟 Time/weather/currency display using a Raspberry Pi Zero with Waveshare LCD HAT</p>
    <p align="center">
        <img src="https://img.shields.io/badge/-Raspberry%20Pi%20Zero%20W-black?style=flat-square&logo=raspberry%20pi&logoColor=C51A4A">
        <img src="https://img.shields.io/badge/python-3.5%2B-lightblue?style=flat-square&logo=python&logoColor=lightblue">
        <img src="https://img.shields.io/github/license/EXLER/pixette?style=flat-square">
        <img src="https://img.shields.io/github/repo-size/EXLER/pixette?style=flat-square">
    </p>
</p>

## Hardware

* Raspberry Pi Zero W
* [Waveshare 1.44 ST7735S LCD HAT](https://www.waveshare.com/wiki/1.44inch_LCD_HAT)

## Installation

1. Install system libraries
```bash
$ sudo apt install git cmake python3-pip python3-dev python3-pygame python3-gpiozero python3-requests libsdl2-dev libsdl2-ttf-dev
```

2. Enable SPI

Enable SPI in `Interfacing Options > SPI` in `raspi-config`

```bash
$ sudo raspi-config
```

3. Add the following lines to `/etc/modules`

```bash
spi-bcm2835
fbtft_device
```

4. Add the following lines to `/etc/modprobe.d/fbtft.conf`

```bash
options fbtft_device name=adafruit18_green gpios=reset:27,dc:25,cs:8,led:24 speed=40000000 bgr=1 fps=60 custom=1 height=128 width=128 rotate=90
```

5. Add the following lines to `/boot/config.txt`

```bash
dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4
hdmi_force_hotplug=1
hdmi_cvt=128 128 60 1 0 0 0
hdmi_group=2
hdmi_mode=1
hdmi_mode=87
display_rotate=0
```

6. Copy between `fb0` and `fb1`

```bash
$ git clone https://github.com/tasanakorn/rpi-fbcp
$ mkdir rpi-fbcp/build
$ cd rpi-fbcp/build/
$ cmake .. && make
$ sudo install fbcp /usr/local/bin/fbcp
```

To launch `fbcp` automatically at startup, add the following lines to `/etc/rc.local` before `exit 0`:
```bash
fbcp&
```

### Test the configuration

To test the Raspberry Pi framebuffer configuration use the [Linux Framebuffer Imageviewer](https://linux.die.net/man/1/fbi):
```bash
$ sudo apt install fbi
$ sudo fbi -T 2 -d /dev/fb1 image.png
```

## Usage

* Install requirements
```bash
$ pip install -r requirements.txt
```

* Run application with `sudo` (root access is necessary to modify the framebuffer).

```bash
$ sudo python3 -m pixette
```

* Add this to `/etc/rc.local` to run PIXETTE at startup:
```bash
$ cd /home/pi/pixette
$ sudo python3 -m pixette &
```

## License

`PIXETTE` is under the terms of the [MIT License](https://www.tldrlegal.com/l/mit), following all clarifications stated in the [license file](LICENSE).
