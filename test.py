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
