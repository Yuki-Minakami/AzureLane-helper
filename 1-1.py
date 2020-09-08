from common import click,mission,snapshot

from time import sleep


def enter():
    click((260,730))
    sleep(1)
    click((1500,800))
    sleep(1)
    click((1500,900))
    sleep(5)
    mission()
    sleep(4)


def fight():
    click((1250,470))
    sleep(20)

    click((1600,950))
    sleep(1)
    click((1600,950))
    sleep(2.5)
    click((1600,950))
    sleep(5)
    mission()
    sleep(5)



def fight2():
    click((880,540))
    sleep(33)

    click((1600,950))
    sleep(1)
    click((1600,950))
    sleep(2.5)
    click((1600,950))
    sleep(5)
    mission()
    sleep(5)


poch = 0
while True:
    enter()
    poch+=1
    print("current ",poch)
    while(True):
        fight()
        fight2()
        break;


