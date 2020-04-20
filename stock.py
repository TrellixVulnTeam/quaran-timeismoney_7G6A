"""
@author nnethercott :)
Using data from Yahoo finance
"""

"""
TODO:
- Options to the history function for history length, etc
"""

import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time

from driver import driver
from ui_html_references import history_locations

class stock:
    def __init__(self, ticker):
        self.id = ticker
        self.address = 'https://finance.yahoo.com/quote/'+self.id+'/history?p='+self.id

    def makeSoup(self, timeframe='default', num=4):
        self.driver = driver(self.address)
        time.sleep(3)

        if timeframe !='default':
            self.change_timeframe(timeframe)
            start = float(timeframe[0].split('-')[0])
            stop = float(timeframe[1].split('-')[0])
            num = 4*int(stop-start)


        self.base_soup = BeautifulSoup(self.driver.html_scrolled(num), "html.parser")
        self.driver.terminate()

    def get_history(self, timeframe = 'default'):
        if timeframe != 'default':
            self.makeSoup(timeframe)
        else:
            self.makeSoup()

        table = self.base_soup.find('table', {'class': 'W(100%) M(0)'})
        contents = table.tbody.find_all('tr')

        labels = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj. Close', 'Volume']
        collected = {label:[] for label in labels}

        for date in contents:
            try:
                tabular = [cat.span.text for cat in date.find_all('td')]
                tabular[1:] = map(lambda x: float(''.join(x.split(','))), tabular[1:])
                for label,value in zip(labels,tabular):
                    collected[label].append(value)
            except:
                pass

        return pd.DataFrame(collected)


    def change_timeframe(self, timeframe):
        """
        Arguments: start and stop times in 'yyyy-mm-dd' form
        """
        start = timeframe[0].split('-')
        stop = timeframe[1].split('-')

        self.driver.browser.find_element_by_css_selector(history_locations['dropdown']).click()
        start_input = self.driver.browser.find_element_by_css_selector(history_locations['startDate'])
        stop_input = self.driver.browser.find_element_by_css_selector(history_locations['endDate'])

        start_input.send_keys(start[0]+Keys.TAB+start[1]+start[2])
        stop_input.send_keys(stop[0]+Keys.TAB+stop[1]+stop[2])
        #For some reason the website lets you put in xxxxxx numbers for the year so we need the TAB
        self.driver.browser.find_element_by_css_selector(history_locations['Done']).click()
        self.driver.browser.find_element_by_css_selector(history_locations['Apply']).click()
        time.sleep(3)
