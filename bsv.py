    def get_followers(self, profile):
       self.driver.get('https://www.instagram.com/' + profile)
       flw_btn = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
       flw_btn.click()
       popup = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]')))
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