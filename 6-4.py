#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,fightEnd


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'


def enter():
    click((450,670))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(6)

def fight(current):
    enemy = getEnemy()
    boss  = match(shotPath, 'images/boss.jpg')
    question = match(shotPath, 'images/question.jpg')

    if len(question) > 0:
        x= question[0][0]
        y= question[0][1]
        goto((x,y+100),enemy)
        sleep(6)
        click((600,60))
        sleep(1)
        click((x+150,y+100))
        sleep(2)
        goto((x,y+100),enemy)
        sleep(2)

    # print("boss is", boss)
    # if len(current) == 0:
    #     current = [(800,100)]


    if len(boss) != 0:
        next = boss[0]
        type = 'boss'
    else: 
        # print("enemy is ",enemy)
        next,distance = findNear(current,enemy)
        type = 'normal'
    # print("next is",next)
    access = goto(next,enemy)
    if access == False:
        type='normal'
    battle(type)
    return type,next



def battle(type):
    if type=='boss':
        sleep(bossTime)
    else:
        sleep(normalTime)

    if(not fightEnd()):
        print('-------')
        sleep(15)

    click((1600,950))
    sleep(1)
    click((1600,950))
    click((1600,700))
    # 针对可能的紫船，多点两下
    sleep(2)
    click((800,450))
    sleep(1)
    click((800,450))

    sleep(2)
    click((1600,950))

    sleep(4)
    mission()
    sleep(1)


poch = 0
bossTime = 110
normalTime = 65
current = [(1500,300)]
globalCurrent = current




while True:
    enter()
    mission()
    poch+=1
    print("current ",poch)
    while(True):
        type,next = fight(globalCurrent)
        globalCurrent = [next]
        if(type == 'boss'):
            break
