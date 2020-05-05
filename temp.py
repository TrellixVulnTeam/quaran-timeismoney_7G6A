from stock import stock
import os
import requests
from bs4 import BeautifulSoup
import string
import numpy as np
import csv
from itertools import combinations

#WORKHORSE FOR WEBSCRAPING
tickers = np.loadtxt(os.getcwd()+'TSX_tickers.csv', delimiter = ',')

for ticker in tickers:
    try:
        stock_obj = stock(ticker)
        stock.get_history(['2017-02-01', '2020-02-01'])
        stock_obj.export_history(os.getcwd()+'bigscrape')
    except:
        pass



#CODE USED TO GATHER STOCK TICKER SYMBOLS ON TSX
'''alphabet = list(string.ascii_uppercase)

tickers = []
for letter in alphabet:
    #webscraping
    link = 'http://eoddata.com/stocklist/TSX/'+letter+'.htm'
    r = requests.get(link).text
    soup = BeautifulSoup(r, 'html.parser')
    table = soup.find('table', {'class':'quotes'})
    rows = table.find_all('tr')[1:]

    for row in rows:
        ticker = row.find('td').text
        if len(''.join(ticker.split('.')))<=3:  #just helps clean up a bit
            tickers.append(ticker.replace('.','-')+'.TO')   #

with open('TSX_tickers.csv', 'w') as f:
    writer = csv.writer(f, delimiter = ',')
    for ticker in tickers:
        writer.writerow([ticker])'''


#list(combinations(iterable, num_elements))
