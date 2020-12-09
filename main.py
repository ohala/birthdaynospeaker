def on_bluetooth_connected():
    basic.show_string("C")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_string("D")
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    basic.show_number(5)
    basic.pause(1000)
    basic.show_number(4)
    basic.pause(1000)
    basic.show_number(3)
    basic.pause(1000)
    basic.show_number(2)
    basic.pause(1000)
    basic.show_number(1)
    music.set_built_in_speaker_enabled(True)
    basic.show_icon(IconNames.YES)
    for index in range(4):
        music.play_melody("C C G G A A G - ", 120)
        music.play_melody("F F E E D D C - ", 120)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_b():
    music.set_built_in_speaker_enabled(True)
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
music.set_built_in_speaker_enabled(False)
basic.show_icon(IconNames.NO)
bluetooth.start_accelerometer_service()
bluetooth.start_button_service()
bluetooth.start_io_pin_service()
bluetooth.start_led_service()
bluetooth.start_magnetometer_service()
bluetooth.start_temperature_service()

def on_forever():
    basic.show_leds("""
        . . # . .
        # . . . #
        . . # . .
        # . # . #
        # # # # #
        """)
    basic.show_leds("""
        # . . . #
        . . # . .
        . . # . .
        # . # . #
        # # # # #
        """)
basic.forever(on_forever)
