import cv2 
import numpy as np 
  

def match(main = 'images/battle.jpg',template = 'images/cv.jpg'):
    path = template

    img_rgb = cv2.imread(main) 
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
    template = cv2.imread(template,0) 
    w, h = template.shape[::-1] 

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 

    threshold = 0.8

    loc = np.where( res >= threshold)  

    begin = 0
    result = []
    for pt in zip(*loc[::-1]): 
        if abs(pt[0] -begin) > 50 :
            begin = pt[0]
            result.append((pt[0],pt[1]))
  
    if len(result)==0 and path == 'images/bullet.jpg' :
        result=[(0,0),'current']
    return result


# print(match())

# bbArr = match('images/shot.png', 'images/bb.jpg')
# print(bbArr)