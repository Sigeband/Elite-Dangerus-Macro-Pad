# Macro-Pad
Control panel add-on for a keyboard.
This Project is Still WIP! Scroll Down for more information!


## Features
The clip-on "macro pad" is designed for the Roccat vulkan keyboard. Easily detachable, it clips right onto its back.

In addition to eight assignable buttons, there are six switches. Changes can be made to the GPIO pins, as well as the buttons' functions.

For those who are looking for a way to enhance their immersion in space games, like Elite Dangerous, this Small panel is perfect for you.




## Parts List
```
1x Raspery pi pico
8x 16mm momentary push buttons
6x toggle switches
1x 3D printed case 
2x M3x20 Screws+ Washers
```

3D modell: https://www.printables.com/de/model/458058-clip-on-button-panel


## Installing Circuit Python

```

1. First, you'll need to download the latest version of CircuitPython for Raspberry Pi Pico from the official website. You can find the download link here: https://circuitpython.org/board/raspberry_pi_pico/

2. Connect your Raspberry Pi Pico to your computer via USB cable.

3. Make sure that your Raspberry Pi Pico is in bootloader mode. You can enter bootloader mode by pressing and holding the BOOTSEL button while plugging in the USB cable.

4. Once your Raspberry Pi Pico is in bootloader mode, it will show up as a removable drive on your computer. Open the drive.

5. Delete the existing file named "main.py" if it exists in the drive.

5. Extract the CircuitPython .uf2 file that you downloaded earlier, and drag and drop the .uf2 file onto the removable drive of your Raspberry Pi Pico.

6. Wait for the .uf2 file to transfer onto the board. The transfer will take a few seconds.

7. Once the transfer is complete, your Raspberry Pi Pico will automatically reboot into CircuitPython. You will know that CircuitPython is running when you see a new drive named "CIRCUITPY" on your computer.

8. It looks like you just installed Cirucit Python!

9. Once the main.py file is dragged to the drive, install the libraries listed in the code. You can find more information about this in their documentation. 


```

For Wiring Youre just gonna wire one contact of the switch/button to +3.3 and the other one to the coresponding gpio pin.
The gpion pins in the programm are sorted like this if you look at the macropad from the front:

```
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
```

This is how mine currently looks:



![20230420_195754](https://user-images.githubusercontent.com/114338337/233449540-1ce50ddb-692f-4b4f-a85c-8c9ad3554959.jpg)




## Planned Features
```
Customizable Grid for putting names under/over the buttons (3D printed ofc)
Enclosure for cables, and modules that work via connectors on the side. ( So you can for example just ad a rotary encoder module for sound controls
An easyier way to adjust gpio pins and functions.

