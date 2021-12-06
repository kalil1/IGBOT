from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Login:
    def __init__(self, driver, username, password):
        self.driver = driver 
        self.username = username
        self.password = password
    def signin(self):
        self.driver.get("https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
        uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')))
        uid.click()
        uid.send_keys(self.username)
        pswd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')))
        pswd.click()
        pswd.send_keys(self.password)
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')))
        button.click()

