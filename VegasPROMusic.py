def Musik ():
    import pyautogui as pg
    import random as rnd
    import time

    time.sleep(2)

    pg.click(725, 710)
    pg.press('home')  # Music
    pg.click(150, 633)

    i = 1

    while i <= 2:
        vid_X = rnd.randrange(55, 1023)
        vid_Y = rnd.randrange(120, 336)
        pg.doubleClick(vid_X, vid_Y)
        time.sleep(1)
        i = i + 1

