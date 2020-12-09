bluetooth.onBluetoothConnected(function () {
    basic.showString("C")
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showString("D")
})
input.onButtonPressed(Button.A, function () {
    basic.showString("A")
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showNumber(5)
    basic.pause(1000)
    basic.showNumber(4)
    basic.pause(1000)
    basic.showNumber(3)
    basic.pause(1000)
    basic.showNumber(2)
    basic.pause(1000)
    basic.showNumber(1)
    music.setBuiltInSpeakerEnabled(true)
    basic.showIcon(IconNames.Yes)
    for (let index = 0; index < 4; index++) {
        music.playMelody("C C G G A A G - ", 120)
        music.playMelody("F F E E D D C - ", 120)
    }
})
input.onButtonPressed(Button.B, function () {
    music.setBuiltInSpeakerEnabled(true)
    basic.showIcon(IconNames.Yes)
})
basic.showIcon(IconNames.Heart)
music.setBuiltInSpeakerEnabled(false)
basic.showIcon(IconNames.No)
bluetooth.startAccelerometerService()
bluetooth.startButtonService()
bluetooth.startLEDService()
bluetooth.startIOPinService()
bluetooth.startTemperatureService()
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
        . . # . .
        . . # . .
        # . # . #
        # # # # #
        `)
})
