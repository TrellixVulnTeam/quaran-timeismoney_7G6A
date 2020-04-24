from stock import stock
from mail import mail
from login_info import info
from Portfolio import Portfolio

if __name__ == '__main__':
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
    account.send(['email...'])
