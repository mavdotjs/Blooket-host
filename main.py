import os
import time
import random
import Scripts.menu
try:
    from stringcolor import *
except ModuleNotFoundError:
    os.system('pip install string-color')
finally:
    from stringcolor import *

os.system('clear')
for x in range(3):
    print('Welcome to Blooket script injector!')
    print('Loading')
    time.sleep(1)
    os.system('clear')
    print('Welcome to Blooket script injector!')
    print('Loading.')
    time.sleep(1)
    os.system('clear')
    print('Welcome to Blooket script injector!')
    print('Loading..')
    time.sleep(1)
    os.system('clear')
    print('Welcome to Blooket script injector!')
    print('Loading...')
    time.sleep(.5)
    os.system('clear')
print('Loaded!')
time.sleep(.5)
os.system('clear')
pinfile = open('Scripts/pin.txt', 'r')
if pinfile.read() == None:
    gamepin = str(input("\033[1;36mGame Pin: \n"))
    pinfile = open('Scripts/pin.txt', 'w')
    pinfile.write(f"{gamepin}")
    pinfile.close()
else:
    pinfile = open('Scripts/pin.txt', 'r')
    gamepin = pinfile.read()
os.system('clear')


def str_append_list_join(s, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(s)
        i += 1
    return ''.join(l1)

for dot in range(5):
    if dot == 0:
        dots = ''
    print(f"Getting Scripts, Please Wait{dots}\nRemember that when you run answers script you can check answers.txt for the list of all answers")
    for printit in range(dot):
        dots = str_append_list_join(".", dot)
    time.sleep(random.randint(1, 3))
    os.system('clear')
    if dot == 4:
        Scripts.menu.loadmenu()


