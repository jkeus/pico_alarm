"""
DS1302 real-time clock module

Special thanks to yunline for the DS1302  Library: https://github.com/omarbenhamid/micropython-ds1302-rtc
and T-622 for the I2C LCD library: https://github.com/T-622/RPI-PICO-I2C-LCD

Remember to check out more tutorials on NerdCave - https://www.youtube.com/c/NerdCaveYT


VCC - VSYS (PIN39)
GND - GND (Any ground on Pico)
CLK - GP18 (PIN24)
DAT - GP17 (PIN22)
RST  - GP16 (PIN21)

Buttons - User interface
# 6  = Set_Alarm 
# 7 = add minutes/hours
# 8 = substract minutes/hoursSet_Minutes 
# 9 = onfirm / Disable alarm

"""

####################Import all the libraries#######################
from machine import I2C, Pin
from ds1302 import DS1302
from pico_i2c_lcd import I2cLcd
from lcd_api import LcdApi
import utime
import random
###################################################################


################Setup LCD I2C and initialize#######################
I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, 39, 2, 16)
lcd.clear()

ds = DS1302(Pin(18),Pin(17),Pin(16))
#ds.date_time() # returns the current datetime.
ds.date_time([2023, 11, 28, 1, 17, 00, 00]) # set datetime. comment out
print(ds.date_time())
print('set date time')
######################################################################


#################initialize the Buzzer################################
buzzer = Pin(14, Pin.OUT)
buzzer.high()
######################################################################


#################Buttons#############################################
Button_pins = [6,7,8,9]

Button = []
# Loop to assign GPIO pins and setup input and outputs
for x in range(0,4):

    Button.append(Pin(Button_pins[x], Pin.IN, Pin.PULL_DOWN))
    Button[x].value(0)
######################################################################


#################Set initial values of alarm############################################# 
set_hour = 25
set_minute = 3
set_second = 00
hour = 0
minute = 0
print('initial values set')

####################------------DEFINITIONS----------######################
    
####################------------set_alarm()----------######################
def set_alarm():

    global set_hour
    global set_minute
    global set_second
    global hour
    global minute

    while True:
        try:
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Set hour:")
            break;
        except OSError as e:
            utime.sleep(0.5)
            print('failed 105')

    while Button[3].value() != 1:    
        if Button[1].value() == 1:
            set_hour += 1
            utime.sleep(0.1)
            set_hour = set_hour%24
            
        elif Button[2].value() == 1:
            set_hour -= 1
            utime.sleep(0.1)
            set_hour = set_hour%24
            
        hour = str(set_hour)
        
        while len(hour) < 2:
            hour = '0' + hour
        
        while True:
            try:
                lcd.move_to(10,0)
                lcd.putstr(str(hour))
                break;
            except OSError as e:
                utime.sleep(0.5)
                print('failed 129')
    
    while True:
        try: 
            lcd.clear()
            utime.sleep(0.3)
            lcd.move_to(0,0)
            lcd.putstr("Set minute:")
            break;
        except OSError as e:
            utime.sleep(0.5)
            print('failed 139')

    while Button[3].value() != 1:
        if Button[1].value() == 1:
            set_minute += 1
            utime.sleep(0.1)
            set_minute = set_minute%60
        
        elif Button[2].value() == 1:
            set_minute -= 1
            utime.sleep(0.1)
            set_minute = set_minute%60
        
        minute = str(set_minute)
        while len(minute) < 2:
            minute = '0' + minute
        
        while True:
            try:
                lcd.move_to(12,0)
                lcd.putstr(str(minute))
                break
            except OSError as e:
                utime.sleep(0.5)
                print('failed 162')
    
    while True:
        try:
            lcd.clear()
            break
        except OSError as e:
            utime.sleep(0.5)
            print('failed 169')
        
    return(set_hour,set_minute)

