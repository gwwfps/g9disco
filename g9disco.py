import random
import time

import usb.core

def set_color(dev, r, g, b):
    msg = bytearray()
    msg.append(0x10)
    msg.append(0x00)
    msg.append(0x80)
    msg.append(0x57)
    msg.append(r)
    msg.append(g)
    msg.append(b)  
    dev.ctrl_transfer(0x34, 0x9, 0x210, 0x01, msg)

def main():
    dev = usb.core.find(idVendor=0x046d, idProduct=0xc066)
    if dev is None:
        dev = usb.core.find(idVendor=0x046d, idProduct=0xc048)

    if dev is None:
        raise ValueError('Could not find a connected G9 or G9X.')

    while True:
        r = random.randint(0, 2) * 127
        g = random.randint(0, 2) * 127
        b = random.randint(0, 2) * 127
        set_color(dev, r, g, b)
        time.sleep(1)
    
if __name__ == "__main__":
    main()