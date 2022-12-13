from insta import Instagram
import os

driver_path = "/Users/hardeepsingh/Downloads/chromedriver"
email = "tekkitest"
password = "Tws2022$$"

insta = Instagram(webdriver_path=driver_path, email=email, pass_=password)
insta.login()

# Searching a specific account with similiar content like mine and following the people who
# who follows that account
insta.search_accounts(account_username="sakshi")
insta.scroll_and_follow(scroll_limit=10)
insta.watchstory()

# print(insta.people_followed)

# # unfollow every one
# insta.unfollow()

# insta.close_window()