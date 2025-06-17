# L298 H Bridge Motor Driver
_Python Software for the L298 H Bridge Motor Driver._

![alt text](<README IMAGES/DROK DC Motor Driver.png>)
_A DROK DC Motor Driver with a L298 Dual H Bridge_

# Using the MotorDriver Class
At a minimum, we need 3 pins from a RaspberryPi not including the ground.

* A PWM Pin for controlling the Duty Cycle or "Speed" of the motors.
* Two other pins to control whether the motor goes forward or backward using a truth table configuration.

| IN1 PIN | IN2 PIN | OUTPUT |
| --- | --- | ------ |
| 1   | 0   | Forward Direction |
| 0   | 1   | Backward Direction |
| 1   | 1   | Short Circuits, Shutdowns both Motors |
| 0   | 0   | Graceful Shutdown |


```python
from time import sleep
from MotorDriver import MotorDriver

MOTOR_1_PWM_PINOUT = 18 ## ENA pin on the board.
IN1_PINOUT = 23
IN2_PINOUT = 24

motor1_controller = MotorDriver(MOTOR_1_PWM_PINOUT, IN1_PINOUT, IN2_PINOUT)

## Motor 1 moves backwards at 10% of its maximum speed.
motor1_controller.set_motor_speed(-10)
sleep(2)

## Motor 1 starts to slow down because it is not receiving a direction or speed at which to go to.
motor1_controller.set_motor_speed(0)
sleep(2)

## Motor 1 moves forward at 10% of its maximum speed.
motor1_controller.set_motor_speed(10)
sleep(2)

motor1_controller.set_motor_speed(0)
```