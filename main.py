import time
import digitalio
import board
import usb_hid
from analogio import AnalogIn
from keycode_win_de import Keycode
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayout(keyboard)
keyboard = Keyboard(usb_hid.devices)

btn1_pin = board.GP0
btn2_pin = board.GP1
switch3_pin = board.GP2
switch4_pin = board.GP3
switch5_pin = board.GP4

btn6_pin = board.GP5
btn7_pin = board.GP6
switch8_pin = board.GP7
switch9_pin = board.GP8
switch10_pin = board.GP9

btn11_pin = board.GP10
btn12_pin = board.GP11
btn13_pin = board.GP12
btn14_pin = board.GP13


btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

switch3 = digitalio.DigitalInOut(switch3_pin)
switch3.direction = digitalio.Direction.INPUT
switch3.pull = digitalio.Pull.DOWN
prev_state3 = switch3.value

switch4 = digitalio.DigitalInOut(switch4_pin)
switch4.direction = digitalio.Direction.INPUT
switch4.pull = digitalio.Pull.DOWN
prev_state4 = switch4.value

switch5 = digitalio.DigitalInOut(switch5_pin)
switch5.direction = digitalio.Direction.INPUT
switch5.pull = digitalio.Pull.DOWN
prev_state5 = switch5.value

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

switch8 = digitalio.DigitalInOut(switch8_pin)
switch8.direction = digitalio.Direction.INPUT
switch8.pull = digitalio.Pull.DOWN
prev_state8 = switch8.value

switch9 = digitalio.DigitalInOut(switch9_pin)
switch9.direction = digitalio.Direction.INPUT
switch9.pull = digitalio.Pull.DOWN
prev_state9 = switch9.value

switch10 = digitalio.DigitalInOut(switch10_pin)
switch10.direction = digitalio.Direction.INPUT
switch10.pull = digitalio.Pull.DOWN
prev_state10 = switch10.value

btn11 = digitalio.DigitalInOut(btn11_pin)
btn11.direction = digitalio.Direction.INPUT
btn11.pull = digitalio.Pull.DOWN

btn12 = digitalio.DigitalInOut(btn12_pin)
btn12.direction = digitalio.Direction.INPUT
btn12.pull = digitalio.Pull.DOWN

btn13 = digitalio.DigitalInOut(btn13_pin)
btn13.direction = digitalio.Direction.INPUT
btn13.pull = digitalio.Pull.DOWN

btn14 = digitalio.DigitalInOut(btn14_pin)
btn14.direction = digitalio.Direction.INPUT
btn14.pull = digitalio.Pull.DOWN




READ_TIME = .001


while True:
    cur_state3 = switch3.value
    cur_state4 = switch4.value
    cur_state5 = switch5.value
    cur_state8 = switch8.value
    cur_state9 = switch9.value
    cur_state10 = switch10.value
    
    if btn1.value:
        print("button1 pressed")
        keyboard.press(Keycode.V)
        time.sleep(0.3)
        keyboard.release(Keycode.V)
        
    if btn2.value:
        print("button2 pressed")
        keyboard.press(Keycode.B)
        time.sleep(0.3)
        keyboard.release(Keycode.B)
 
    if cur_state3 != prev_state3:
        print("switch3 pressed")
        keyboard.press(Keycode.B)
        time.sleep(0.3)
        keyboard.release(Keycode.B)
        prev_state3 = switch3.value
        
    if cur_state4 != prev_state4:
        print("switch4 pressed")
        keyboard.press(Keycode.L)
        time.sleep(0.3)
        keyboard.release(Keycode.L)
        prev_state4 = switch4.value
        
    if cur_state5 != prev_state5:
        print("switch5 pressed")
        keyboard.press(Keycode.U)
        time.sleep(0.3)
        keyboard.release(Keycode.U)
        prev_state5 = switch5.value
        
    if btn6.value:
        print("button6 pressed")
        keyboard.press(Keycode.F)
        time.sleep(0.3)
        keyboard.release(Keycode.F)
        
    if btn7.value:
        print("button7 pressed")
        keyboard.press(Keycode.G)
        time.sleep(0.3)
        keyboard.release(Keycode.G)
        
    if cur_state8 != prev_state8:
        print("switch8 pressed")
        keyboard.press(Keycode.H)
        time.sleep(0.3)
        keyboard.release(Keycode.H)
        prev_state8 = switch8.value
        
    if cur_state9 != prev_state9:
        print("switch9 pressed")
        keyboard.press(Keycode.I)
        time.sleep(0.3)
        keyboard.release(Keycode.I)
        prev_state9 = switch9.value
        
    if cur_state10 != prev_state10:
        print("switch10 pressed")
        keyboard.press(Keycode.K)
        time.sleep(0.3)
        keyboard.release(Keycode.K)
        prev_state10 = switch10.value
        
    if btn11.value:
        print("button7 pressed")
        keyboard.press(Keycode.J)
        time.sleep(0.3)
        keyboard.release(Keycode.J)
        
    if btn12.value:
        print("button7 pressed")
        keyboard.press(Keycode.I)
        time.sleep(0.3)
        keyboard.release(Keycode.I)
        
    if btn13.value:
        print("button7 pressed")
        keyboard.press(Keycode.X)
        time.sleep(0.3)
        keyboard.release(Keycode.X)
        
    if btn14.value:
        print("button7 pressed")
        keyboard.press(Keycode.Ö)
        time.sleep(0.3)
        keyboard.release(Keycode.Ö)
        
    
#time.sleep(0.1)