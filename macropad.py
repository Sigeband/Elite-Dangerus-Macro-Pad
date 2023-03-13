import time
import digitalio
import board
import usb_hid
from keycode_win_de import Keycode
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)

btn1_pin = board.GP15

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("button pressed")
        keyboard.press(Keycode.D)
        time.sleep(0.5)
        keyboard.release(Keycode.D)
        
time.sleep(0.1)   