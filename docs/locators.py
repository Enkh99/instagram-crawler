from selenium.webdriver.common.by import By

class InstaLocators(object):

	FOLLOWERS: "//li/a/span[@title]"
	FOLLOWING: "//li/a[text()[contains(., 'following')]]//span"
	POST_BOX = (By.XPATH, "//div[@class='v1Nh3 kIKUG  _bz0w']")
	POST_LIKE_COUNT = (By.XPATH, "//li[@class='-V_eO']/span[@class='_1P1TY coreSpriteHeartSmall']/preceding-sibling::span")
	POST_COMMENT_COUNT = (By.XPATH, "//li[@class='-V_eO']/span[@class='_1P1TY coreSpriteSpeechBubbleSmall']/preceding-sibling::span")
	FOLLOWER_USER = (By.XPATH, "//li[@class='wo9IH']//a[@href]")
	FOLLOWING_USER = (By.XPATH, "//div[@class='PZuss']/li//a[@href]")
	
	POST_LIKE_OTHERS_BUTTON = (By.XPATH, "//a[@class='zV_Nj']")

	POST_LIKED_USER = (By.XPATH, "//div[@class='                     Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                 ']//a[@href]")
	POST_COMMENT = (By.XPATH, "//div[@class='eo2As ']//ul[@class='Mr508 ']")
	POST_COMMENT_CONTENT = (By.XPATH, "//div[@class='eo2As ']//ul[@class='Mr508 ']//h3/following-sibling::span")
	POST_COMMENT_AUTHOR = (By.XPATH, "//div[@class='eo2As ']//ul[@class='Mr508 ']//h3")