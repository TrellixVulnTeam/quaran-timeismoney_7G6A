from stock import stock
from mail import mail
from login_info import info
from portfolio import portfolio
from driver import driver
import time
from ui_html_references import history_locations

BNS_TO = {'ticker':'BNS.TO', 'entry_price':53.78, 'quantity':5}
CNQ_TO = {'ticker':'CNQ.TO', 'entry_price':17.67, 'quantity':10}

Portfolio = [BNS_TO, CNQ_TO]

if __name__ == '__main__':
    a = driver('https://finance.yahoo.com/')
    b = portfolio(Portfolio,a)
    



"""
account = mail([info['username'], info['password']])

positions_current = []
positions_original = []
for item in Portfolio:
    positions_original.append(item['entry_price'])
    a = stock(item['ticker'])
    positions_current.append(a.get_current())

#clean this whole process up a little
net = 0
index = 0
for current, original in zip(positions_current, positions_original):
    delta = current-original
    net+=delta*Portfolio[index]['quantity']
    index+=1


account.compose('First Automated Report', f'Net value of owned shares: {round(net,2)} CAD')
account.send([info['username']])
"""
