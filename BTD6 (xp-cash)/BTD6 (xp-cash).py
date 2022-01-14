import pyautogui as a
import time

def gimmecash():
    
# Menu And Level Selection
    a.moveTo(830, 930, duration = 1)
    a.click()

    a.moveTo(540, 260, duration = .75)
    a.click()

    a.moveTo(630, 400, duration = .75)
    a.click()

    a.moveTo(1280, 440, duration = .75)
    a.click()

    a.moveTo(960, 745, duration = 2)
    a.click()
    time.sleep(1)


    # Placing and Upgrading Monkeys
    a.moveTo(241, 400, duration = .25) # Wizard Monkey
    a.press('a')
    time.sleep(.1)
    a.click()
    time.sleep(.1)
    a.click()
    a.moveTo(1550, 780, duration = .2)
    a.click(clicks=4, interval=.1)

    a.moveTo(470, 400, duration = .2) # Ice Monkey
    a.press('t')
    time.sleep(.1)
    a.click()
    time.sleep(.1)
    a.click()
    a.moveTo((1550, 630), duration = .2)
    a.click(clicks=2, interval=.1)
    a.moveTo(1550, 780, duration = .1)
    a.click(clicks=4, interval=.1)

    a.moveTo(640, 400, duration = .2) # Cannon
    a.press('e')
    time.sleep(.1)
    a.click()
    time.sleep(.1)
    a.click()
    a.moveTo((1550, 630), duration = .2)
    a.click(clicks=3, interval=.1)

    a.moveTo(470, 500, duration = .2) # Cannon
    a.press('e')
    time.sleep(.1)
    a.click()
    time.sleep(.1)
    a.click()
    a.moveTo((1550, 630), duration = .2)
    a.click(clicks=3, interval=.1)

    a.moveTo(640, 500, duration = .2) # wizard Monkey
    a.press('a')
    time.sleep(.1)
    a.click()
    time.sleep(.1)
    a.click()
    a.moveTo(1550, 780, duration = .2)
    a.click(clicks=4, interval=.1)

    a.moveTo(642, 567, duration = .2) # Engineer Monkey
    a.press('l')
    time.sleep(.1)
    a.click()
    time.sleep(.1)
    a.click()
    a.moveTo(1550, 480, duration = .2)
    a.click(clicks=2, interval=.1)
    a.moveTo(1550, 630, duration = .2)
    a.click(clicks=3, interval=.1)


# Start Round and Round Duration Delay
    time.sleep(.5)
    a.press('space', presses=2, interval=.1)
    time.sleep(5)
        
    a.moveTo(960, 745, duration = 2)
    a.click()
    a.moveTo(1825,1000, duration=1)
    for i in range(290):
        time.sleep(1)
        a.click()

# Return To Home Screen
    a.moveTo(955, 900, duration=1)
    a.click()

    a.moveTo(790, 840, duration=1.2)
    a.click()
    time.sleep(2.5)

for _ in range(5):
    gimmecash()
