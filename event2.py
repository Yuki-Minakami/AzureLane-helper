#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission,findRight,findFar,roll,getElite,drag


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'


# count =0


def enter():
    click((700,900))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(5)
    mission()
    sleep(6)


def scan():
    enemy = getEnemy()
    elite = getElite()
    boss  = match(shotPath, 'images/boss.jpg')  

    if len(enemy) == 0 and len(elite) == 0 and len(boss) == 0:
        return ['empty','empty']

    print("boss is", boss)

    if len(boss) != 0:
        next = boss[0]
        type = 'boss'
        distance = 0
    elif len(elite) > 0 :
        print("elite is ",elite)
        next = elite[0]
        type = 'elite'
    else:
        print("enemy is ",enemy)
        next, distance = findNear(current,enemy)
        type = 'normal'

    print("next is",next)
    return next,type,distance

def fight():
    next,type,distance = scan()
    # next = result[0]
    # type = result[1]
    if next=='empty':
        drag(1382,750,-250,-200)
        sleep(2)
        next = scan()[0]
    result = goto(next)
    if result == False:
        goto(next)

    global current
    current = [next]
    battle(type,distance)
    return type



def battle(type,distance):
    if type=='boss':
        sleep(bossTime)
    elif type=='elite':
        sleep(eliteTime)
    else :
        sleep(normalTime+int(distance/200))
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


bossTime = 75
normalTime = 65
eliteTime = 70


current = [(300,800)]
poch = 0


while True:
    enter()
    poch +=1
    print("current Poch is " ,poch)

    count = 0 
    while(True):
        count+=1
        type = fight()
        if(type == 'boss'):
            break

# enter()