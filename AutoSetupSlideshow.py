# search network drive for imgs
# P:\Worship\Video-Powerpoints\2022\7 July 2022\7.10.22 PNGs and Music
import time
import shutil
import os
from datetime import date
from datetime import datetime
today = date.today()
dateindots = today.strftime("%m.%d.%y")
split_date = dateindots.split(".")
split_date[0] = split_date[0].lstrip("0")
split_date[1] = split_date[1].lstrip("0")
joined_date = ".".join(split_date)
month_fullword_cap = today.strftime("%B")
ROOTDIR = f"P:/Worship/Video-Powerpoints/20{split_date[2]}/{split_date[0]} {month_fullword_cap} 20{split_date[2]}/{joined_date} PNGs and Music/"

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
# look fornew .mp3
# move to folder
# start OBS
