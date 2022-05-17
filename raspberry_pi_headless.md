# Setting up a Headless Raspberry Pi

Currently, PIXETTE works only on a legacy version of Raspbian:
* [Raspbian Lite 2017-11-2](https://downloads.raspberrypi.org/raspbian_lite/images/raspbian_lite-2017-12-01/)

## Enable SSH

```bash
/boot $ touch ssh
```

## Configure wireless network

```bash
# /boot/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
country=PL
update_config=1

network={
 ssid="<Name of your wireless LAN>"
 psk="<Password for your wireless LAN>"
}
```
