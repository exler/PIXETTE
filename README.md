<p align="center">
    <img src="pixette/assets/images/logo.png" width="256">
    <p align="center">📟 Time/weather/currency display using a Raspberry Pi Zero with Waveshare LCD HAT</p>
    <p align="center">
        <img src="https://img.shields.io/badge/-Raspberry%20Pi%20Zero%20W-black?style=flat-square&logo=raspberry%20pi&logoColor=C51A4A">
        <img src="https://img.shields.io/badge/python-3.9%2B-lightblue?style=flat-square&logo=python&logoColor=lightblue">
        <img src="https://img.shields.io/github/license/EXLER/pixette?style=flat-square">
        <img src="https://img.shields.io/github/repo-size/EXLER/pixette?style=flat-square">
    </p>
</p>

## Hardware

* Raspberry Pi Zero W
* [Waveshare 1.44 ST7735S LCD HAT](https://www.waveshare.com/wiki/1.44inch_LCD_HAT)

## Installation

1. Install BCM2835 libraries
```bash
$ wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.68.tar.gz
$ tar zxvf bcm2835-1.68.tar.gz 
$ cd bcm2835-1.68/
$ sudo ./configure && sudo make && sudo make check && sudo make install
```

2. Install system libraries
```bash
$ sudo apt install git cmake python3-pip python3-dev python3-pygame python3-gpiozero python3-numpy libsdl2-dev libsdl2-image-dev libjpeg-dev libsdl2-ttf-dev libfreetype6-dev libsdl2-mixer-dev libportmidi-dev
```

3. Update `/boot/config.txt`
```bash
# Comment the following lines
dtoverlay=vc4-fkms-v3d
max_framebuffers=2

# Add the following line at the end of the file
hdmi_force_hotplug=1
hdmi_cvt=300 300 60 1 0 0 0
hdmi_group=2
hdmi_mode=87
display_rotate=0
gpio=6,19,5,26,13,21,20,16=pu
```

4. Setup FBCP
```
$ git clone https://github.com/EngineerWill/waveshare_fbcp
$ cd waveshare_fbcp
$ mkdir build
$ cd build
$ cmake -DSPI_BUS_CLOCK_DIVISOR=20 -DWAVESHARE_1INCH44_LCD_HAT=ON -DBACKLIGHT_CONTROL=ON -DSTATISTICS=0 ..
$ make -j
$ sudo cp ~/waveshare_fbcp/build/fbcp /usr/local/bin/fbcp
$ sudo nano /etc/rc.local

# Add this before exit 0
fbcp&
```

### Test the configuration

To test the Raspberry Pi framebuffer configuration use the [Linux Framebuffer Imageviewer](https://linux.die.net/man/1/fbi):
```bash
$ sudo apt install fbi
$ sudo fbi -T 2 -d /dev/fb0 image.png
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
