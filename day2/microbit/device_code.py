from microbit import *

id_1 = 'arrival,123'
id_2 = 'arrival,456'

def send_sensor_data():
    # sensor data stream
    acc = accelerometer.get_values()
    
    # convert to comma separated string
    print(','.join(map(str, 
        [accelerometer.current_gesture(),
         acc[0], acc[1], acc[2],
         temperature(), compass.heading()])))

def receive_data():
    try:
        bytestring = uart.readline()
        if bytestring:
            display.show(str(bytestring))
    except:
        pass

while True:
    # arrivals
    if button_a.is_pressed():
        print(id_1)
    elif button_b.is_pressed():
        print(id_2)

    send_sensor_data()
    receive_data()

    sleep(100)