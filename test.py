from stock import stock
from mail import mail
from portfolio import portfolio
from CONFIG import *


if __name__ == '__main__':

    p = portfolio(Portfolio)
    account = mail(mail_info)

'''
UNCOMMENT TO EXECUTE MAILING FEATURE, MAKE SURE TO COMPLETE REQUIRED FIELDS
    message1 = []
    message2 = []
    for item in p.stocks:
        message1.append(f'{item.id}:')
        message1.append(f'{item.delta}'[:4])
        message2.append(f'{item.id}:')
        message2.append(f'{item.weeklyDelta}'[:4])

    newmessage1 = 'Net \n' + ' '.join(message1[0:2])+'\n'+' '.join(message1[2:])
    newmessage2 = 'Weekly \n' + ' '.join(message2[0:2])+'\n'+ ' '.join(message2[2:])
    tosend = newmessage1 + '\n\n' + newmessage2

    account.compose("SUBJECT", {'plaintext':tosend})
    account.send('RECIPIENT')
'''
