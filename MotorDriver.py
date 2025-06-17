import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class MotorDriver:
    def __init__(self, pwm_pin, forward_direction_pin, backward_direction_pin):
        GPIO.setup([pwm_pin, forward_direction_pin, backward_direction_pin], GPIO.OUT)
        self.pwm_controller = GPIO.PWM(pwm_pin, 1000) ## 1kHz

        self.forward_pin = forward_direction_pin
        self.backward_pin = backward_direction_pin
        self.pwm_controller.start(0)
    
    def forward(self, speed):
        GPIO.output(self.forward_pin, GPIO.HIGH)
        GPIO.output(self.backward_pin, GPIO.LOW)
        self.pwm_controller.ChangeDutyCycle(speed)
    
    def backward(self, speed):
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.HIGH)
        self.pwm_controller.ChangeDutyCycle(speed)
    
    def stop(self):
        self.pwm_controller.ChangeDutyCycle(0)
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.LOW)
    
    def cleanup(self):
        self.pwm_controller.stop()
        GPIO.cleanup()
    
    def set_motor_speed(self, speed):
        speed = max(-100, min(100, speed)) ## Clamps the speed to [-100, 100]
        if speed > 0:
            self.forward(speed)
        elif speed < 0:
            self.backward(-speed)
        else:
            self.stop()