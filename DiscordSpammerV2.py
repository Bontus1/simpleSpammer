import sys
from colorama import init
from termcolor import colored
init()
from pyautogui import *
import pyautogui
import time
import random
import pyperclip
import keyboard
import os
from colorama import Fore, Back, Style


def clearShell():
    if sys.platform=="win32":
        os.system("cls")
    else os.system("clear")
    
def mainFunction():
    pyperclip.copy(Name)
    for i in range(Quantity):
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.01)
        pyautogui.press('enter')
        time.sleep(0.01)
        pyautogui.press('enter')
        time.sleep(speed)
        if keyboard.is_pressed("esc"):
            stop()


print(colored("Python-based simple spammer by Bontus.", "green"))

input('Press Enter to continue.')

clearShell()

Name=input('What to send? \nNote that you can also use special characters such as @ to, for example, tag people in discord.\n')


while True:
    try:
        global Quantity
        Quantity=int(input('How many times? \n'))
        break
    except:
        pyautogui.alert("Please Enter a Valid Number")
        clearShell()


while True:
    try:
        global speed
        speed=float(input('Time between messages (in seconds) ? \n'))
        break
    except:
        pyautogui.alert("Please Enter a Valid Number")
        clearShell()



print('Select the chat box on the server and, when ready press the down arrow key to start the script.')
print(colored("Hold esc to stop.", "red"))

while True:
    try:
        if keyboard.is_pressed('down'):
            mainFunction()
            break
    except:
        continue
        
    
pyautogui.alert("Spamming done")

def stop():
    pass
    
    