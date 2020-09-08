import os
from time import sleep
from cv import request
from template import match


shotPath = 'images/shot.png'
judgePath = 'images/judge.png'
missionPath = 'images/mission.png'
fightEndPath = 'images/fightEnd.png'


def snapshot():
    if os.path.isfile(shotPath):
        os.remove(shotPath);
    sleep(0.2)
    os.system("setPos.exe shot")

def mission():
    if os.path.isfile(missionPath):
        os.remove(missionPath);
    os.system("setPos.exe mission")
    if request(missionPath) == 'mission': 
        click((950,750))
        sleep(0.5)


def fightEnd():
    snapshot()
    if request(shotPath) == 'end':
        return True
    return False 


def judge():
    if os.path.isfile(judgePath):
        os.remove(judgePath);
    os.system("setPos.exe judge")
    return request(judgePath) != 'cannot'

def click(position):
    str = 'setPos.exe click %d %d'%(position[0],position[1])
    os.system(str)

def roll(dis):
    str = 'setPos.exe roll %d'%(dis)
    os.system(str)

def drag(x,y,dx,dy):
    str = 'setPos.exe drag %d %d %d %d'%(x,y,dx,dy)
    os.system(str)


def findNext(current, enemy):
    max = -float("inf")
    location = current[0][0]+current[0][1]
    result = ""

    for e in enemy:
        distance = abs(e[0]-current[0][0]) + abs(e[1]-current[0][1])
        if distance > max:
            max = distance
            result = e

    return result


def findNear(current,enemy):
    # print('current is ', current)
    # print('enemy is ', enemy)
    location = current[0][0]+current[0][1]
    result = ""
    min = float("inf")

    result = ""
    for e in enemy:
        distance = abs(e[0]-current[0][0]) + abs(e[1]-current[0][1])
        if distance < min : #and distance > 100 :
            min = distance
            result = e

    # print('distance is ', min)
    return result,min

def findFar(current,enemy):
    location = current[0]+current[1]
    max = -float("inf")

    result = ""
    for e in enemy:
        distance = abs(e[0]-current[0]) + abs(e[1]-current[1])
        if distance > max and distance > 100 :
            max = distance
            result = e

    if result != "":
        x = result[0] + 10
        y = result[1] + 10
    return (x,y)

def findRight(current,enemy):
    currentX = current[0][0]
    right = ()
    max = -float("inf")

    for e in enemy:
        if e[0]-currentX > max:
            right = e
            max = e[0]-currentX
    return right

def findLeft(current,enemy):
    currentX = current[0][0]
    left = ()
    max = -float("inf")

    for e in enemy:
        if currentX-e[0] > max:
            left = e
            max = currentX-e[0]
    return left

def getElite():
    elite = match(shotPath, 'images/elite.png')
    elite2 = match(shotPath, 'images/elite1.png')

    elite += elite2
    
    final = []
    for e in elite:
        final.append((e[0]+30,e[1]+100))

    return final


def getMountain():
    elite = match(shotPath, 'images/mountain.png')

    return elite

def getEnemy():
    snapshot()
    bbArr = match(shotPath, 'images/bb.jpg')
    bb2Arr = match(shotPath, 'images/bb2.png')
    bb3Arr = match(shotPath, 'images/bb3.png')
    bb4Arr = match(shotPath, 'images/bb4.png')
    cvArr = match(shotPath, 'images/cv.jpg')
    cv2Arr = match(shotPath, 'images/cv2.jpg')
    ddArr = match(shotPath, 'images/dd.jpg')
    dd2Arr = match(shotPath, 'images/dd2.jpg')

    ddArr+=dd2Arr

    bbArr+=bb2Arr
    bbArr+=bb3Arr
    bbArr+=bb4Arr

    cvArr+= cv2Arr

    transArr = match(shotPath, 'images/trans.jpg')
    transArr2 = match(shotPath, 'images/trans2.jpg')

    result = bbArr+cvArr+ddArr+transArr+transArr2
    final = []

    for item in result:
        if no_same(item, final):
            final.append(item)

    return final


def no_same(target,list):
    for item in list:
        if abs(target[0]-item[0]) < 35 and abs(target[1] -item[1])<35:
            return False
    return True

def goto(position,enemy):
    # origin = position
    # click(position)
    print('---',position)
    click(position)
    # enemy = getEnemy()
    sleep(1)

    access = judge()
    initial = access
    while(access == False) :
        sleep(3)
        type = "normal"
        print("cannot go to", position)
   
        if(position in enemy):
            enemy.remove(position)
        next,distance = findNear([position],enemy)
        print("new position ",next)
        click(next)

        position = next

        sleep(1)
        access = judge()
    
    return initial
    # sleep(60)
    # goto(position)
    



# snapshot()

# request(shotPath)
# print(not fightEnd())
# print(getElite())
# print(getEnemy())
# print(getMountain())

# elite = match(shotPath, 'images/eye.png')
# elite1 = match(shotPath, 'images/weapon2.png')
# elite2 = match(shotPath, 'images/weapon3.png')
# me = match(shotPath, 'images/bullet.jpg')

# print(me)
# print(elite1)
# print(elite2)
# mission()

# drag(1000,400,-50,-20)

