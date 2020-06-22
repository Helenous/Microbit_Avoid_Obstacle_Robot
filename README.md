# Microbit Robot powered by L9110S

![robot](https://github.com/Helenous/Microbit_Robot/blob/master/Images/Robot.png)

<img src= "images/robot.png" width=800>


### Table of Contents

- [Description](#description)
- [Assembling The Robot](#assembling-the-robot)
- [Understand how motor works](#understand-how-motor-works)
- [Make robot turn left and right](#make-robot-turn-left-and-right)
- [Make robot move forward and backward](#make-robot-move-forward-and-backward)
- [How to Stop Motor](#how-to-stop-motor)
- [Changing speed of the motor](#changing-speed-of-the-motor)
- [Radio control using accelerometer](#radio-control-using-accelerometer)
- [Avoid Obstacle](#avoid-obstacle)
- [Components](#components)
- [Author Info](#author-info)

# Description
Build a robot powered by a Microbit that will move and avoid obstacles.

# Assembling the Robot

cf pdf file in Assembling Instruction folder

[Back To The Top](#Microbit-Robot-powered-by-L9110S)

# Understand how motor works

To control the motors, we need to access the pins of the microbit . We do this though Edge connector and the motor driver L9110s.

Each motor has two pins connected to it. 
Right motor: Pin 8, Pin 12
Left motor: Pin 0, Pin 16 

<pre>
Edge connector & L9110s:
Right Motor: A-1A ---> pin8 of the edge connector
Right Motor: A-1B ---> pin12 of the edge connector

Left Motor: B-1A ---> pin0 of the edge connector
Left Motor: B-1A ---> pin16 of the edge connector
</pre>

The simplest way to make the motors move is to set one pin to HIGH (1)and the the other pin to LOW(0) (to move full speed forwards). We do this by sending power to the respective GPIO pins using write_digital. 
 
In Python, move left motor Forwards: 
> pin0.write_digital(1) 
> pin16.write_digital(0)

To move the motor at full speed in reverse, we change which pin is 0 (Low) and 1 (High). 
Move left motor Reverse:
> pin0.write_digital(0) 
> pin16.write_digital(1) 

[Back To The Top](#Microbit-Robot-powered-by-L9110S)

## Make robot turn left and right
To turn the robot left we need to tell one motor to go forward, and the other to go backwards. 

Motor A is the right motor and it’s connected to pins 8 and 12. 
Motor B is the left motor and is connected to pins 0 and 16.  

So to turn the robot left, motor A needs to go forwards and motor B backwards. 
> pin8.write_digital(1)
> pin12.write_digital(0)
> pin0.write_digital(0)
> pin16.write_digital(1)

The code to turn the robot right is a reverse of what we set for turning left. 
> pin8.write_digital(0)
> pin12.write_digital(1)
> pin0.write_digital(1)
> pin16.write_digital(0)

## Make robot move forward and backward
To move robot forward, both motors need to go forward:
> pin8.write_digital(1)
> pin12.write_digital(0)
> pin0.write_digital(1)
> pin16.write_digital(0)

To move robot backward, both motors need to go backward:
> pin8.write_digital(0)
> pin12.write_digital(1)
> pin0.write_digital(0)
> pin16.write_digital(1)

## How to Stop motor
We will need to set all of the GPIO pins connected to the motors to off:
> pin8.write_digital(0)
> pin12.write_digital(0)
> pin0.write_digital(0)
> pin16.write_digital(0)

[Back To The Top](#Microbit-Robot-powered-by-L9110S)

# Changing speed of the motor

If we want to change the speed of a motor, so that it is not going at full speed all the time, we need to use PWM (Pulse Width Modulation). This is a means of changing the amount of power given to the motor by switching it on and off very fast. 

The percentage value of PWM determines the amount of each cycle that the output is ON. So a percentage of 100% is the same as being on all the time. A percentage of 50% would mean that the motor is only energised half the time, so it will go much slower. Note that the actual speed of the motor is not the same as the percentage of PWM – the motor won’t turn at all if the PWM value is too low and you will also get some stuttering at certain values. Nevertheless, being able to change the speed makes for a much better robot.

To change the PWM value of a pin, we must use the analog_write commands. These can be set to a value between 0 (always off) to 1023 (always on), so 50% would be 511.(which half of 1023)
Here are the commands to change the speed of the Right motor to approx 50% (value is 511)
Move right motor forwards at 50%
> pin8.write_analog(511)
> pin12.write_digital(0)
 
Move right motor Reverse at 50%
Doing this for the motors moving in reverse is a little different. We need to change the second pin to 1 for reverse. We then simply take the number (512) in this case) away from 1023, giving 512:
> pin8.write_analog(512)
> pin12.write_digital(1)

[Back To The Top](#Microbit-Robot-powered-by-L9110S)

# Radio Control using Accelerometer 
**Project 1**

Now you understand how the motors work, we are now going to use a radio link to connect two Microbits which enabled strings of data to be sent between devices. We will also use the accelerometer feature of the Microbit.

For this tutorial, you’ll need two micro:bits. Our robot will be controlled by micro:bit 1 that will read data from the built-in accelerometer and communicate the information to micro:bit 2  attached to our robot. We will code all of this project in MicroPython, using the Python editor for microbit, on the Microbit.org website.

1. Coding the controller - Microbit #1

The Python code can be found in the Microbit Robot folder

2. Coding the Robot - Microbit #2

The Python code can be found in the Microbit Robot folder

# Avoid Obstacle 
**Project 2**

1 x Microbit
The Python code can be found in the Microbit Robot folder

[Back To The Top](#Microbit-Robot-powered-by-L9110S)

# Components 
**What you will need**
- Microbit
- Microbit Edge Connector
- Motor Driver L1190S
- Ultrasonic Sensor
- Wooden Robot Chassis
- Gear Motors
- Wheels
- Caster wheel
- Jumper wires
- Mini Breadboard
- Battery pack
- Screws

[Back To The Top](#Microbit-Robot-powered-by-L9110S)

## Author Info

- Twitter - [@girlsintocoding](https://twitter.com/girlsintocoding)
- Website - [Girls Into Coding](https://girlsintocoding.com)

[Back To The Top](#Microbit-Robot-powered-by-L9110S)
