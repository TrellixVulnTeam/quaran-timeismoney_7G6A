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
from driver import driver

class stock:
    def __init__(self, ticker):
        self.id = ticker
        self.address = 'https://finance.yahoo.com/quote/'+self.id+'/history?p='+self.id
        self.makeSoup()

    def makeSoup(self):
        self.driver = driver(self.address)
        self.base_soup = BeautifulSoup(self.driver.html_scrolled(), "html.parser")
        self.driver.terminate()

    def get_history(self):
        table = self.base_soup.find('table', {'class': 'W(100%) M(0)'})
        contents = table.tbody.find_all('tr')

        labels = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj. Close', 'Volume']
        collected = {label:[] for label in labels}

        for date in contents:
            tabular = [cat.span.text for cat in date.find_all('td')]
            if len(tabular)==7:
                tabular[1:] = map(lambda x: float(''.join(x.split(','))), tabular[1:])
                for label,value in zip(labels,tabular):
                    collected[label].append(value)
            else:
                pass
        return pd.DataFrame(collected)


test = stock('CNQ.TO')
