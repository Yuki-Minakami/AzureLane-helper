#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEventEnemy,mission,drag,fightEnd,battle,getElite,snapshot,getEnemy


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'


def enter():
    click((1250,400))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(7)
    drag(1000,250,0,50)
    sleep(1)

def fight(current):
    enemy = getEventEnemy()
    print("enemy is ",enemy)
    # if len(enemy) == 0:
    #     drag(1000,250,-50,-300)
    #     sleep(1)
    #     enemy = getEventEnemy()

    boss  = match(shotPath, 'images/eventBoss.jpg')
    print("boss is ",boss)

    if len(boss) != 0:
        print("boss is ",boss)
        next = boss[0]
        type = 'boss'
    else : 
        next,distance = findNear(current,enemy)
        type = 'normal'

    print("next is",next)
    access = goto(next,enemy)
    if access == False:
        type='normal'
    # sleep(8)
    # click((1550,900))
    # sleep(1)
    battle(type,bossTime,normalTime,extraTime)
    return type,next

poch = 0
bossTime = 80
normalTime = 60
extraTime = 10

current = [(900,800)]
while True:
    count = 0
    enter()
    mission()
    sleep(1)
    poch+=1
    print("current ",poch)
    while(True):
        type,next = fight(current)
        count += 1
        if(type == 'boss'):
            break

# enemy = getEventEnemy()
# print("enemy is ",enemy)