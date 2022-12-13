from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import json
import sys

class Instagram:
    def __init__(self, webdriver_path, email, pass_):
        '''Takes three required params wedriver_path:type(str),
        email:type(str),pass_:type(str)'''

        self.people_followed = 0
        self.webdriver_path = webdriver_path
        self.email = email
        self.pass_ = pass_
        self.driver = webdriver.Chrome(executable_path = self.webdriver_path)
    
    def login(self):
        '''This function logs you in to the instagram'''

        self.driver.get("https://www.instagram.com/")
        time.sleep(8)

        self.driver.find_element(By.NAME, "username").send_keys(self.email)
        self.driver.find_element(By.NAME, "password").send_keys(self.pass_)
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]//*[@type="submit"]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[contains(text(), "Not now")]').click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//*[@class="_a9-- _a9_1"]').click()
        time.sleep(10)
    
    def search_accounts(self, account_username):
        '''Takes one required argument account_username:type(str)
        to find and open the profile of the username mentioned in
        parameter'''

        url = "https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query="+account_username+"&rank_token=0.09551295091776835&include_reel=true"
        time.sleep(5)
        #open tab
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't') 
        # You can use (Keys.CONTROL + 't') on other OSs
        self.driver.get(url)
        time.sleep(2)
        json_text = self.driver.find_element(By.CSS_SELECTOR, 'body > pre')
        time.sleep(2)
        # print(json_text.text)
        # Writing to username.json
        with open("username.json", "w") as outfile:
            outfile.write(json_text.text)

    def scroll_and_follow(self, scroll_limit):
        '''Takes one required parameter scroll_limit:type(int)
        Its is recommend to pass maximum value of 125'''
        count = 0
        time.sleep(3)
        # Opening JSON file
        f = open('username.json')
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        for i in data['users']:
            # print(i['user']['username'])
            username = i['user']['username']
            count = count+1
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't') 
            self.driver.get('https://www.instagram.com/'+username)
            time.sleep(10)

            # Follow  user
            self.driver.find_element(By.XPATH, '//*[@class="_acan _acap _acas _aj1-"]').click()
            # self.driver.find_element(By.XPATH, '//*[@class="_aacl _aaco _aacw _aad6 _aade"]').click()
            time.sleep(10)

            
            # Get post follower and follow count
            url     = 'https://i.instagram.com/api/v1/users/web_profile_info/?username='+username
        
            headers = {"X-IG-App-ID": "936619743392459"}
            res = requests.get(url, headers=headers)
            print("------------------------------------")
            print(res.json())
            user_data = res.json()
            is_reel = user_data['data']['user']['highlight_reel_count']
            if is_reel == 0:
                print("Followers", user_data['data']['user']['edge_followed_by'])
                print("is_private:", user_data['data']['user']['is_private'])
                print("Following", user_data['data']['user']['edge_follow'])
                print("Posts", user_data['data']['user']['edge_owner_to_timeline_media']['count'])
                time.sleep(5)

                # If profile is_private is false
                if user_data['data']['user']['is_private'] == False:
                    if user_data['data']['user']['edge_owner_to_timeline_media']['count'] > 0:
                        # for i in range(1):
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, '//article/div/div/div[1]/div['+str(1)+']').click()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, '//*[@class="_aamu _ae3_ _ae47 _ae48"]//*[@class="_abm0 _abl_"]//*[@aria-label="Like"]').click()
                        time.sleep(5)
                            # self.driver.find_element(By.XPATH, '//*[@class="_aamu _ae3_ _ae47 _ae48"]//*[@class="_abm0 _abl_"]//*[@aria-label="Comment"]').click()
                            # time.sleep(2)
                            # self.driver.find_element(By.XPATH, '//*[@class="_aidk"]/textarea)').send_keys("Looks good.")
                            # time.sleep(2)
                            # self.driver.find_element(By.XPATH, '//*[@class="_aidk"]//*[@role="button"]').click()
            else:
                # Watch story
                self.driver.find_element(By.XPATH, '//*[@class="_aarf _aarg"]').click()
                time.sleep(5)
                self.driver.find_element(By.XPATH, '//*[@class="_abx4"]').click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, '//*[@class="_ac0g"]').click()
                time.sleep(5)

                print("Followers", user_data['data']['user']['edge_followed_by'])
                print("is_private:", user_data['data']['user']['is_private'])
                print("Following", user_data['data']['user']['edge_follow'])
                print("Posts", user_data['data']['user']['edge_owner_to_timeline_media']['count'])
                time.sleep(2)

                # If profile is_private is false
                if user_data['data']['user']['is_private'] == False:
                    if user_data['data']['user']['edge_owner_to_timeline_media']['count'] > 0:
                        # for i in range(1):
                        time.sleep(5)
                        self.driver.find_element(By.XPATH, '//article/div/div/div[1]/div['+str(1)+']').click()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, '//*[@class="_aamu _ae3_ _ae47 _ae48"]//*[@class="_abm0 _abl_"]//*[@aria-label="Like"]').click()
                        time.sleep(5)
                            # self.driver.find_element(By.XPATH, '//*[@class="_aamu _ae3_ _ae47 _ae48"]//*[@class="_abm0 _abl_"]//*[@aria-label="Comment"]').click()
                            # time.sleep(2)
                            # self.driver.find_element(By.XPATH, '//*[@class="_aidk"]/textarea)').send_keys("Looks good.")
                            # time.sleep(2)
                            # self.driver.find_element(By.XPATH, '//*[@class="_aidk"]//*[@role="button"]').click()




        

        # followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        # followers.click()
        # time.sleep(3)

        # for _ in range(scroll_limit):
        #     time.sleep(2)
        #     scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

        # buttons = self.driver.find_element(By.CLASS_NAME, "sqdOP")
        # for button in buttons:
        #     time.sleep(1)
        #     if button.text == "Follow":
        #         # button.click()
        #         self.people_followed += 1
        #     else:
        #         pass
    
    # def unfollow(self):
    #     '''This function unfollows everyone you are following'''

    #     time.sleep(3)
    #     self.driver.find_element(By.CLASS_NAME, "_6q-tv").click()
    #     time.sleep(3)
    #     self.driver.find_element(By.CLASS_NAME, "-qQT3").click()

    #     time.sleep(3)
    #     user_info = self.driver.find_element(By.CLASS_NAME, "-nal3")
    #     user_info[2].click()

    #     # Scroll through following list 
    #     for _ in range(5):
    #         time.sleep(2)
    #         scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]')
    #         self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    #     # Unfollow people one by one
    #     time.sleep(2)
    #     buttons = self.driver.find_element(By.CLASS_NAME, "sqdOP")
    #     for button in buttons:
    #         if button.text == "Following":
    #             button.click()
    #             time.sleep(3)
    #             unfollow_btn = self.driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div[3]/button[1]")
    #             unfollow_btn.click()
    #             time.sleep(3)

    # def watchstory(self):
    #     '''This will see watch story'''
    #     time.sleep(4)
    #     self.driver.find_element(By.CLASS_NAME, "_aarf _aarg").click()
    #     time.sleep(3)
    #     '''This will like watch story'''
            
    def close_window(self):
        time.sleep(5)
        self.driver.quit()