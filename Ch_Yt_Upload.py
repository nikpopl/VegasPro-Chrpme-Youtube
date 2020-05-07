def Up_add():
    import pyautogui as pg
    import time

    time.sleep(2)

    pg.click(147, 1060)
    time.sleep(3)
    pg.typewrite('https://studio.youtube.com/channel/UCIgZQhuhnKJW_gsAGszDiaA/videos/'
                 'upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C'
                 '%22sortOrder%22%3A%22DESCENDING%22%7D')
    pg.press('enter')
    time.sleep(5)
    pg.click(483, 500)
    time.sleep(3)
    pg.doubleClick(437, 282)
    time.sleep(5)
    pg.click(106,571)
    pg.typewrite('This video was made by Bot.')
    # Ifthere'
    # 'is an obscene statement, the author '
    # 'is not responsible.это видео сделано'
    # ' Ботомесли будет нецензурное высказы'
    # 'вание автор ответственности не несет
    pg.click(915, 961)
    time.sleep(2)
    pg.click(66, 747)
    time.sleep(1)
    pg.doubleClick(915, 961)
    time.sleep(1)
    pg.click(112, 441)
    time.sleep(0.5)
    pg.click(882, 962)
    time.sleep(20)
    pg.click(242, 29)
