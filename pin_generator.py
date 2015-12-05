

def generate(date):
    hr_index = date.index(" ") + 1
    hr_end = date.index(":")
    hours = int(date[hr_index:hr_end])
    min_index = hr_index + 3
    minutes = int(date[min_index:min_index + 2])
    pin = str(hours)+str(minutes)
    return pin


def get_key(pin):
    if len(pin) == 2:
        hours = int(pin[:1])
        minutes = int(pin[1:])
    elif len(pin) == 4:
        hours = int(pin[:2])
        minutes = int(pin[2:])
    else:
        hours = int(pin[:1])
        minutes = int(pin[1:])
    return [hours, minutes]
