#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,findLeft


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'



def enter():
    click((1300,300))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(5)
    mission()
    sleep(6)

def fight():
    enemy = getEnemy()
    boss  = match(shotPath, 'images/boss.jpg')
    current = match(shotPath, 'images/bullet.jpg')
   

    print("boss is", boss)
    if len(current) == 0:
        current = [(800,100)]

    if len(boss) != 0:
        next = boss[0]
        type = 'boss'
    else: 
        print("enemy is ",enemy)
        next = findLeft(current,enemy)
        type = 'normal'
    print("next is",next)
    result = goto(next)
    if result == False:
        goto(next)
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


poch = 0


bossTime = 95
normalTime = 70

while True:
    enter()
    click((1050,260))
    sleep(5)
    click((600,60))
    sleep(1)
    click((1250,260))
    sleep(1)
    poch+=1
    print("current ",poch)
    while(True):
        type = fight()
        if(type == 'boss'):
            break


