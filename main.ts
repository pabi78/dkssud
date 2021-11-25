input.onSound(DetectedSound.Loud, function () {
    strip.showRainbow(1, 360)
    strip.show()
    basic.pause(5000)
    for (let index = 0; index < 4; index++) {
        strip.rotate(5)
        strip.show()
        basic.pause(500)
    }
    strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    strip.show()
    basic.pause(100)
})
let strip: neopixel.Strip = null
strip = neopixel.create(DigitalPin.P13, 24, NeoPixelMode.RGB)
strip.setBrightness(255)
strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
strip.show()
basic.pause(100)
basic.forever(function () {
	
})
