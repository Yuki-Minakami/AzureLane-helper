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
    click((1360,800))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(4)
    sleep(1)


def fight(current):
    print("扫描敌人")
    enemy = getEnemy()
    boss  = match(shotPath, 'images/boss.jpg')

    
    if len(boss) != 0:
        print("boss 出现",boss)

        next = boss[0]
        global displayedBoss
        displayedBoss = boss
        type = 'boss'
    elif len(displayedBoss) != 0:
        next = displayedBoss[0]
        type = 'boss'
    else: 
        print("敌人列表",enemy)
        next,distance = findNear(current,enemy)
        type = 'normal'

    print("下一步",next)
    access = goto(next,enemy)
    if access == False:
        type='normal'
    battle(type,bossTime,normalTime,extraTime)
    return type,next


poch = 0
bossTime = 100
normalTime = 60
extraTime =10

initialMark = (1105,727)


while True:
    print("进入关卡")
    enter()
    mission()
    print("自定义拖动")
    drag(1000,400,-55,0)
    sleep(1)
    poch+=1
    print("当前为第",poch,"盘")
    count = 0
    displayedBoss = []
    current = [(1500,800)]

    while(True):

        type,next = fight(current)
        count += 1
        if count == 4:
            print("---------切换编队--------")
            current = [(600,600)]
            click((1450,950))
            sleep(4)
            snapshot()
            drag(1000,400,-150,100)
            
        if(type == 'boss'):
            break