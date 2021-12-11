from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self, driver):
        self.driver = driver
        self.hrefs = [] 
    def get_num_flw(self):
       time.sleep(0.5)
    #    flw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
       XPATH = "/html/body"
       v = WebDriverWait(self.driver, 3).until(lambda driver: driver.find_element_by_xpath(XPATH).get_attribute("innerHTML"))
       sflw = b(v, 'html.parser')
       fn = sflw.findAll('span', {'class': 'g47SY'})
       try:
           f = int(fn[1]["title"].replace(',', ''))
           return f
       except: 
           print("New Account")
       return 301000000
    def get_followers(self, profile):
       self.driver.get('https://www.instagram.com/' + profile)
       flw_btn = WebDriverWait(self.driver, 11).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a')))
       flw_btn.click()
       popup = WebDriverWait(self.driver, 11).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/div[2]')))
       for h in range(30):
           time.sleep(1)
           self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), popup)
           for i in range(35):
               time.sleep(1)
               self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
       b_popup = b(popup.get_attribute('innerHTML'), 'html.parser')
       for p in b_popup.findAll('li', {'class': 'wo9IH'}):
           try:
               hlink = p.findAll('a')[0]['href']
               self.hrefs.append(hlink)
           except:
               print("nah")
       return self.hrefs
    def is_public(self):
        try:   
            astate = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, 'rkEop')))
            if astate:
                print("account is private")
                return False 
            else:
                return True
        except:
            return True
    def can_like_post(self):
        try:
            posts = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div')
            posts = b(posts.get_attribute('innerHTML'), 'html.parser')
            n = 0
            for post in posts.findAll('a'):
                href = post['href'] 
            return  True
        except: 
            return  False
    def like_all_posts(self):
        try:
            posts = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div')
            posts = b(posts.get_attribute('innerHTML'), 'html.parser')
            n = 0
            for post in posts.findAll('a'):
                href = post['href'] 
                time.sleep(2)
                self.driver.get('https://www.instagram.com' + href)
                time.sleep(3)
                like = WebDriverWait(self.driver, 5.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
                like.click()
                n += 1
            return  n
        except: 
            return  0
        # try:
        #     post = self.driver.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div:nth-child(2) > div:nth-child(2) > a')
        #     if post:
        #         post.click()
        #         like = WebDriverWait(self.driver, 1.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg')))
        #         like.click()
        #         return  True
        # except: 
        #     return  False
    def follow_page(self):
        try:
            button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
            button.click()        
            return True
        except: 
            return False
    def unfollow_followers(self, profile):
       self.driver.get('https://www.instagram.com/' + profile)
       flw_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')))
       flw_btn.click()
       popup = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/ul/div/li[1]')))
       for h in range(30):
           time.sleep(3)
           self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight/{}'.format(str(11-h)), popup)
           popup = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/ul/div')))
           b_popup = b(popup.get_attribute('innerHTML'), 'html.parser')
           for i in range(35):
               time.sleep(3)
               self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
           for p in b_popup.findAll('li'):
               try:
                   hlink = p.findAll('a')[0]['href']
                   self.hrefs.append(hlink)
                   return self.hrefs
               except:
                   print("nah")
                   return self.hrefs

        
