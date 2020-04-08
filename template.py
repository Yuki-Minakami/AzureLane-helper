import cv2
import numpy as np
# 1.模板匹配
img = cv2.imread('images/i9.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
template = cv2.imread('images/cl.jpg', 0)
h, w = template.shape[:2]  # rows->h, cols->w

# 6种匹配方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img2 = img.copy()

    # 匹配方法的真值
    method = eval(meth)
    res = cv2.matchTemplate(img_gray, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 如果是平方差匹配TM_SQDIFF或归一化平方差匹配TM_SQDIFF_NORMED，取最小值
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.circle(res, top_left, 10, 0, 2)
    # 画矩形|
    print(top_left,bottom_right)
    cv2.rectangle(img2, top_left, bottom_right, (0, 255, 0), 2)