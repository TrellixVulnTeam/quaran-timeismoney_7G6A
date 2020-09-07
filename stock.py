"""
@author nnethercott :)
Using data from Yahoo finance
"""

import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time

from driver import driver
from ui_html_references import history_locations, souped_history_locations

class stock:
    def __init__(self, ticker):
        self.id = ticker
        self.address = 'https://finance.yahoo.com/quote/'+self.id+'/history?p='+self.id
        self.driver = driver(self.address)
        self.base_soup  = None
        self.driver.launch()

    def makeSoup(self, timeframe='default'):
        num=4

        if timeframe !='default':
            self.change_timeframe(timeframe)    #make this thing into a function probably
            start = float(timeframe[0].split('-')[0])
            stop = float(timeframe[1].split('-')[0])
            num = 4*int(stop-start)


        self.base_soup = BeautifulSoup(self.driver.html_scrolled(num), "html.parser")
        #self.driver.terminate()

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

        self.history = pd.DataFrame(collected)

    def get_current(self):
        if self.base_soup is None:
            self.makeSoup()

        current_price = self.base_soup.find('span', {'class':souped_history_locations["currentPrice"]}).text
        self.current = float(current_price)
        self.driver.scroll('top',10)
        return float(current_price)


    def change_timeframe(self, timeframe):
        """
        Arguments: start and stop times in 'yyyy-mm-dd' form
        """

        self.driver.browser.find_element_by_css_selector(history_locations['dropdown']).click()


        start = timeframe[0].split('-')
        stop = timeframe[1].split('-')
        start_input = self.driver.browser.find_element_by_css_selector(history_locations['startDate'])
        stop_input = self.driver.browser.find_element_by_css_selector(history_locations['endDate'])

        start_input.send_keys(start[0]+Keys.TAB+start[1]+start[2])
        stop_input.send_keys(stop[0]+Keys.TAB+stop[1]+stop[2])
        #For some reason the website lets you put in xxxxxx numbers for the year so we need the TAB

        self.driver.browser.find_element_by_css_selector(history_locations['Done']).click()
        self.driver.browser.find_element_by_css_selector(history_locations['Apply']).click()
        time.sleep(5)

    def search(self):   #don't use this if you want to save on time
        search_input = self.driver.browser.find_element_by_css_selector(history_locations['searchBar'])
        search_input.send_keys(self.id)
        time.sleep(3)
        self.driver.browser.find_element_by_css_selector(history_locations['searchButton']).click()
        time.sleep(5)
        self.driver.scroll('smidgeDown')


    def export_history(self, path):
        try:
            filename = self.id + '-'+'('+self.history.iloc[-1]['Date'][-4:]+','+self.history.iloc[0]['Date'][-4:]+')'+'.csv'
            self.history=self.history.iloc[::-1]    #reverse the order so we start chronologically
            self.history.to_csv(path+filename, index=False)
        except:
            print('retrieve history first')
