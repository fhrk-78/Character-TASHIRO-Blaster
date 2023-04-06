# -*- coding: utf-8 -*-
import pyautogui as pg
import asyncio as ac
import random as rd

mks = '田代大好き'

async def toLINE(wm: str):
    pg.typewrite(wm)
    pg.hotkey('alt', 'enter')

def main():
    while True:
        ac.run(toLINE(mks + int(rd.uniform(0, 20030314))))

if __name__ == '__main__':
    main()
