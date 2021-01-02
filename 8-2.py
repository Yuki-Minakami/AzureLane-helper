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
    click((400,600))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(4)
    drag(1000,400,0,20)
    sleep(1)

def fight(current):
    enemy = getEnemy()
    # print("enemy is ",enemy)
    boss  = match(shotPath, 'images/boss.jpg')

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
bossTime = 120
normalTime = 75
extraTime =20

while True:
    enter()
    mission()
    sleep(1)
    poch+=1
    print("current ",poch)
    count = 0
    displayedBoss = []
    current = [(1200,600)]

    while(True):
        type,next = fight(current)
        count += 1
        if count == 3:
            current = [(400,300)]
        if(type == 'boss'):
            break