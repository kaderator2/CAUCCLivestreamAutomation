from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
# chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
# driver = webdriver.Chrome(options=chrome_options)

# Basic login attempts


def get_login(filename):
    f = open(filename, 'r')
    creds = []
    for line in f.readlines():
        creds.append(line)
    f.close()
    return creds[0], creds[1]

    # squaresUser = input(
    #    "[SQUARESPACE] Please Enter the SquareSpace Username: ")
    # squaresPass = input(
    #    "[SQUARESPACE] Please Enter the SquareSpace Password: ")


def attemptSquareSpaceLogin(driver, level, max_depth):
    if level < max_depth:
        try:
            # opens the square space website
            driver.get("https://account.squarespace.com/")
            time.sleep(1)
            user = driver.find_element(  # Finds the username field
                By.XPATH, '//*[@id="renderTarget"]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/form/div[1]/div[1]/input')
            pas = driver.find_element(  # Finds the password field
                By.XPATH, '//*[@id="renderTarget"]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/form/div[2]/div[1]/div/input')

            squaresUser, squaresPass = get_login(
                "C:/Users/Loft/Desktop/ssc.txt")
            user.send_keys(squaresUser)
            pas.send_keys(squaresPass)

            time.sleep(1)
            confirm = driver.find_element(
                By.XPATH, '//*[@id="renderTarget"]/div/div[2]/div/div[1]/div/div[1]/div[1]/div/form/button')
            confirm.click()

            time.sleep(5)
            if not driver.find_elements(By.XPATH, '//*[@id="renderTarget"]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[1]/h1'):
                print(
                    f"[SQUARESPACE][WARNING] Cant login! Was Username/Password was incorrect?\n{max_depth - level + 1} Attempts remaining...\n")
                attemptSquareSpaceLogin(driver, level=level + 1, max_depth)
            print("[SQUARESPACE][SUCCESS] Logged in to square space..")
            if not driver.find_elements(By.XPATH, '//*[@id="renderTarget"]/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a'):
                print("[SQUARESPACE][WARNING] Cant Find CAUCC!")
                attemptSquareSpaceLogin(driver, level=level + 1, max_depth)
            else:
                return True
        except Exception as error:
            print(
                f"[SQUARESPACE][WARNING] Cant login! Execption was thrown\n{error}\n{max_depth - level + 1} Attempts remaining...\n")
            attemptSquareSpaceLogin(driver, level=level + 1, max_depth)
    else:
        return False


"""
def attemptYouTubeLogin(driver):
    try:
        driver.get("https://account.squarespace.com/")
        ytUser = input("[YOUTUBE] Please Enter the Youtube Username: ")
        ytPass = input("[YOUTUBE] Please Enter the Youtube Password: ")
        return True
    except:
        print(
            "[YOUTUBE][WARNING] Cant login! Was Username/Password was incorrect?\nTrying again...\n")
        return False

# Main functions

"""


def mainSquareSpace():
    driver = webdriver.Chrome(options=chrome_options)
    logged_in = attemptSquareSpaceLogin(driver, 0, 3)
    if logged_in:
        print("[SQUARESPACE][SUCCESS] Properly initialized Squarespace..")
    else:
        print("[SQUARESPACE][ERROR] Final login attempt was a fail..")
    # do other things


"""
def mainYouTube():
    driver = webdriver.Chrome(options=chrome_options)
    loggedIn = False
    for retries in range(3):
        if loggedIn == False:
            time.sleep(1)
            loggedIn = attemptYouTubeLogin(driver)
            print("\n[YOUTUBE][WARNING]%s login retries left!" %
                  (str(3 - retries + 1)))
            time.sleep(2)
    if not loggedIn:
        print("[YOUTUBE][ERROR] Final login attempt was a fail.. Please check youtube manually..\nclosing in 5s.")
        time.sleep(5)
        quit()
    print("[YOUTUBE][SUCCESS] Logged in to youtube..")
    driver.quit()
    # do other things

"""


def main():
    print("starting")
    mainSquareSpace()


if __name__ == "__main__":
    main()


# wait for this VVV
# driver.quit()
