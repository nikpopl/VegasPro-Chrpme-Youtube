def Vid_f():
    import random as rnd
    import pyautogui as pg
    import time

    time.sleep(2)

    tFX = 65
    FX = 1

    while FX <= tFX:
        vFX = rnd.randrange(100, 620)   # y
        vTL = rnd.randrange(355, 1600)  # x
        FX = FX + 1
        time.sleep(0.2)
        pg.moveTo(75, vFX)
        pg.dragTo(vTL, 710, 0.4)
        pg.click(260,617)
    pg.click(260,122,tFX)