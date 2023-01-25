def on_button_pressed_a():
    music.set_volume(255)
    music.play_melody("E D G F B A C5 B ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("papa")
basic.pause(5000)
basic.show_string("je")
basic.pause(5000)

def on_forever():
    for index in range(3):
        basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
