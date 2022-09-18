#http://192.168.1.13/snapshot.jpg
# 192.168.1.13
import time
import os
import requests # request img from web
import shutil # save img locally
from datetime import date
from datetime import datetime

#change these if needed
CAMERA_IP = "192.168.1.103"
SNAPSHOT_INTERVAL = 1
TIME_TO_START = (9, 25) # HOUR , MINUTE
OVERRIDE = False

START = time.time()
CAMERA_URL = ("http://%s/snapshot.jpg" % (CAMERA_IP))
today = date.today()
PATH = "%s/imgs/" % (today.strftime("%m-%d-%y"))

def calc_dur(dur):
    """ needs doc string
    """
    return int(dur - START)

def pull_img():
    try:
        res = requests.get(CAMERA_URL, stream = True, timeout=4)
        if res.status_code == 200:
            now = datetime.now()
            file_name = PATH + str(calc_dur(time.time())) + ".jpg"
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
                print('Image sucessfully Downloaded: ',file_name)
            return True
    except:
        return False

def test_connection():
    try:
        res = requests.get(CAMERA_URL, stream = True, timeout=2)
        if res.status_code == 200:
            return True
    except:
        return False

def main():
    # get image
    running = True
    while running:
        if pull_img() == True:
            time.sleep(SNAPSHOT_INTERVAL)
        else:
            print("\nCAMERA DISCONNECTED!!")
            running = False
    print("Closing in 5...")
    time.sleep(5)
    quit()
    
    
if __name__ == "__main__":
    # Waits for TIME_TO_START
    print("Waiting for 9:25 to start...")
    time_to_go = False
    while time_to_go == False and OVERRIDE == False:
        now = datetime.now()
        if int(now.strftime("%H")) >= TIME_TO_START[0] and int(now.strftime("%M")) >= TIME_TO_START[1]: # monkey brain code ignore
            time_to_go == True
            break
        time.sleep(1)

    # Attempts to connect to cameras and begin main loop
    print("Connecting to camera %s..." % (CAMERA_IP))
    if test_connection() == False:
        print("FAILED TO CONNECT TO %s" % (CAMERA_URL))
        print("closing in 5s.")
        time.sleep(5)
        quit()
    print("Connected to %s!" % (CAMERA_URL))
    print("\nStarting main loop...")
    
    # make dir
    try:
        os.makedirs(PATH)
    except FileExistsError:
    # directory already exists
        print(PATH + " already exists!")
        pass
    
    main()
    """
    while True:
        print("Attempting to recconnect in 5 seconds...")
        time.sleep(5)
        if
    """

