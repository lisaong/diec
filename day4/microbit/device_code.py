# https://python.microbit.org/v/1.1
# Paste the following code

from microbit import *

def send_sensor_data():
    # sensor data stream
    acc = accelerometer.get_values()
    
    # convert to comma separated string
    print(','.join(map(str, 
        [button_a.is_pressed(), acc[0], acc[1], acc[2], compass.heading()])))

while True:
    send_sensor_data()

    sleep(100)