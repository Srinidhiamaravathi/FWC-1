from machine import Pin
import time

led = Pin(15, Pin.OUT)

a = Pin(2, Pin.OUT)
b = Pin(3, Pin.OUT)
c = Pin(4, Pin.OUT)
d = Pin(5, Pin.OUT)
e = Pin(6, Pin.OUT)
f = Pin(7, Pin.OUT)
g = Pin(8, Pin.OUT)

minterms = [0, 1, 2]

def display_digit(num):
    digits = {
        0:(0,0,0,0,0,0,1),
        1:(1,0,0,1,1,1,1)
    }

    if num in digits:
        val = digits[num]
        a.value(val[0])
        b.value(val[1])
        c.value(val[2])
        d.value(val[3])
        e.value(val[4])
        f.value(val[5])
        g.value(val[6])

while True:
    for num in range(4):  

        if num in minterms:
            display_digit(1)
            led.value(1)
        else:
            display_digit(0)
            led.value(0)

        time.sleep(1)
