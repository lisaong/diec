from microbit import *

id_1 = 'arrival:123'
id_2 = 'arrival:456'

while True:
    # arrivals
    if button_a.is_pressed():
        print(id_1)
    elif button_b.is_pressed():
        print(id_2)

    # sensor data stream
    print(accelerometer.current_gesture(),
          accelerometer.get_values(), temperature(), compass.heading())
    sleep(100)