import VegasPRO as VPro
import VegasPRO_filters as VPro_F
import VegasPROMusic as VPro_M
import pyautogui as pg
import time
import random as rnd
import string
import Ch_Yt_Upload as CYU

time.sleep(3)

vids = 1
while vids <= 30:
    videoSeed: object = ((rnd.choice(string.ascii_letters[:26])) + (rnd.choice(string.ascii_letters[:26])) + (rnd.choice(string.ascii_letters[:26])))
    print(videoSeed)
    time.sleep(2)
    pg.click(128, 712)  # Удаление пр
    time.sleep(0.5)
    pg.press('del')
    time.sleep(0.5)
    pg.click(128, 712)  # Удаление пр
    time.sleep(0.5)
    pg.press('del')
    time.sleep(0.5)
    pg.press('home')
    time.sleep(0.5)
    pg.keyDown('ctrl')
    pg.keyDown('shift')
    pg.press('q')
    pg.keyUp('shift')
    pg.press('q')
    pg.keyUp('Ctrl')
    time.sleep(0.5)
    pg.click(400, 724)
    pg.press('home')
    VPro.Vid_s()  # Вызов другого
    pg.click(320, 630)
    VPro_F.Vid_f()
    VPro_M.Musik()  # Music
    pg.click(25, 41)  # Рендер
    time.sleep(1)
    pg.click(65, 196)
    time.sleep(2)
    pg.typewrite("Random video and effects and sound and ")
    pg.typewrite(videoSeed)
    pg.press(['enter'])
    time.sleep(60)
    CYU.Up_add()

