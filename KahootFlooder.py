import threading
import os, random, string
import colorama
from colorama import Fore, Style
import selenium
import psutil
import platform
from os import system
from datetime import datetime
from time import sleep
from selenium import webdriver
from discord.ext import commands
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
colorama.init()

system("title " + "Made By FGLX (Open Source Project)")

def logo():
    msg = Fore.LIGHTMAGENTA_EX+"""
                       ____  __.      .__                   __   
                      |    |/ _|____  |  |__   ____   _____/  |_ 
                      |      < \__  \ |  |  \ /  _ \ /  _ \   __\
                      
                      |    |  \ / __ \|   Y  (  <_> |  <_> )  |  
                      |____|__ (____  /___|  /\____/ \____/|__|  
                              \/    \/     \/
        """
    print(msg)


def checkpc():
    while True:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            swap = psutil.swap_memory()
            partition_usage = psutil.disk_usage(partition.mountpoint)
            system("title " + f"Disk {partition_usage.percent}% Memory {swap.percent}%")

gamePin = ''
system('mode con: cols=90 lines=20')
logo()
print("")
print(Fore.WHITE+"$"+Fore.LIGHTMAGENTA_EX+">Enter GamePin")
gamePin = input("")
print(Fore.WHITE+"$"+Fore.LIGHTMAGENTA_EX+">Enter Threads (Shit pc 1-2 | good pc 5-9 | GOD pc 10-20) (must need good internet also)")
threads = int(input(""))
system('mode con: cols=45 lines=10')

botnum = 0


def createBotThread1():
    global botnum
    while True:
        try:
            print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"-"+Fore.WHITE+"]"+Fore.LIGHTYELLOW_EX+f"Bot Connecting..")
            code = ('').join(random.choices(string.ascii_letters + string.digits, k=10))
            user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"     
            options = webdriver.ChromeOptions()
            options.headless = True
            options.add_argument(f'user-agent={user_agent}')
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--allow-running-insecure-content')
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
            driver.get('https://kahoot.it/')
            sleep(0.2)
            driver.find_element_by_xpath('//*[@id="game-input"]').send_keys(gamePin)
            driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/main/div[2]/main/div/form/button').click()
            print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"/"+Fore.WHITE+"]"+Fore.LIGHTYELLOW_EX+f"Bot Picking Name")
            sleep(0.3)
            driver.find_element_by_xpath('//*[@id="nickname"]').send_keys(code)
            driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/main/div[2]/main/div/form/button').click()
            botnum += 1
            print(Fore.WHITE+"["+Fore.LIGHTGREEN_EX+"+"+Fore.WHITE+"]"+Fore.LIGHTGREEN_EX+f"Bot{botnum} Joined Game")
        except:
            print(Fore.WHITE+"["+Fore.RED+"+"+Fore.WHITE+"]"+Fore.RED+f"Bot Failed To Join/Connect")
            pass

for x in range(threads):
    x = threading.Thread(target=createBotThread1)
    x.start()
    sleep(0.2)
y = threading.Thread(target=checkpc)
y.start()

