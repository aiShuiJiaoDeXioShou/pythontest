import time
import random
from PIL import ImageGrab
from pynput import keyboard,mouse

show = [
    "小声说",
    "从零开始实验",
    "变身成为奥特曼"
]

time.sleep(1)

my_mose = mouse.Controller()
my_key = keyboard.Controller()
# my_mose.position(0,20)
# my_mose.click(mouse.Button.right)

# 糊弄臭饺子
while(True):
    time.sleep(1)
    index = random.randint(0, len(show)-1)
    my_key.type(show[index])
