import sys, cv2
import numpy as np
import math

def scale(src, x_scale, y_scale):
    h,w = src.shape[:2]
    aff = np.array([[x_scale,0,0],[0,y_scale,0]], dtype=np.float32)
    dst = cv2.warpAffine(src,aff,(x,y))
    return dst

src = cv2.imread('mission_01.jpg')

if src is None:
    sys.exit('image load failed')


dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
dst2 = cv2.resize(src,(0,0),fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst3 = cv2.resize(src,(0,0),fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src',src)
cv2.imshow('cubic', dst1)
cv2.imshow('nearest', dst2)
cv2.imshow('lanczos4', dst3)

cv2.waitKey()
cv2.destroyAllWindows()
