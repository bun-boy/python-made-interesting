import webbrowser, sys
import pyinputplus as pyip

place = pyip.inputStr("Place:")
add = place.split()
link = "https://www.google.com/maps/search/"

for wd in add:
    link = link + "+" + wd

webbrowser.open(link)