import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')

    def login(self):
        self.driver.get('https://www.messenger.com')

        self.driver.find_element_by_id('email').send_keys(self.email)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_id('loginbutton').click()

    def selectReceiver(self, serialNumber):
        chatRooms = self.driver.find_elements_by_css_selector('a._1ht5._2il3._6zka._5l-3._3itx')
        chatRooms[serialNumber - 1].click()

    def sendMessage(self, message):
        input = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div')

        input.send_keys(message)
        input.send_keys(Keys.ENTER)


