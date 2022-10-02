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


def attemptSquareSpaceLogin(driver, max_depth, level):
    if level < max_depth:
        try:
            username_field = '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/form/div[1]/div[1]/div[1]/div/input'
            password_field = '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/form/div[2]/label/div/div[1]/div/div/input'
            confirm_button = '/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/form/button'
            caucc_check = '//*[@id="renderTarget"]/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/a'
            login_check = '//*[@id="renderTarget"]/div/div[3]/div/div/div/div/div/div/div/div[1]/div[1]/h1'
            login_location = "C:/Users/Chade/Desktop/ccs.txt"
            # opens the square space website
            driver.get("https://account.squarespace.com/")
            time.sleep(1)

            user = driver.find_element(By.XPATH, username_field)
            pas = driver.find_element(By.XPATH, password_field)
            squaresUser, squaresPass = get_login(login_location)
            user.send_keys(squaresUser)
            pas.send_keys(squaresPass)

            time.sleep(1)
            driver.find_element(By.XPATH, confirm_button).click()

            time.sleep(5)

            if not driver.find_elements(By.XPATH, login_check):
                print(
                    f"[SQUARESPACE][WARNING] Cant login! Was Username/Password was incorrect?\n{max_depth - level} Attempt(s) remaining...\n")
                attemptSquareSpaceLogin(driver,  max_depth, level=level + 1)
            print("[SQUARESPACE][SUCCESS] Logged in to square space..")
            if not driver.find_elements(By.XPATH, caucc_check):
                print(
                    f"[SQUARESPACE][WARNING] Cant Find CAUCC!\n{max_depth - level} Attempt(s) remaining...\n")
                attemptSquareSpaceLogin(driver,  max_depth, level=level + 1)
            else:
                return True
        except Exception as error:
            print(
                f"[SQUARESPACE][WARNING] Cant login! Execption was thrown\n{error}\n{max_depth - level} Attempt(s) remaining...\n")
            attemptSquareSpaceLogin(driver,  max_depth, level=level + 1)
    else:
        driver.quit()
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
    website_button = '/html/body/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/div/a'
    pages_button = '/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/a/div/span/span[1]/p'
    online_worship = "/html/body/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/section/div[1]/div[2]/div/div/div[1]"
    driver = webdriver.Chrome(options=chrome_options)
    logged_in = attemptSquareSpaceLogin(driver, 3, 0)
    if logged_in:
        print("[SQUARESPACE][SUCCESS] Properly initialized Squarespace..")
    else:
        print("[SQUARESPACE][ERROR] Final login attempt was a fail..")
        return

    driver.find_element(By.XPATH, website_button).click()
    time.sleep(2)
    driver.find_element(By.XPATH, pages_button).click()
    time.sleep(2)
    driver.find_element(By.XPATH, online_worship).click()
    time.sleep(4)

    #
    # /html/body/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div/section/div[1]/div[2]/div/div/div[1]
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
