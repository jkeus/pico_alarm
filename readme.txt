Source code and libraries:

main.py
i2c_scan.py
led_test.py
lcd_api.py
pico_i2c_lcd.py
Ds1302.py

Other files needed:

RPI_PICO_W-20231005-v1.21.0.uf2 (grab this from official raberry pico documentation, most recent version)
Thonny-4.1.4.exe (get this from offical thonny website)


Quick start guide:

1. Install Thonny
2. Hold down the boot reset button on pico then plug it into the computers USB
3. Install the .uf2 file from the Raspberry Pi's doc
4. Drag the file onto the new drive on your PC
5. Find the device in Thonny
6. Make sure to uplaod main.py and all other .py files while in Thonny
6. Run the i2c_scan file to see the address and fill it into main.py before running

Our pin layout:
Buttons:
⦁	Buttons 1-4 go to pins 9-12(gp6--gp9)
⦁	Buttons also need power on other side
⦁	For our build we decided to use a side strip connected to the 3V3(OUT) pin 36

Screen:
⦁	SDA >> pin 1 (gp0), SCL >> pin 2 (gp1)
⦁	Voltage must come from a 5V src per supplier instructions. Either pin 40 (VBUS) or 39 (VSYS)

Time Module:
⦁	RST >> pin 21(GP16), DAT >> pin 22(GP17), CLK >> pin 24(GP18)
⦁	Ground it and supply 3V either pin 37(3V3_EN) or pin 36(3V3(OUT))

Buzzer:
⦁	IO >> pin 20(GP15)
⦁	Supply with ground and 3V

Moving Forward:
TO improve I would probably create a helper method for the self-checking/pushing. There was a heavy time constraint to get the demo working. This shouldn't have been a issue in the first place, but we had some faulty parts. So with little time and no budget, that was the solution.

Note:
the only code that is needed to configure the script is main.py. Everything else is either a library used or a test of the parts/scan
That being said you do need to have the libraries isntalled onto the pico

Also if the pin layout needs to be differnt make sure to update the code to reflect it

Link to a short YouTube video:
https://www.youtube.com/watch?v=sEOtqeTDLdg

This Project was inspired by 
https://www.youtube.com/watch?v=EOMcPAKL6RM&t=152s