"""
@author Nate :)

Using data from Yahoo finance
"""
"""
TODO:
- Learn how to use selenium so I can just do this more generally.
- Gotta figure out how to scroll to the bottom of the page (selenium) since
  we only get the first 100 entries
- Float conversion with commas, could write some simple split/join-map action
    - helper function script?
- Options to the history function for history length, etc
"""
import bs4
import requests
from bs4 import BeautifulSoup
from Portfolio import portfolio #use this later
import pandas as pd

class stock:
    def __init__(self, ticker):
        self.id = ticker
        self.address = 'https://finance.yahoo.com/quote/'+self.id+'/history?p='+self.id
        self.makeSoup()

    def makeSoup(self):
        r = requests.get(self.address).text
        self.base_soup = BeautifulSoup(r, 'lxml')

    def get_history(self):
        table = self.base_soup.find('table', {'class': 'W(100%) M(0)'})
        contents = table.tbody.find_all('tr')

        labels = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj. Close', 'Volume']
        collected = {label:[] for label in labels}

        for date in contents:
            tabular = [cat.span.text for cat in date.find_all('td')]
            if len(tabular)==7:
                tabular[1:-1] = map(float, tabular[1:-1])
                for label,value in zip(labels,tabular):
                    collected[label].append(value)
            else:
                pass
        return pd.DataFrame(collected)


test = stock('CNQ.TO')
df = test.get_history()
print(df)