###############################-------------simon_says()--------------------#######################################
def simon_says():
    
    def get_guess_val():
        print("Please select")
        while Button[3].value() != 1:
                if Button[0].value() == 1:
                    guess_val = 0
                    print("curr val 0")
                    while True:
                        try:
                            lcd.clear()
                            lcd.putstr("Blue?")
                            break
                        except OSError as e:
                            utime.sleep(0.5)
                            continue
                    utime.sleep(0.25)
                elif Button[1].value() == 1:
                    guess_val = 1
                    print("curr val 1")
                    while True:
                        try:
                            lcd.clear()
                            lcd.putstr("Black?")
                            break
                        except OSError as e:
                            utime.sleep(0.5)
                            continue
                    utime.sleep(0.25)
                elif Button[2].value() == 1:
                    guess_val = 2
                    print("curr val 2")
                    while True:
                        try:
                            lcd.clear()
                            lcd.putstr("White?")
                            break
                        except OSError as e:
                            utime.sleep(0.5)
                            continue
                    utime.sleep(0.25)
        return guess_val
    
    while True:
        try:
            utime.sleep(0.5)
            lcd.clear()
            lcd.putstr("Simon Says!")
            utime.sleep(1)
            lcd.clear()
            lcd.putstr("Blue to Start")
            print("Simon Says")
            break
        except OSError as e:
            utime.sleep(0.5)
            continue
        
    but_blue = Button[0]
    but_black = Button[1]
    but_white = Button[2]
    but_colors = [but_blue, but_black, but_white]
    game_colors = ["Blue","Black","White"]
    answer = []
    guess = []
    print("blue = start")
    
    while True:
        if Button[0].value() == 1:
            while True:
                try:
                    utime.sleep(0.25)
                    lcd.clear()
                    lcd.putstr("Starting")
                    utime.sleep(1)
                    break
                except OSError as e:
                    utime.sleep(0.5)
                    continue
            break
    print("Starting")


    while True:
            try:
                lcd.clear()
                lcd.putstr("Red to Select")
                utime.sleep(2)
                lcd.clear()
                break
            except OSError as e:
                utime.sleep(0.5)
                continue
    for i in range(4):
        game_on = True
        guess = []
        answer.append(random.randint(0,2))
        while True:
                try:
                    for color in range(len(answer)):
                        lcd.putstr(game_colors[answer[color]])
                        utime.sleep(1)
                        lcd.clear()
                        utime.sleep(0.5)
                    break
                except OSError as e:
                    utime.sleep(0.5)
                    continue
        while game_on:
            print(answer)
            val = get_guess_val()
            print(val)
            guess.append(val)
            print("added")
            
            if len(guess) == len(answer):
                if guess == answer:
                    print("Nice Job")
                    while True:
                        try:
                            lcd.clear()
                            lcd.putstr("Nice Job")
                            utime.sleep(0.5)
                            lcd.clear()
                            break
                        except OSError as e:
                            utime.sleep(0.5)
                            continue
                    game_on = False
                else:
                    print("Incorrect")
                    guess = []
                    print("Try again")
                    while True:
                        try:
                            lcd.clear()
                            lcd.putstr("Incorrect")
                            utime.sleep(0.5)
                            lcd.putstr("Try again")
                            utime.sleep(0.5)
                            lcd.clear()
                            break
                        except OSError as e:
                            utime.sleep(0.5)
                            continue
                        
            elif len(guess) < len(answer):
                print("next")
                while True:
                        try:
                            lcd.clear()
                            lcd.putstr("Next")
                            utime.sleep(0.25)
                            lcd.clear()
                            break
                        except OSError as e:
                            utime.sleep(0.5)
                            continue
                continue
            else:
                guess = []
    
#############################--------------------check_alarm()--------------############################
    
def check_alarm(set_hour,set_minute,set_second):
 
    if set_hour == int(hr) and set_minute == int(m) and set_second == int(s) :
        while Button[3].value() != 1:
            try:
                lcd.clear()
                lcd.move_to(4,0)
                lcd.putstr("Wake Up!")
                
                utime.sleep(0.2)
                buzzer.low()
                utime.sleep(0.2)
                buzzer.high()
                lcd.clear()
            except OSError as e:
                utime.sleep(0.5)
                continue
        simon_says()
        
    utime.sleep(1)


##########################---------WELCOME MESSAGE------------#################################
while True:
    try:
        lcd.move_to(0,0)
        lcd.putstr("Alarm Clock Game")
        utime.sleep(4)
        lcd.clear()
        break
    except OSError as e:
        utime.sleep(0.5)
        print('failed')
print('welcome message')

##########################---------------RUN TIME CODE---------#############################
while True:

    (Y,M,D,day,hr,m,s)=ds.date_time()
    if s < 10:
        s = "0" + str(s)
    if m < 10:
        m = "0" + str(m)
    if hr < 10:
        hr = "0" + str(hr)
    if D < 10:
        D = "0" + str(D)
    if M < 10:
        M = "0" + str(M)
    
    while True:
        try:
            lcd.move_to(0,0)
            lcd.putstr("Time:")
            lcd.move_to(6,0)
            lcd.putstr(str(hr) + ":" + str(m) + ":" + str(s))
            lcd.move_to(0,1)
            lcd.putstr("Date:")
            lcd.move_to(6,1)
            lcd.putstr(str(M) + "/" + str(D) + "/" + str(Y))
            break
        except OSError as e:
            utime.sleep(0.5)
            print('failed 300')
            
    if Button[0].value() == 1:
        utime.sleep(0.1)
        print("Set Alarm")
        set_alarm()
        
    if Button[1].value() == 1:
        print("black on")
        simon_says()

    check_alarm(set_hour,set_minute,set_second)