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
    boss  = match(shotPath, 'images/boss.jpg')

    global count
    
    if count == 0:
        for e in enemy:
            if 650 < e[0] < 950 and  650 <e[1]<850:
                next = e
                type = 'normal'
                sleep(2)
    else:
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

    access = goto(next,enemy)
    if access == False:
        type='normal'
    battle(type,bossTime,normalTime,extraTime)
    return type,next


poch = 0
bossTime = 100
normalTime = 80
extraTime =20

initialMark = (1105,727)
# displayedBoss = []




while True:
    
    enter()
    mission()
    drag(1000,400,-55,0)
    sleep(1)
    poch+=1
    print("current ",poch)
    count = 0
    displayedBoss = []
    current = [(1500,800)]

    while(True):

        type,next = fight(current)
        count += 1
        if count == 5:
            print("-----------switch-----------")
            current = [(600,600)]
            click((1450,950))
            sleep(4)
            snapshot()
            drag(1000,400,-300,150)
            
        if(type == 'boss'):
            break



# enemy = getEnemy()
# print("enemy is ",enemy)

# gotoSafe()

# drag(1000,400,-300,150)