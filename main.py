def on_button_pressed_a():
    music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
        MelodyOptions.FOREVER)
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
