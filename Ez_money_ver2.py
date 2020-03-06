import pyautogui
import time
import csv
from random import *


def go2Menu(escIter, delay):

    print('go to initial menu')
    
    i = 0
    while i < escIter:
        i = i + 1
        pyautogui.press('esc')

    time.sleep(delay)

def go2TradingFlea():

    print('go to Trading Flea Market')
    
    pyautogui.click(953, 799)                           # click Trading
    time.sleep(3)
    pyautogui.click(963, 37)                            # click Flea
    time.sleep(3)

def go2TradingDealer(DealerName):

    print('go to Trading Dealers %s'%DealerName)
    
    pyautogui.click(953, 799)                           # click Trading
    time.sleep(3)
    pyautogui.click(747, 37)                            # click Dealers
    time.sleep(5)

    if DealerName == 'T':
        pyautogui.click(875, 421)                       # click Theripist

    elif DealerName == 'S':
        pyautogui.click(1215, 411)                      # click Skier

    time.sleep(5)

def typeItem(itemName, itemPrice):

    print('typing item : %s price : %s'%(itemName, itemPrice))

    # double reset
    pyautogui.click(480, 86)                            # click filter
    time.sleep(0.3)
    pyautogui.click(744, 430)                           # click reset
    time.sleep(3)
    
    pyautogui.click(480, 86)                            # click filter
    time.sleep(0.3)
    pyautogui.click(744, 430)                           # click reset
    time.sleep(3)
    
    pyautogui.click(450, 119)                           # click Search Box
    time.sleep(1)
    pyautogui.write(itemName, interval=0.1)             # type item
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(450, 164)                           # select item
    time.sleep(2)
    
    pyautogui.click(480, 86)                            # click filter
    time.sleep(0.3)    
    pyautogui.click(696, 118)                           # click currency
    pyautogui.click(664, 178)                           # click RUB
    pyautogui.click(824, 151)                           # click Max price
    pyautogui.write(itemPrice, interval=0.1)            # type our price
    pyautogui.click(608, 430)                           # click OK
    time.sleep(3)

def Buy(initTime, buyingTime):

    print('buying')
    
    while (time.time() - initTime) <= buyingTime:
        pyautogui.press('f5')                           # refresh
        pyautogui.click(1756, 183)                      # click buy
        pyautogui.click(1756, 291)                      # click buy_below
        pyautogui.press('y')                            # confirm buy
        pyautogui.click(963, 569)                       # click ok
        pyautogui.click(955, 566)                       # click ok
        pyautogui.click(956, 589)                       # click ragfair ok
    #   pyautogui.click(958, 588)                       # Error ok
    #   pyautogui.click(950, 799)                       # click trade

def Sell():

    print('selling')
    
    pyautogui.click(235, 45)                            # click sell
    time.sleep(5)

    # select items
    pyautogui.keyDown('ctrlleft')

    for y in range(287, 981, 63):
        for x in range(1265, 1835, 63):
            pyautogui.click(x, y)

    pyautogui.keyUp('ctrlleft')
    time.sleep(1)
    pyautogui.click(851, 165)                           # click deal
    time.sleep(5)

def readCSV(fileName):

    print('reading item list')
    
    f = open(fileName, 'r')
    rdr = csv.reader(f)

    num_L = []
    name_L = []
    slot_L = []
    dealer_L = []
    price_L = []
    profit_L = []
    flea_filter_L = []

    i = 0

    for line in rdr:

        print(line)
        i = i + 1

        if i > 1:
            num_L.append(line[0])
            name_L.append(line[1])
            slot_L.append(line[2])
            dealer_L.append(line[3])
            price_L.append(line[4])
            profit_L.append(line[5])
            flea_filter_L.append(line[6])

    return num_L, name_L, slot_L, dealer_L, price_L, profit_L, flea_filter_L

########################################################################################################
# main

pyautogui.FAILSAFE = True
buying_time = 60                                        # in sec
esc_iter = 15

num_list = []
name_list = []
slot_list = []
dealer_list = []
price_list = []
profit_list = []
flea_filter_list = []

num_list, name_list, slot_list, dealer_list, price_list, profit_list, flea_filter_list  = readCSV('item_list.csv')

time.sleep(5)                                           # initial delay

# loop
while 1:

    init_time = time.time()                             # start time

    # random number for selecting item
    randNum = randint(0, 13)                            

    # go back to initial Menu page wherever you were
    go2Menu(esc_iter, 3)

    # go to Trading and Flea
    go2TradingFlea()

    # type item and set up our filter
    # typeItem(name_list[randNum], flea_filter_list[randNum])
    
    # buy
    Buy(init_time, buying_time)

    time.sleep(5)                                       # delay for loading

    # go back to initial Menu page wherever you were
    go2Menu(esc_iter, 3)

    # go to Trading Dealers
    # go2TradingDealer(dealer_list[randNum])
    go2TradingDealer('T')
    
    # sell
    Sell()




