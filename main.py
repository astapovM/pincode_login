from random import randint

def create_pin():
    pin = []
    for i in range(4):
        pin.append(randint(0,9))
    return pin

print(*create_pin())
