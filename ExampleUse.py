import time
from MotorDriver import MotorDriver

MOTOR_1_PWM_PINOUT = 18 ## PWM for the first Motor (ENA)
IN1_PINOUT = 23 ## Forwards Direction
IN2_PINOUT = 24 ## Backwards Direction

MOTOR_2_PWM_PINOUT = 19 ## PWM for the second Motor (ENB)
IN3_PINOUT = 5 ## Forwards Direction
IN4_PINOUT = 6 ## Backwards Direction

motor1_controller = MotorDriver(MOTOR_1_PWM_PINOUT, IN1_PINOUT, IN2_PINOUT)
motor2_controller = MotorDriver(MOTOR_2_PWM_PINOUT, IN3_PINOUT, IN4_PINOUT)

## Backwards direction at 10% speed.
motor1_controller.set_motor_speed(-10)
motor2_controller.set_motor_speed(-10)
time.sleep(2)

## Stops both motors.
motor1_controller.set_motor_speed(0)
motor2_controller.set_motor_speed(0)
time.sleep(2)

## Forwards direction at 10% speed.
motor1_controller.set_motor_speed(10)
motor2_controller.set_motor_speed(10)
time.sleep(2)

motor1_controller.set_motor_speed(0)
motor2_controller.set_motor_speed(0)