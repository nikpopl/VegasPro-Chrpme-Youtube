import random as rnd
import pyautogui as pg
import time
import string

time.sleep(3)

t = 1
while t <= 23:
    textSeed: object = ((rnd.choice(string.ascii_letters[:26])) +
                         (rnd.choice(string.ascii_letters[:26])) +
                         (rnd.choice(string.ascii_letters[:26])))
    pg.click(725, 710)
    pg.keyDown('ctrl')
    pg.press('a')
    pg.press('c')
    pg.keyUp('Ctrl')
    pg.press('del')
    pg.press('home')
    pg.keyDown('ctrl')
    pg.press('v')
    pg.keyUp('Ctrl')
    pg.press('enter')
    pg.click(444,740)
    pg.click(228,606) #555
    pg.keyDown('ctrl')
    pg.press('a')
    pg.keyUp('Ctrl')
    pg.typewrite(textSeed)
    pg.press('enter')
    # pg.click(147, 1060)
    # time.sleep(1)
    # pg.typewrite('https://loremipsum.io/generator/?n=5&t=w')
    # pg.press('enter')
    # time.sleep(3)
    # pg.click(510, 766)
    # time.sleep(3)
    # pg.click(803, 766)
    # pg.click(242, 29)
    # pg.click(1160, 742)
    # pg.click(1394, 385)
    # pg.keyDown('ctrl')
    # pg.press('a')
    # pg.press('v')
    # pg.keyUp('Ctrl')
    t = t + 1

