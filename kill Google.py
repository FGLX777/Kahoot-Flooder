import psutil
import time
import os
from os import system
import colorama
from colorama import Fore, Style
colorama.init()

print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTYELLOW_EX+f"Killing Chrome.exe..")

PROCNAME = "chrome.exe"
killed = 0

for i in range(3):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
            killed += 1
            system("title " + f"Killed {killed}")
            print(Fore.WHITE+"["+Fore.LIGHTGREEN_EX+"+"+Fore.WHITE+"]"+Fore.LIGHTGREEN_EX+f"Killed Chrome.exe!")
    print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTYELLOW_EX+f"Searching for more Chrome.exe")
    time.sleep(3)

