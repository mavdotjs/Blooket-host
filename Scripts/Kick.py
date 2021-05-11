"""
	This script sends a request to kick a specific player from the game.
"""
import menu
import requests
pinfile = open('Scripts/pin.txt', 'r')
gamePin = pinfile.read()
name = str(input("Name to kick: "))
pinfile.close()
# Sends request to kick the specified player
r = requests.delete(f"https://api.blooket.com/api/firebase/client?id={gamePin}&name={name}", headers={
	"Referer": "https://www.blooket.com/"
})

print(r.text)
menu.loadmenu()