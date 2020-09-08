#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,drag,fightEnd


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

    question2 = match(shotPath, 'images/question2.PNG')
    question1 = match(shotPath, 'images/question.JPG')

    if len(question1) > 0:
        question = question1
    elif len(question2) > 0:
        question = question2
    else:
        question = []

    # print("question is ",question)
    if len(question) > 0:
        x= question[0][0]
        y= question[0][1]
        goto((x,y+100),enemy)
        sleep(8)
        click((x,y+100))
        sleep(1)

    # print("boss is", boss)

    if len(boss) != 0:
        next = boss[0]
        type = 'boss'
    else: 
        print("enemy is ",enemy)
        next,distance = findNear(current,enemy)
        type = 'normal'
    print("next is",next)
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
bossTime = 120
normalTime = 60

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
