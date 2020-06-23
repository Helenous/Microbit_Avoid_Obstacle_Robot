from microbit import *
import radio
radio.config(channel=20)
radio.on()
radio.config(power=7)


while True:
    incoming = radio.receive()
    if incoming == "left":
        display.show(Image.ARROW_E)
        pin8.write_digital(1)
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_analog(200)
        sleep(100)
    elif incoming == "right":
        display.show(Image.ARROW_W)
        pin8.write_digital(0)
        pin12.write_analog(200)
        pin0.write_digital(1)
        pin16.write_digital(0)
    elif incoming == "forward":
        display.show(Image.ARROW_N)
        pin8.write_digital(1)
        pin12.write_digital(0)
        pin0.write_digital(1)
        pin16.write_digital(0)
        
    elif incoming == "reverse":
        display.show(Image.ARROW_S)
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin0.write_digital(0)
        pin16.write_digital(1)
        
    elif incoming == "stop":
        display.show(Image.ASLEEP)
        pin8.write_digital(0)
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_digital(0)
        

    
    
        
        

