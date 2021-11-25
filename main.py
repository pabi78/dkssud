def on_sound_loud():
    strip.show_rainbow(1, 360)
    strip.show()
    basic.pause(5000)
    for index in range(4):
        strip.rotate(5)
        strip.show()
        basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    strip.show()
    basic.pause(100)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P13, 24, NeoPixelMode.RGB)
strip.set_brightness(255)
strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
strip.show()
basic.pause(100)

def on_forever():
    pass
basic.forever(on_forever)

