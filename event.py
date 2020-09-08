#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,findRight,findFar,roll


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'



def enter():
    click((1450,450))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(5)
    mission()
    sleep(6)
    roll(200)


def fight(current):
    enemy = getEnemy()


    boss  = match(shotPath, 'images/event.png')
    boss1  = match(shotPath, 'images/boss1.jpg')
    boss += boss1

    print("boss is", boss)

    if len(boss) != 0:
        next = boss[0]
        type = 'boss'
    else: 
        while( len(enemy) == 0):
            click((250,300))
            roll(500)
            roll(500)
            enemy = getEnemy()

        print("enemy is ",enemy)
        next = findFar(current,enemy)
        type = 'normal'
    

    # print("next is",next)
    result = goto(next)
    if result == False:
        goto(next)

    current = next
    battle(type)
    return type



def battle(type):
    if type=='boss':
        sleep(bossTime)
    else:
        sleep(normalTime)
    click((1600,950))
    sleep(1)
    click((1600,950))
    # 针对可能的紫船，多点两下
    sleep(2)
    click((800,450))
    sleep(0.5)
    click((800,450))

    sleep(2.5)
    click((1600,950))

    sleep(6)
    mission()
    sleep(6)


bossTime = 85
normalTime = 75


current = (450,600)
poch = 0

while True:
    enter()
    poch +=1
    print("current Poch is " ,poch)
    while(True):
        type = fight(current)
        if(type == 'boss'):
            break
