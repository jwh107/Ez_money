import pyautogui
import time

pyautogui.FAILSAFE = True

while 1:

    init_time = time.time()
    buying_time = 120                   # in sec

    time.sleep(5)                       # initial delay

    # buy

    while (time.time()-init_time) <= buying_time:

        pyautogui.press('f5')           # refresh
        pyautogui.click(1756, 183)      # click buy
        pyautogui.click(1756, 291)      # click buy_below
        pyautogui.press('y')            # confirm buy
        pyautogui.click(963, 569)       # click ok
        pyautogui.click(955, 566)       # click ok
        pyautogui.click(956, 589)       # click ragfair ok
#       pyautogui.click(958, 588)       # Error ok
        pyautogui.click(950, 799)       # click trade


    time.sleep(5)                       # delay for loading

# sell

    pyautogui.click(747, 37)            # click dealers
    time.sleep(5)
    pyautogui.click(875, 421)           # click Theripist
    time.sleep(5)
    pyautogui.click(235, 45)            # click sell
    time.sleep(5)

# select items
    pyautogui.keyDown('ctrlleft')

    for y in range(320, 952, 126):

        for x in range(1265,1835,63):

            pyautogui.click(x, y)

    pyautogui.keyUp('ctrlleft')

    time.sleep(1)

    pyautogui.click(851, 165)           # click deal

    time.sleep(10)

# go back to flea market

    pyautogui.press('esc')
    time.sleep(10)
    pyautogui.click(949, 36)

    pyautogui.click(950, 799)       # click trade







    


