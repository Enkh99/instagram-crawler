from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from locators import InstaLocators
from argparser import parser
import argparse
import pdb
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="insta",
    user="postgres",
    password="password")

def login(driver):
    username = "enkodod"
    password = "19991017"
    # username = "icancrawl"
    # password = "19991017"
    # Load page
    driver.get("https://www.instagram.com/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div//input[@name='username']")))
    # Login
    driver.find_element_by_xpath(
        "//div//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath(
        "//div//input[@name='password']").send_keys(password)
    driver.find_element(*InstaLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Save Your Login Info?')]")))
    driver.find_element(*InstaLocators.NOT_NOW_BUTTON).click()

    sleep(2)


def scrape_profile_info(driver):
    username = driver.find_element(*InstaLocators.USERNAME).text
    post = driver.find_element(*InstaLocators.POST).text
    followers = driver.find_element(*InstaLocators.FOLLOWERS).text
    following = driver.find_element(*InstaLocators.FOLLOWING).text
    print("Username: ", username, "Post: ", post,
          "Followers: ", followers, "Following: ", following)
    return username, post, followers, following


def scrape_followers(driver):
    sleep(1)
    driver.find_element(*InstaLocators.FOLLOWERS).click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul//li//a[@title]")))
    sleep(1)
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script(
        "return document.querySelector(\"div[role='dialog'] ul\").scrollHeight")
    while True:
        driver.execute_script(
            "let ul = document.querySelector(\"div[role='dialog'] ul\"); let p = ul.parentElement; p.scrollTo(0, ul.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.querySelector(\"div[role='dialog'] ul\").scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Finally, scrape the followers
    followers_elems = driver.find_elements(*InstaLocators.FOLLOWER_USER)

    return [e.text for e in followers_elems]


def scrape_followings(driver):

    driver.find_element(*InstaLocators.FOLLOWING).click()

    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//ul//li//a[@title]")))
    sleep(1)

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script(
        "return document.querySelector(\"div[role='dialog'] ul\").scrollHeight")
    while True:
        driver.execute_script(
            "let ul = document.querySelector(\"div[role='dialog'] ul\"); let p = ul.parentElement; p.scrollTo(0, ul.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.querySelector(\"div[role='dialog'] ul\").scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Finally, scrape the followers
    followings_elems = driver.find_elements(*InstaLocators.FOLLOWING_USER)

    return [e.text for e in followings_elems]


def scrape_posts(driver):

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        print(last_height)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(new_height)
        if new_height == last_height:
            break
        last_height = new_height

    posts_elems = driver.find_elements(*InstaLocators.POST_BOX)
    print(posts_elems)

    sleep(1)

    likes = 0
    comments = 0
    for i in posts_elems:

        webdriver.ActionChains(driver).move_to_element(i).perform()
        try:
            likes += int(driver.find_element(*
                         InstaLocators.POST_LIKE_COUNT).text)
            print(likes, "likes")
            # others_button = driver.find_element(*InstaLocators.POST_LIKE_OTHERS_BUTTON)
            # shown_like = driver.find_element(*InstaLocators.SHOWN_LIKED_USER_ON_POST)
        except:
            print("IGTV video or not Liked")

        try:
            comments += int(driver.find_element(*
                            InstaLocators.POST_COMMENT_COUNT).text)
            print(comments, "comment")
        except:
            print("Post not scraped")
    return likes, comments

    # driver.find_element(*InstaLocators.RIGHT_ARROW).click()
    # sleep(1)

# def like_checker(driver):

    # if like_check != None:
    #     if others_button != None:
#             driver.find_element(*InstaLocators.POST_LIKE_OTHERS_BUTTON).click()
#             likers = scrape_post_likes(driver)
#             return likers
#         else:
#             print(shown_like)
#             return shown_like
#     else:
#         driver.find_element(*InstaLocators.RIGHT_ARROW).click()
#         sleep(1)


def scrape_post_likes_comments(driver):

    posts_elems = driver.find_elements(*InstaLocators.POST_BOX)
    print(posts_elems)

    sleep(1)

    likes = 0
    comments = 0
    for i in posts_elems:

        webdriver.ActionChains(driver).move_to_element(i).perform()
        try:
            likes += int(driver.find_element(*
                         InstaLocators.POST_LIKE_COUNT).text)
            print(likes, "likes")
            # others_button = driver.find_element(*InstaLocators.POST_LIKE_OTHERS_BUTTON)
            # shown_like = driver.find_element(*InstaLocators.SHOWN_LIKED_USER_ON_POST)
        except:
            print("IGTV video or not Liked")

        try:
            comments += int(driver.find_element(*
                            InstaLocators.POST_COMMENT_COUNT).text)
            print(comments, "comment")
        except:
            print("Post not scraped")

        pdb.set_trace()


def scrape_post_likes(driver):

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[@class='m82CD']")))

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script(
        "return document.querySelector(\"div[class='pbNvD  fPMEg     '] div[style='flex-direction: column; padding-bottom: 0px; padding-top: 0px;']\").scrollHeight")
    while True:
        driver.execute_script(
            "let ul = document.querySelector(\"div[class='pbNvD  fPMEg     '] div[style='flex-direction: column; padding-bottom: 0px; padding-top: 0px;']\"); let p = ul.parentElement; p.scrollTo(0, ul.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(
            "return document.querySelector(\"div[class='pbNvD  fPMEg     '] div[style='flex-direction: column; padding-bottom: 0px; padding-top: 0px;']\").scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    other_liked_users = driver.find_elements(*InstaLocators.POST_LIKED_USER)

    return [e.text for e in other_liked_users]

def insert_query(userID, lost_followers, new_followers):


    cursor = conn.cursor()

    scraped_data_table_insert_query = """ INSERT INTO scraped_data (user_id, name, follower, following, post_number, total_comment, total_like) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    followers_insert_query = """ INSERT INTO followers (user_id, follower_account) VALUES (%s,%s) """
    followers_delete_query = """ DELETE FROM followers  where  user_id = %s and follower_account = %s """
    followings_insert_query = """ INSERT INTO followings (user_id, following_account) VALUES (%s,%s) """

    # record_for_scraped = (userID, username, follower,
    #                       following, post, comments, likes)

    # cursor.execute(scraped_data_table_insert_query, record_for_scraped)
    # conn.commit()
    # print("User statistic inserted successfully:", userID)

    for f in lost_followers:
        d = [userID, f]
        cursor.execute(followers_delete_query, d)
    conn.commit()

    print(len(followers), "Lost followers successfully deleted")

    for f in new_followers:
        d = [userID, f]
        cursor.execute(followers_insert_query, d)
    conn.commit()

    print(len(followers), "New Followers inserted successfully")

    # for f in followings:
    #     d = [userID, f]
    #     cursor.execute(followings_insert_query, d)
    # conn.commit()
    # print(len(followings), "Record inserted successfully into scraped_data table")
    
def select_userID():

    cursor = conn.cursor()
    select_Query = "select user_id, link from users where is_active and not is_deleted"

    cursor.execute(select_Query)
    return cursor.fetchall()

# */30 * * * * cd /home/chaire/Documents/Enkh-Od/instatrack/pkg/crawler && /usr/bin/python3 crawler.py

def select_followers(userID):

    cursor = conn.cursor()
    select_Query = "select follower_account from followers where user_id = %s"
    cursor.execute(select_Query, [userID])
    return cursor.fetchall()

def insert_lost_add(userID, lost_followers, new_followers):
    cursor = conn.cursor()

    insert_add = """ INSERT INTO added_followers (user_id, username) VALUES (%s,%s)"""
    insert_lost = """ INSERT INTO lost_followers (user_id, username) VALUES (%s,%s) """


    for f in lost_followers:
        d = [userID, f]
        cursor.execute(insert_add, d)

    conn.commit()

    for f in new_followers:
        d = [userID, f]
        cursor.execute(insert_lost, d)

    conn.commit()
    return

def difference_lost(userID):

    old = select_followers(userID)
    old = [i[0]for i in old]

    return list(set(old) - set(followers))

def difference_new(userID):

    old = select_followers(userID)
    old = [i[0]for i in old]

    return list(set(followers) - set(old))

if __name__ == "__main__":

    options = Options()
    userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(
    options=options, executable_path=r"/home/chaire/Documents/chromedriver")

    try:
        # parser()
        login(driver)
        users = select_userID()
        for user in users:
            print(user[1])
            # driver.get("https://www.instagram.com/g.biligt/")
            driver.get(user[1])
            sleep(2)
            # username, post, follower, following = scrape_profile_info(driver)
            followers = scrape_followers(driver)
            print(followers, len(followers))
            driver.find_element(*InstaLocators.EXIT_BUTTON).click()
            sleep(1)
            lost_followers = difference_lost(user[0])
            new_followers = difference_new(user[0])
            insert_lost_add(user[0], lost_followers, new_followers)
            # followings = scrape_followings(driver)
            # print(followings, len(followings))
            # driver.find_element(*InstaLocators.EXIT_BUTTON).click()
            # sleep(1)

            # likes, comments = scrape_posts(driver)
            # sleep(1)

            insert_query(user[0], lost_followers, new_followers)

    finally:
        driver.quit()

# try:
#             driver.find_element(*InstaLocators.LIKE_CHECK)
#             try:
#                 driver.find_element(*InstaLocators.POST_LIKE_OTHERS_BUTTON)
#                 driver.find_element(*InstaLocators.POST_LIKE_OTHERS_BUTTON).click()
#                 likers = scrape_post_likes(driver)
#                 return likers
#             except:
#                 driver.find_element(*InstaLocators.SHOWN_LIKED_USER_ON_POST)
#                 shown_like = driver.find_element(*InstaLocators.SHOWN_LIKED_USER_ON_POST)
#                 print(shown_like)
#                 return shown_like
#             # others_button = driver.find_element(*InstaLocators.POST_LIKE_OTHERS_BUTTON)
#             # shown_like = driver.find_element(*InstaLocators.SHOWN_LIKED_USER_ON_POST)
#         except:
#             driver.find_element(*InstaLocators.RIGHT_ARROW).click()
#             sleep(1)
