#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,drag,fightEnd,battle,snapshot


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'
markPath = 'images/mark.jpg'


def enter():
    click((1160,420))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(4)
    sleep(1)



def fight(current):
    enemy = getEnemy()
    # print("enemy is ",enemy)
    boss  = match(shotPath, 'images/boss.jpg')

    global count
    if count == 5 and len(boss) == 0:
        drag(1000,400,50,50)
        snapshot()
        boss  = match(shotPath, 'images/boss.jpg')
        print("boss is ",boss)
        enemy = getEnemy()



    if len(boss) != 0:
        print("boss is ",boss)

        next = boss[0]
        global displayedBoss
        displayedBoss = boss
        type = 'boss'
    elif len(displayedBoss) != 0:
        next = displayedBoss[0]
        type = 'boss'
    else: 
        # print("enemy is ",enemy)
        next,distance = findNear(current,enemy)
        type = 'normal'
    print("next is",next)
    access = goto(next,enemy)
    if access == False:
        type='normal'
    battle(type,bossTime,normalTime,extraTime)
    return type,next


poch = 0
bossTime = 90
normalTime = 75
extraTime =15
current = [(1500,800)]
initialMark = (1105,727)
# displayedBoss = []


while True:
    enter()
    mission()
    sleep(1)
    poch+=1
    print("current ",poch)
    count = 0
    displayedBoss = []

    while(True):
        type,next = fight(current)
        count += 1
        if count == 5:
            print("-----------switch-----------")
            click((1450,950))
            sleep(4)
            snapshot()
            currentMark = match(shotPath, markPath)
            print("currentMark is ",currentMark)

            if initialMark[0] < currentMark[0][0]:
                drag(1000,400,-20,-30)
            else:
                drag(1000,400,20,30)
            sleep(1)
        if(type == 'boss'):
            break

# click((1450,950))
# sleep(4)
# snapshot()
# currentMark = match(shotPath, markPath)
# print("currentMark is ",currentMark)

# drag(1000,400,-50,-50)

# snapshot()
# currentMark = match(shotPath, markPath)
# print("currentMark is ",currentMark)

# drag(1000,400,50,50)