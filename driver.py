"""
@Cuong Tran's scroll function did not work with this website for some reason :(
"""
"""
TODO: add a function for the driver to click on a certain tab
"""


import requests
from selenium import webdriver
import time

class driver():

    def __init__(self, base):
        self.browser = webdriver.Chrome('/Users/nathanielnethercott/Desktop/Coding/Stonks/quaran-timeismoney/chromedriver')
        self.base = base

    def launch(self):
        self.browser.get(self.base)

    def terminate(self):
        self.browser.quit()

    def scroll(self, direction, num):
        #could do this based on time elapsed (like only scroll for x seconds)
        #maybe figure out sometime why the document.body.scrollHeight aint working
        #could also make the range a function of desired history length
        if direction == 'down':
            for i in range(num):
                self.browser.execute_script("window.scrollBy(0, document.body.scrollHeight);")
                time.sleep(0.25)
        elif direction == 'up':
            for i in range(num):
                self.browser.execute_script("window.scrollBy(0, -document.body.scrollHeight);")
                time.sleep(0.25)
        elif direction == 'top':
            self.browser.execute_script("window.scrollTo(0, 0);")

        elif direction == 'smidgeDown':
            self.browser.execute_script("window.scrollBy(0, 2);")

    def html_scrolled(self, num):
        self.scroll('down',num)
        return self.browser.page_source


'''
#Cuong's method:

def scroll_Bottom(self):
    # Get scroll height
    last_height = self.browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(0.5)
        # Calculate new scroll height and compare with last scroll height
        new_height = self.browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height'''
