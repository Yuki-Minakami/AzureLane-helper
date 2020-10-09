#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEventEnemy,mission,drag,fightEnd,battle,getElite,snapshot


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'


def enter():
    click((1400,550))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(4)
    drag(1000,400,0,150)
    sleep(1)


def fight(current):
    enemy = getEventEnemy()

    elite = getElite()
    print("enemy is ",enemy)

    print("elite is ",elite)

    boss  = match(shotPath, 'images/eventBoss.jpg')
    print("boss is ",boss)

    if(len(boss) == 0 and len(enemy) == 0 and len(elite) == 0):
        drag(1000,400,0,100)
        enemy = getEventEnemy()
        elite = getElite()

    if len(boss) != 0:
        sleep(1)
        click((1400,1000))
        sleep(2)
        snapshot()
        boss  = match(shotPath, 'images/event/eventBoss.jpg')
        print("boss is ",boss)
        next = boss[0]
        type = 'boss'
    elif len(elite) != 0: 
        print("elite is ",elite)
        next,distance = findNear(current,elite)
        type = 'normal'
    else : 
        next,distance = findNear(current,enemy)
        type = 'normal'
    # else :
    #     drag(1000,400,0,-200)

    print("next is",next)
    access = goto(next,enemy)
    if access == False:
        type='normal'
    battle(type,bossTime,normalTime,extraTime)
    return type,next

poch = 0
bossTime = 110
normalTime = 60
extraTime = 30

current = [(800,800)]
count = 0
while True:
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
