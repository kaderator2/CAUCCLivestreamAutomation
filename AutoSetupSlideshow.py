#search network drive for imgs
# P:\Worship\Video-Powerpoints\2022\7 July 2022\7.10.22 PNGs and Music
import time
import shutil, os
from datetime import date
from datetime import datetime
today = date.today()
dateindots = today.strftime("%m.%d.%y")
dateindots = [ele.lstrip('0') for ele in dateindots]
strdate = ""
for char in dateindots:
    strdate = strdate + char
fulldate = strdate.split(".")

ROOTDIR = "P:/Worship/Video-Powerpoints/20%s/%s %s 20%s/%s PNGs and Music/" % (fulldate[2], fulldate[0], today.strftime("%B"), fulldate[2], strdate)
#ROOTDIR = "P:/Worship/Video-Powerpoints/2022/5 May 2022/5.8.22 PNGs/"
workingDIR = "C:/Users/Loft/Desktop/RollingSlideshowsDONOTDELETE/"

try:
    arr = os.listdir(ROOTDIR)
except:
    print("Cant find new folder!")
    quit()
try:
    targetarr = os.listdir(workingDIR)
except:
    print("Cant find target folder!")
    quit()
newPNGS = False
newMP3 = False
for item in arr:
    if ".PNG" in item:
        newPNGS = True
        print("found %s!" % (item))
for item in arr:
    if ".mp3" in item:
        newMP3 = True
        print("found %s!" % (item))
        
if newPNGS:
    print("clearing %s of PNGS" % (workingDIR))
    for item in targetarr:
        if ".PNG" in item:
            os.remove(workingDIR + item)
    print("copying pngs!")
    for item in arr:
        if ".PNG" in item:
            shutil.copy(ROOTDIR + item, workingDIR)
if newMP3:
    print("clearing %s of MP3S" % (workingDIR))
    for item in targetarr:
        if ".mp3" in item:
            os.remove(workingDIR + item)
    print("copying mp3s!")
    for item in arr:
        if ".mp3" in item:
            shutil.copy(ROOTDIR + item, workingDIR)
quit()
#look fornew .mp3
#move to folder
#start OBS
