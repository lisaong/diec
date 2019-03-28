from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        display.show(Image.SAD)

    print(accelerometer.current_gesture(), accelerometer.get_values(), temperature())
    sleep(100)

display.clear()
