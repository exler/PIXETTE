# Setting up a Headless Raspberry Pi

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

## Configure user

* Generate a password using OpenSSL
```bash
echo "mypassword" | openssl passwd -6 -stdin
```

* Create a file with username and password
```bash
# /boot/userconf.txt
username:password
```
