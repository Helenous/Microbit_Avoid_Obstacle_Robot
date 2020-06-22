# Add your Python code here. E.g.
from microbit import *
import radio
radio.config(channel=20)
radio.on()
radio.config(power=7)

display.show(Image.HAPPY)
while True:
    gesture = accelerometer.current_gesture()
    print(gesture)
    if gesture == "left":
        display.show(Image.ARROW_W)
        radio.send('left')
    elif gesture == "right":
        display.show(Image.ARROW_E)
        radio.send('right')
    elif gesture == "up":
        display.show(Image.ARROW_N)
        radio.send('forward')
    elif gesture == "down":
        display.show(Image.ARROW_S)
        radio.send('reverse')
        
    elif button_a.was_pressed():
        display.show(Image.ASLEEP)
        radio.send('brakes')
        

