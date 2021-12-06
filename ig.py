from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import login
import getpages
import sys
from getpass import getpass
username = input("Please enter username: ")
print("you entered", username)
password = getpass("Please enter password: ")
profile = input("Who's account are you getting followers from: ")
max_follows = 125
max_likes = 100
driver = 0
def main():
    global driver
    print("Go!")
    driver = webdriver.Chrome('C://Users/wkali/Desktop/IGBOT/chromedriver.exe')
    driver.maximize_window()
    l = login.Login(driver, username, password)
    l.signin()
    info_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
    info_btn.click()
    gp = getpages.Getpages(driver)
    refs = gp.get_followers(username)
    if profile == "":
        unfollow_bot(refs,driver,gp)
    else:
        refs = gp.get_followers(profile)
        follow_bot(refs,driver,gp)    
        

def follow_bot(refs, driver, gp):
    t = time.time()
    # How many likes and follows
    L = 0
    F = 0
    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(0.5)
        if gp.get_num_flw() < 8000:
            if gp.is_public():
                if F < max_follows:
                    follow_page = gp.follow_page()
                    if follow_page:
                        print("followed")
                        print('current follows:' + str(F))
                        F += 1
                        if L < max_likes:
                            like_post = gp.can_like_post()
                            if like_post:
                                like_all = gp.like_all_posts()
                                L += like_all
                                print(str(L) + " Posts Liked")
                            else:
                                print("Couldn't like post")
                        else:
                            L = 0
                            F = 0
                            gp.unfollow_followers()
                            time.sleep(5400)
                else: 
                    L = 0
                    F = 0
                    gp.unfollow_followers()
                    time.sleep(5400)

def unfollow_bot(refs, driver, gp):
    t = time.time()
    # How many accounts have been unfollowed
    L = 0
    F = 0
    for r in refs:
        driver.get('https://www.instagram.com' + r)
        time.sleep(0.5)
        if gp.get_num_flw() < 8000:
            if gp.is_public():
                if F < max_follows:
                    follow_page = gp.follow_page()
                    if follow_page:
                        print("followed")
                        print('current follows:' + str(F))
                        F += 1
                        if L < max_likes:
                            like_post = gp.can_like_post()
                            if like_post:
                                like_all = gp.like_all_posts()
                                L += like_all
                                print(str(L) + " Posts Liked")
                            else:
                                print("Couldn't like post")
                        else:
                            L = 0
                            F = 0
                            gp.unfollow_followers()
                            time.sleep(5400)
                else: 
                    L = 0
                    F = 0
                    gp.unfollow_followers()
                    time.sleep(5400)
if __name__ == "__main__":
    main()