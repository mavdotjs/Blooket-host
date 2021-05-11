import os
import time
import random
try:
    from stringcolor import *
except ModuleNotFoundError:
    os.system('pip install string-color')
finally:
    from stringcolor import *
def loadmenu():
    time.sleep(3)
    os.system('clear')
    print(cs('Answers: Get all Answers', 'green').bold())
    print(cs('Kick: kick any player', 'green').bold())
    print(cs('Masskick: kick everyone from the game', 'green').bold())
    print(
        cs('Masskwlist: masskick except a username you pick', 'green').bold())
    print(cs('Change pin: change the current game pin stored', 'green').bold())
    scriptselect = str(input('\033[1;36mPlease choose a script from above:  '))
    if (scriptselect == 'change pin') or (scriptselect == 'Change pin'):
        os.system('clear')
        pinfile = open('Scripts/pin.txt', 'w')
        gamepin = str(input("\033[1;36mGame Pin:  "))
        pinfile.write(f'{gamepin}')
        pinfile.close()
        loadmenu()
    elif (scriptselect == 'answers') or (scriptselect == 'Answers'):
        os.system('clear')
        os.system('python Scripts/Answers.py')
    elif (scriptselect == 'kick') or (scriptselect == 'Kick'):
        os.system('clear')
        os.system('python Scripts/Kick.py')
    elif (scriptselect == 'masskick') or (scriptselect == 'Masskick'):
        os.system('clear')
        os.system('python Scripts/MassKick.py')
    elif (scriptselect == 'masskwlist') or (scriptselect == 'Masskwlist'):
        os.system('clear')
        os.system('python Scripts/MassKickWithBlaclist.py')
    else:
        print(f'\033[1;31mERROR script: {scriptselect} not defined \033[0;37m')
        time.sleep(.5)
        os.system('clear')
        loadmenu()