def Vid_s ():
    import random as rnd
    import pyautogui as pg
    import time

    time.sleep(2)

    vids = 1
    pg.click(55,632)
    while vids <= 42:
        vid_X = rnd.randrange(200, 950)
        vid_Y = rnd.randrange(120, 505)
        vids = vids + 1
        time.sleep(0.2)
        pg.doubleClick(vid_X, vid_Y)
        pg.typewrite(["left","left"])
