from stock import stock
import time
import datetime

class portfolio():
    def __init__(self, portfolio_contents):
        self.portfolio_ = portfolio_contents
        self.netAssetValue()

    def netAssetValue(self):
        self.stocks = []
        current_positions = []
        for item in self.portfolio_:
            stock_obj = stock(item['ticker'])
            time.sleep(2)
            current_positions.append(stock_obj.get_current())
            stock_obj.driver.terminate()
            self.stocks.append(stock_obj)

        original_positions = [item['entry_price'] for item in self.portfolio_]

        self.netValue = 0
        for index, pair in enumerate(zip(current_positions, original_positions)):
            running_net = (pair[0]-pair[1])*self.portfolio_[index]['quantity']
            self.stocks[index].delta = running_net
            self.netValue += running_net

    def weekly(self):
        pass




'''positions_current = []
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
'''
