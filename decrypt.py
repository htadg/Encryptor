import pin_generator


def decrypt(encrypted, date):
    msg = ""
    pin = pin_generator.generate(date)
    key = pin_generator.get_key(pin)
    hours = key[0]
    minutes = key[1]
    for c in range(0, len(encrypted), hours + 1):
        msg += chr(ord(encrypted[c]) - minutes)
    print msg
