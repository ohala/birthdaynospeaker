input.onButtonPressed(Button.A, function () {
    music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Forever)
})
input.onButtonPressed(Button.B, function () {
    music.setBuiltInSpeakerEnabled(true)
    basic.showIcon(IconNames.Yes)
})
basic.showIcon(IconNames.Heart)
music.setBuiltInSpeakerEnabled(false)
basic.showIcon(IconNames.No)
basic.forever(function () {
    basic.showLeds(`
        . . # . .
        # . . . #
        . . # . .
        # . # . #
        # # # # #
        `)
    basic.showLeds(`
        # . . . #
        . . . . .
        . . # . .
        # . # . #
        # # # # #
        `)
})
