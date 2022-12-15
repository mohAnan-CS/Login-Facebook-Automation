import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def ignore_notification():
    chrome_options.add_experimental_option("prefs", prefs)

    # open the webpage
    driver.get("https://wwww.facebook.com/")

    #enter username and password
    username.clear()
    username.send_keys("YOUR_EMAIL")
    password.clear()

    # use your username and password
    password.send_keys("YOUR_PASSWORD")

    # target the login button and click it
    time.sleep(5)

    # We are logged in!
    print("Logged in")


def name_parse():
    driver.get(url)
    names = driver.find_elements(By.TAG_NAME, 'h3')
    for name in names:
        name = name.text
        Name.append(name)

# program to parse comments
def comment_parse():
    driver.get(url)
    comments = driver.find_elements(By.CSS_SELE999999CTOR, "[class='ed']") or driver.find_elements(By.CSS_SELECTOR, "[class='ee']") or driver.find_elements(By.CSS_SELECTOR, "[class='eg']")
    for comment in comments:
        comment = comment.text
        Comment.append(comment)


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Firefox()

    # open the webpage
    driver.get("https://wwww.facebook.com/")
    username = driver.find_element(By.ID, "email")
    print("Hello " + username.text)
    password = driver.find_element(By.ID, "pass")
    submit = driver.find_element(By.NAME, "login")
    username.send_keys("YOUR_EMAIL")
    password.send_keys("YOUR_PASSWORD")
    submit.click()
    print("Waiting")
    time.sleep(30)
    print("End Sleep")
    Name = []
    Comment = []
    cnt = 0

    # program to parse comments from 5 pages, if you want comments from all pages then use while loop
    for i in range(6):
        # while True:
        url = "LINK_OF_PAGES"
        url = url + str(cnt)
        name_parse()
        print(Name)
        comment_parse()
        print(Comment)
        print(url)
        cnt = cnt + 10

    # create a dataframe
    data = pd.DataFrame({'Name': Name, 'Comment': Comment})
    data.to_csv('facebook.csv')
    print('data saved')