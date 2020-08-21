"""
@Cuong Tran's scroll function did not work with this website for some reason :(
"""
"""
TODO: add a function for the driver to click on a certain tab
"""


import requests
from selenium import webdriver
import time
from CONFIG import driver_path

class driver():

    def __init__(self, base):
        self.browser = webdriver.Chrome(driver_path)
        self.base = base

    def launch(self):
        self.browser.get(self.base)
        time.sleep(2)

    def terminate(self):
        self.browser.quit()

    def scroll(self, direction, num=1):
        """
        arguments:
            direction: "down", "up", "top", "smidgeDown"
            num: specifies how many 'scrolls' by the document scrollHeight to move down
        """
        if direction == 'down':
            for i in range(num):
                self.browser.execute_script("window.scrollBy(0, 20*document.body.scrollHeight);")
                time.sleep(0.25)
        elif direction == 'up':
            for i in range(num):
                self.browser.execute_script("window.scrollBy(0, -20*document.body.scrollHeight);")
                time.sleep(0.25)
        elif direction == 'top':
            self.browser.execute_script("window.scrollTo(0, 0);")
        elif direction == 'smidgeDown':
            self.browser.execute_script("window.scrollBy(0, 20);")

    def html_scrolled(self, num):
        self.scroll('down',num)
        return self.browser.page_source
