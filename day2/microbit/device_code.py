from microbit import *

# IOTA address is transmitted over serial
# (in real life this needs to be replaced with an ID lookup)
address = 'XQKBUNOERH9CJLLRQTNOLMWBJYUCGXORVNGEOEMBHNCPRVVBNSNNUOJMZODVUJXCOMMYXVLVNNJMBQMYX'
bad_address = '999999999999999999999999999999999999BADBADBADBADBAD'

while True:
    if button_a.is_pressed():
        print(address)
    elif button_b.is_pressed():
        print(bad_address)

    print(accelerometer.current_gesture(),
          accelerometer.get_values(), temperature(), compass.heading())
    sleep(100)