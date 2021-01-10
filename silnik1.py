import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Silnik():
    def __init__(self, EnaA, In1A, In2A, EnaB, In1B, In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnaB = EnaB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnaB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 100);
        self.pwmA.start(0);
        self.pwmB = GPIO.PWM(self.EnaB, 100);
        self.pwmB.start(0);

    def doprzodu(self, sterowanie, czas=0):

        wypel = int(sterowanie)
        self.pwmA.ChangeDutyCycle(wypel)
        self.pwmB.ChangeDutyCycle(wypel)
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)
        sleep(czas)
    def wlewo(self, sterowanie, czas=0):

        wypel = int(sterowanie)
        self.pwmA.ChangeDutyCycle(wypel)
        self.pwmB.ChangeDutyCycle(wypel)
        GPIO.output(self.In1A, GPIO.LOW)
        GPIO.output(self.In2A, GPIO.HIGH)
        GPIO.output(self.In1B, GPIO.LOW)
        GPIO.output(self.In2B, GPIO.HIGH)
        sleep(czas)

    def wprawo(self, sterowanie, czas=0):

        wypel = int(sterowanie)
        self.pwmA.ChangeDutyCycle(wypel)
        self.pwmB.ChangeDutyCycle(wypel)
        GPIO.output(self.In1A, GPIO.HIGH)
        GPIO.output(self.In2A, GPIO.LOW)
        GPIO.output(self.In1B, GPIO.HIGH)
        GPIO.output(self.In2B, GPIO.LOW)
        sleep(czas)

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0);
        self.pwmB.ChangeDutyCycle(0);
        sleep(t)

