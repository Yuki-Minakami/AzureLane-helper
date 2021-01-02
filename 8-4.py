#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,drag,fightEnd,battle,getQuestion


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'


def enter():
    click((1100,700))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(4)
    drag(1000,400,-50,-20)
    sleep(1)

def fight(current):
    enemy = getEnemy()
    print("enemy is ",enemy)
    boss  = match(shotPath, 'images/boss.jpg')
    print("boss is ",boss)

    question = getQuestion()

    questionAccess = True
    while len(question) > 0:
        x= question[0][0]
        y= question[0][1]
        questionAccess = goto((x,y+100),enemy)
        if(not questionAccess):
            break

        sleep(8)
        click((x,y+100))
        sleep(1)
        del question[0]

    # print("boss is", boss)
    enemy = getEnemy()

    if len(boss) != 0:
        next = boss[0]
        type = 'boss'
    else: 
        # print("enemy is ",enemy)
        next,distance = findNear(current,enemy)
        type = 'normal'
    print("next is",next)
    access = goto(next,enemy)
    if access == False or (not questionAccess):
        type='normal'


    battle(type,bossTime,normalTime,extraTime)
    return type,next


poch = 0
bossTime = 140
normalTime = 70
extraTime = 20

current = [(1500,800)]
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
