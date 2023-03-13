import time
import digitalio
import board
import usb_hid
from keycode_win_de import Keycode
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)
keyboard = Keyboard(usb_hid.devices)

btn1_pin = board.GP15
btn2_pin = board.GP14
btn3_pin = board.GP13


btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        print("button1 pressed")
        keyboard.press(Keycode.A)
        time.sleep(0.5)
        keyboard.release(Keycode.A)
        
    if btn2.value:
        print("button2 pressed")
        keyboard.press(Keycode.B)
        time.sleep(0.5)
        keyboard.release(Keycode.B)
    if btn3.value:
        print("button3 pressed")
        keyboard.press(Keycode.C)
        time.sleep(0.5)
        keyboard.release(Keycode.C)
        
time.sleep(0.1)  