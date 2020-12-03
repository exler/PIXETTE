def toggle_backlight(backlight):
    if backlight.is_active:
        backlight.off()
    else:
        backlight.on()