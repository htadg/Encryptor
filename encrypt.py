import pin_generator
import random
import datetime


def encrypt(msg):
    encrypted = ""
    msg = msg.upper()
    pin = pin_generator.generate(str(datetime.datetime.now()))
    hours, minutes = pin_generator.get_key(pin)
    for ind in range(0, len(msg)):
        encrypted += chr(ord(msg[ind]) + minutes)
        for c in range(0, hours):
            encrypted += chr(random.randrange(0, 255))
    pin = str(hours) + str(minutes)
    return encrypted
