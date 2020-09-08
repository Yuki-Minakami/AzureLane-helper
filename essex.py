#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os

from template import match
from cv import request
import copy
from math import pow
from time import sleep

from common import click, goto,findNear,findNext,getEnemy,mission

def cal():
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
    return

while(True):
    print("-----")
    click((1550,450))
    sleep(1)
    click((1550,900))
    sleep(2)
    click((1600,950))
    sleep(3)
    click((750,750))
    sleep(95)
    cal()
    sleep(5)



