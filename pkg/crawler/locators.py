from selenium.webdriver.common.by import By

class InstaLocators(object):


    LOGIN_USERNAME = (By.XPATH, "//input[@name='username']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//div/button/div[contains(text(),'Log In')]")
    NOT_NOW_BUTTON = (By.XPATH, "//div/button[contains(text(),'Not Now')]")
    USERNAME = (By.XPATH, "//h2")
    POST = (By.XPATH, "//span[@class='-nal3 ']/span[@class='g47SY ']")
    FOLLOWERS = (By.XPATH, "//li/a/span")
    FOLLOWING = (By.XPATH, "//li/a[text()[contains(., 'following')]]//span")
    POST_BOX = (By.XPATH, "//div[@class='v1Nh3 kIKUG  _bz0w']")
    POST_LIKE_COUNT = (By.XPATH, "//li[@class='-V_eO']/span[@class='_1P1TY coreSpriteHeartSmall']/preceding-sibling::span")
    POST_COMMENT_COUNT = (By.XPATH, "//li[@class='-V_eO']/span[@class='_1P1TY coreSpriteSpeechBubbleSmall']/preceding-sibling::span")
    FOLLOWER_USER = (By.XPATH, "//div[@role='dialog']//ul//li//a[@title]")
    FOLLOWING_USER = (By.XPATH, "//div[@role='dialog']//ul//li//a[@title]")
    POST_LIKE_OTHERS_BUTTON = (By.XPATH, "//a[@class='zV_Nj']")
    POST_LIKED_USER = (By.XPATH, "//div[@class='                     Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                 ']//a[@href]//text()")
    POST_COMMENT = (By.XPATH, "//div[@class='eo2As ']//ul[@class='Mr508 ']")
    POST_COMMENT_CONTENT = (By.XPATH, "//div[@class='eo2As ']//ul[@class='Mr508 ']//h3/following-sibling::span")
    POST_COMMENT_AUTHOR = (By.XPATH, "//div[@class='eo2As ']//ul[@class='Mr508 ']//h3")

    EXIT_BUTTON = (By.XPATH, "//h1[@class='m82CD']//following-sibling::div")
    LIKE_CHECK = (By.XPATH, "//div[contains(text(),'Liked by')]")
    RIGHT_ARROW = (By.XPATH, "//a[contains(@class,'coreSpriteRightPaginationArrow')]")
    SHOWN_LIKED_USER_ON_POST = (By.XPATH, "//a[@title]")
    PROFILE_PICTURE_URL = (By.XPATH, "//span[@tabindex='-1']//img[@data-testid='user-avatar']/@src")

    # Wait checking XPATH here