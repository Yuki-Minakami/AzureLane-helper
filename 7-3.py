#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,drag,fightEnd,getQuestion,battle


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'


def enter():
    click((1200,500))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(4)

def find(current,enemy):
    sortedList = sorted(enemy)
    distance = 0

    if(sortedList[0][0]<400):
        distance = (current[0][0]-sortedList[0][0]) + current[0][1] - sortedList[0][1]
        return sortedList[0],distance
    else:
        return findNear(current,enemy)

def fight(current):
    enemy = getEnemy()
    # print("enemy is ",enemy)

    boss  = match(shotPath, 'images/boss.jpg')
    print("boss is ",boss)

    question = getQuestion()
    # print("question is ",question)

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


    if len(boss) != 0:
        global ifBossAppeared
        ifBossAppeared = True
        next = boss[0]
        type = 'boss'
    else: 
        # if(ifBossAppeared):
            
        # print("enemy is ",enemy)
        next,distance = find(current,enemy)
        type = 'normal'

    print("next is",next)
    access = goto(next,enemy)
    if access == False or (not questionAccess):
        type='normal'
    
    battle(type,bossTime,normalTime,extraTime)
    return type,next

poch = 0
bossTime = 110
normalTime = 50
extraTime = 20

ifBossAppeared = False

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
# [(390, 338),(342, 583) (315, 843)]