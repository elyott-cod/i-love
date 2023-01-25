input.onButtonPressed(Button.A, function () {
    music.setVolume(255)
    music.playMelody("E D G F B A C5 B ", 120)
})
input.onButtonPressed(Button.B, function () {
	
})
basic.showString("papa")
basic.pause(5000)
basic.showString("je")
basic.pause(5000)
basic.forever(function () {
    for (let index = 0; index < 3; index++) {
        basic.showIcon(IconNames.Heart)
    }
})
